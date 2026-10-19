import json
import uuid
from unittest.mock import patch

from django.test import TestCase, override_settings, Client
from django.urls import reverse
from django.core.cache import cache

from .models import AssistantConversation
from services.models import Service
from contact.models import ContactInquiry


class AssistantTests(TestCase):
    def setUp(self):
        cache.clear()

    def post_chat(self, client, message="Hello", conversation_id=None):
        data = {"message": message}
        if conversation_id:
            data["conversation_id"] = conversation_id
        return client.post(reverse("core:chatbot_reply"), json.dumps(data), content_type="application/json")

    @patch("core.views._assistant_completion", return_value="A helpful answer")
    def test_chat_creates_session_owned_conversation(self, completion):
        response = self.post_chat(self.client)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()["reply"], "A helpful answer")
        conversation = AssistantConversation.objects.get()
        other = Client()
        self.assertEqual(self.post_chat(other, conversation_id=conversation.pk).status_code, 403)

    def test_empty_and_oversized_messages_rejected(self):
        self.assertEqual(self.post_chat(self.client, " ").status_code, 400)
        self.assertEqual(self.post_chat(self.client, "x" * 1201).status_code, 400)

    @patch("core.views._assistant_completion", return_value="")
    def test_provider_failure_has_helpful_fallback(self, completion):
        response = self.post_chat(self.client, "hello")
        self.assertEqual(response.status_code, 200)
        self.assertIn("AI guide", response.json()["reply"])

    @patch("core.views._assistant_completion", return_value="ok")
    @override_settings(ASSISTANT_RATE_LIMIT=1)
    def test_rate_limit(self, completion):
        self.assertEqual(self.post_chat(self.client).status_code, 200)
        self.assertEqual(self.post_chat(self.client).status_code, 429)

    def test_published_services_only_in_retrieval(self):
        Service.objects.create(title="Public web apps", slug="public", short_description="web app services", description="build web app", status="published")
        Service.objects.create(title="Private draft", slug="private", short_description="web app services", description="secret project", status="draft")
        from .views import _assistant_knowledge
        knowledge = _assistant_knowledge("web app")
        self.assertIn("Public web apps", knowledge)
        self.assertNotIn("Private draft", knowledge)

    def test_assistant_inquiry_reuses_contact_validation_and_consent(self):
        self.client.get(reverse("core:home"))
        response = self.client.post(reverse("core:assistant_inquiry"), json.dumps({"consent": False}), content_type="application/json")
        self.assertEqual(response.status_code, 400)
        data = {"consent": True, "submission_token": str(uuid.uuid4()), "full_name": "A Client", "email": "bad", "service": "website", "budget": "", "message": "Build a site"}
        response = self.client.post(reverse("core:assistant_inquiry"), json.dumps(data), content_type="application/json")
        self.assertEqual(response.status_code, 400)
        data["email"] = "client@example.com"
        response = self.client.post(reverse("core:assistant_inquiry"), json.dumps(data), content_type="application/json")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ContactInquiry.objects.get().source, "assistant")
        self.assertEqual(self.client.post(reverse("core:assistant_inquiry"), json.dumps(data), content_type="application/json").status_code, 409)

    def test_whatsapp_contact_fallback_and_shared_widget(self):
        response = self.client.get(reverse("core:home"))
        self.assertContains(response, "Nine Eight Assistant")
        self.assertContains(response, reverse("contact:contact"))

    @override_settings(WHATSAPP_NUMBER="256700123456")
    def test_whatsapp_number_is_injected_from_configuration(self):
        response = self.client.get(reverse("core:home"))
        self.assertContains(response, 'data-whatsapp="256700123456"')

    def test_csrf_protects_assistant_post(self):
        client = Client(enforce_csrf_checks=True)
        response = client.post(reverse("core:chatbot_reply"), json.dumps({"message": "hi"}), content_type="application/json")
        self.assertEqual(response.status_code, 403)
