from django import forms
from .models import message
from django.forms import modelformset_factory


class chatt_Form(forms.ModelForm):
    
    class Meta:
        model = message
        fields = ('Nachricht',)
        labels = {
            'Nachricht': '',
        }
        
        widgets = {

            'Nachricht': forms.Textarea(attrs={
                'class': "nachricht_form",
                'rows': '1',
                'autocomplete': 'off',
            })
            

        }

