from django import forms

from .models import ContactInquiry


class ContactInquiryForm(forms.ModelForm):

    class Meta:

        model = ContactInquiry

        fields = [
            "full_name",
            "email",
            "phone",
            "company",
            "service",
            "budget",
            "message",
        ]

        widgets = {

            "full_name": forms.TextInput(
                attrs={
                    "placeholder": "Your full name",
                    "class": "contact-input",
                    "autocomplete": "name",
                    "pattern": "[^0-9]*",
                    "title": "Please enter your name without numbers.",
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "placeholder": "you@example.com",
                    "class": "contact-input",
                }
            ),

            "phone": forms.TextInput(
                attrs={
                    "placeholder": "+256...",
                    "class": "contact-input",
                    "type": "tel",
                    "inputmode": "tel",
                    "pattern": "[0-9+().\\s-]*",
                    "title": "Use numbers and common phone separators only.",
                }
            ),

            "company": forms.TextInput(
                attrs={
                    "placeholder": "Company or organisation (optional)",
                    "class": "contact-input",
                }
            ),

            "service": forms.Select(
                attrs={
                    "class": "contact-input",
                }
            ),

            "budget": forms.Select(
                attrs={
                    "class": "contact-input",
                }
            ),

            "message": forms.Textarea(
                attrs={
                    "placeholder": (
                        "Tell us about your project, "
                        "idea or software requirements..."
                    ),
                    "class": "contact-input",
                    "rows": 6,
                }
            ),

        }

    def clean_full_name(self):
        full_name = self.cleaned_data["full_name"].strip()
        if any(character.isdigit() for character in full_name):
            raise forms.ValidationError("Please enter your name without numbers.")
        return full_name

    def clean_phone(self):
        phone = self.cleaned_data["phone"].strip()
        if phone and any(character.isalpha() for character in phone):
            raise forms.ValidationError("Please enter a phone number without letters.")
        if phone and not any(character.isdigit() for character in phone):
            raise forms.ValidationError("Please include at least one digit in the phone number.")
        if phone and any(character not in "+0123456789 ().-" for character in phone):
            raise forms.ValidationError("Use numbers and common phone separators only.")
        return phone
