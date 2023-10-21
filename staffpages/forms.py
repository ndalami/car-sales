from django import forms
from django.forms import ModelForm
from cars.models import Car

class CarForm(ModelForm):
      class Meta:
            model = Car
            fields =['carName','carPrice','carEngine','fuel','transmission','color','doors',
                     'carImg','carSdImg','carFrImg','carInImg']

            labels={
                  'Car name':'','Price':'', 'Engine':'', 'Fuel':'', 'Transmission':'', 'Color':'', 'Doors':'',
                  'First Image':'','Second Image':'','Third Image':'','Fourth Image':'',
            }

            widgets ={
                  'carName':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Car Name'}),
                  'carPrice':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Price'}),
                  'carEngine':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Engine CC'}),
                  'fuel':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Fuel type'}),
                  'transmission':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Transmission'}),
                  'color':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Color'}),
                  'doors':forms.NumberInput(attrs={'class':'form-control', 'placeholder':'Number of Doors'}),
                  'carImg':forms.FileInput(attrs={'class':'form-control', 'placeholder':'First Image'}),
                  'carSdImg':forms.FileInput(attrs={'class':'form-control', 'placeholder':'Second Image'}),
                  'carFrImg':forms.FileInput(attrs={'class':'form-control', 'placeholder':'Third Image'}),
                  'carInImg':forms.FileInput(attrs={'class':'form-control', 'placeholder':'Fourth Image'}),
                  
            }

