from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Crud #Profile

class CrudForms(forms.ModelForm):
    class Meta:
        model = Crud
        fields = ['activity','location']
        


class SignUpForms(UserCreationForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['username'].widget.attrs.update({
    #         'name':'username',
    #         'type':'text',
    #         'minlength':'4',
    #         'maxlength':'200',
    #         'class':'form-input',
    #         'placeholder':'Username'
    #     })
    #     self.fields['email'].widget.attrs.update({
    #         'name':'email',
    #         'type':'email',
    #         'minlength':'4',
    #         'maxlength':'200',
    #         'class':'form-input',
    #         'placeholder':'Email'
    #     })
    #     self.fields['password1'].widget.attrs.update({
    #         'name':'password1',
    #         'type':'text',
    #         'minlength':'4',
    #         'maxlength':'200',
    #         'class':'form-input',
    #         'placeholder':'Password'
    #     })
    #     self.fields['password2'].widget.attrs.update({
    #         'name':'password2',
    #         'type':'text',
    #         'minlength':'4',
    #         'maxlength':'200',
    #         'class':'form-input',
    #         'placeholder':'Confirm Password'
    #     })
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class LoginForms(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1']
        # widgets = {
        #     'activity':forms.TextInput(attrs={'value':'placeholder'}),
        #     'location':forms.TextInput(attrs={'value':'placeholde'})
        # }
