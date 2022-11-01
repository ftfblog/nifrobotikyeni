from django.forms import ModelForm
from .models import contactform
from django.forms import Textarea,TextInput,Select


class contactform(ModelForm):
    class Meta:
        model  = contactform
        fields = ["first_name","last_name","email","phone","Company","emailorphone","message"]

        widgets = {
            'first_name': TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'last_name': TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'email': TextInput(
                attrs={
                    'class': 'form-control',
                    
                }
            ),
            'phone': TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'Company': TextInput(
                attrs={
                    'class': 'form-control'
                }
            ),
            'message': Textarea(
                attrs={
                    'class': 'form-control'
                }
            ),
        }
