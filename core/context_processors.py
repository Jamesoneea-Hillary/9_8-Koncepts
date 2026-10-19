from .models import SiteSettings
from django.conf import settings as django_settings


def site_settings(request):

    settings = SiteSettings.objects.first()

    return {
        "site_settings": settings,
        "assistant_whatsapp": django_settings.WHATSAPP_NUMBER,
    }
