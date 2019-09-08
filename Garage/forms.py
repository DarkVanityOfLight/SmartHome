from django import forms


class GaragenForm(forms.Form):

    SollStatus = forms.ChoiceField(choices=[('Auf','Auf'),('Zu','Zu')], widget=forms.Select(attrs={
        'class': "my_form",
    }))

