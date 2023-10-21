from django import forms
from django.forms import ModelForm
from .models import Message

class MessageForm(ModelForm):
      class Meta:
            model = Message
            fields =['fname', 'sname','phone', 'message']


            labels={
                  'fname':'','sname':'', 'phone':'', 'message':''
            }

            widgets ={
                  'fname':forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
                  'sname':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Second Name'}),
                  'phone':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone Number'}),
                  'message':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Your Message'})  
            }
