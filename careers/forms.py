from django import forms

from .models import JobApplication


class JobApplicationForm(forms.ModelForm):

    class Meta:
        model = JobApplication

        fields = [
            "full_name",
            "email",
            "phone",
            "resume",
            "portfolio_url",
            "linkedin_url",
            "github_url",
            "cover_letter",
        ]

        widgets = {
            "full_name": forms.TextInput(
                attrs={
                    "placeholder": "Your full name",
                    "autocomplete": "name",
                }
            ),

            "email": forms.EmailInput(
                attrs={
                    "placeholder": "you@example.com",
                    "autocomplete": "email",
                }
            ),

            "phone": forms.TextInput(
                attrs={
                    "placeholder": "Your phone number",
                    "autocomplete": "tel",
                }
            ),

            "resume": forms.ClearableFileInput(
                attrs={
                    "accept": ".pdf,.doc,.docx",
                }
            ),

            "portfolio_url": forms.URLInput(
                attrs={
                    "placeholder": "https://yourportfolio.com",
                }
            ),

            "linkedin_url": forms.URLInput(
                attrs={
                    "placeholder": "https://linkedin.com/in/yourname",
                }
            ),

            "github_url": forms.URLInput(
                attrs={
                    "placeholder": "https://github.com/yourname",
                }
            ),

            "cover_letter": forms.Textarea(
                attrs={
                    "placeholder": "Tell us about yourself and why you'd be a great fit...",
                    "rows": 7,
                }
            ),
        }

    def clean_resume(self):
        resume = self.cleaned_data["resume"]

        allowed_extensions = [
            ".pdf",
            ".doc",
            ".docx",
        ]

        extension = "." + resume.name.split(".")[-1].lower()

        if extension not in allowed_extensions:
            raise forms.ValidationError(
                "Please upload a PDF, DOC, or DOCX file."
            )

        # Keep uploaded files reasonably sized.
        if resume.size > 5 * 1024 * 1024:
            raise forms.ValidationError(
                "Resume must be 5 MB or smaller."
            )

        return resume