from django import forms
from .models import important_thing


from django.contrib.admin import widgets

class pinned_message_form(forms.ModelForm):

    class Meta:

        model = important_thing

        fields = ('Datum', 'body')
        widgets = {
            'Datum': widgets.AdminDateWidget(attrs={
                'class': 'Datum',
                "id": "datepicker",
            }),
            
            'body': forms.Textarea(attrs={
                'id': "Body",
                'rows': '3',
                'class': 'my_body',
            }),
        }

        labels = {
            'body': 'Nachricht'
        
        }
