from django import forms


""" 
Using Django Form API https://docs.djangoproject.com/en/2.1/ref/forms/api/
"""

class ContactForm(forms.Form):
    from_email = forms.EmailField(required=True)
    subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)