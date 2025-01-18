from django import forms
from .models import ContactMessage

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Tam Ad'}),
            'email': forms.EmailInput(attrs={'placeholder': ' E-poçt Ünvanı'}),
            'subject': forms.TextInput(attrs={'placeholder': 'Mövzu'}),
            'message': forms.Textarea(attrs={'placeholder': 'Sual / Mesaj', 'rows': 4}),
        }
