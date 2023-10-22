from django import forms
from .models import Crud

class CrudForms(forms.ModelForm):
    class Meta:
        model = Crud
        fields = [
            'activity',
            'location'
        ]

        # widgets = {
        #     'activity':forms.TextInput(attrs={'value':'placeholder'}),
        #     'location':forms.TextInput(attrs={'value':'placeholde'})
        # }