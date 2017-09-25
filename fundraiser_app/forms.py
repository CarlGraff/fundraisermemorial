from django import forms
from fundraiser_app.models import FMItem

class FMItemForm(forms.ModelForm):
    class Meta():
        model = FMItem
        fields = '__all__'

        widgets = {
            'name': forms.TextField()
        }
