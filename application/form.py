from django import forms


class ContactForm(forms.Form):
    title = forms.CharField()
    description = forms.CharField()
