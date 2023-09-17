from django import forms
from django.forms import ModelForm
from .models import Message

class MessageForm(ModelForm):
      class Meta:
            model = Message
            fields =['name', 'email','subject', 'message']

            labels={
                  'name':'','email':'', 'subject':'', 'message':''
            }

            widgets ={
                  'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Your Name'}),
                  'email':forms.EmailInput(attrs={'class':'form-control', 'placeholder':'Your Email'}),
                  'subject':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Subject'}),
                  'message':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Your Message'})  
            }
