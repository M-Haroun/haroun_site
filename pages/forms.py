from django import forms 
from .models import Message

class ContactForm(forms.ModelForm):
    class Meta:
        model = Message
        #fields = '__all__'
        exclude = ['posted']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder':'Enter your full name'}),
            'email': forms.EmailInput(attrs={'placeholder':'example@host.com'}),
            'phone': forms.TextInput(attrs={'placeholder':'Enter your phone number'}),
            'message': forms.Textarea(attrs={'placeholder':'Enter your message'}),
        } 