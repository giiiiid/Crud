from django import forms
from .models import Crud, Profile

class CrudForms(forms.ModelForm):
    class Meta:
        model = Crud
        fields = [
            'activity',
            'location'
        ]

class UserAuthenticationForms(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['email']
        # widgets = {
        #     'activity':forms.TextInput(attrs={'value':'placeholder'}),
        #     'location':forms.TextInput(attrs={'value':'placeholde'})
        # }
