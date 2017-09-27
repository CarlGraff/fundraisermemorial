from django import forms
from fundraiser_app.models import FMItem
from django.forms.widgets import RadioSelect

class FMItemForm(forms.ModelForm):
    RADIO_CHOICES = [['1', 'Radio 1'], ['2', 'Radio 2']]
    type = forms.ChoiceField(widget=RadioSelect(), choices=RADIO_CHOICES)

    class Meta():
        model = FMItem
        fields = ['type', 'purchaser', 'name', 'placement', 'logo', 'line1', 'line2', 'line3', 'line4', 'line5', 'row', 'col', 'email', 'install_date']

        # widgets = {
        #     'name': forms.CharField()
        # }
