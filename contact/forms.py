from django import forms
from .models import Contact, Newsletter, Inquiry, ScheduleMeeting


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
        

class ScheduleMeetingForm(forms.ModelForm):
    
    class Meta:
        model = ScheduleMeeting
        fields = "__all__"