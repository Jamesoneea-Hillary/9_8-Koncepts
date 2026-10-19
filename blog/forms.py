from django import forms


class NewsletterSubscriptionForm(forms.Form):

    email = forms.EmailField(
        max_length=254,
    )

    def clean_email(self):
        return self.cleaned_data["email"].lower()
