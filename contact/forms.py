from django import forms
from .models import Contact, Newsletter, Inquiry


class ContactForm(forms.ModelForm):
    
    class Meta:
        model = Contact
        fields = "__all__"
        

class NewsletterForm(forms.ModelForm):
    
    class Meta:
        model = Newsletter
        fields = "__all__"
        

class InquiryForm(forms.ModelForm):
    
    class Meta:
        model = Inquiry
        fields = "__all__"