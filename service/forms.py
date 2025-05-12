from django import forms
from django.core import validators
class User_Registeration(forms.Form):
    name=forms.CharField(max_length=100)
    email=forms.EmailField()
    phone=forms.NumberInput()
    message=forms.CharField(widget=forms.Textarea())
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())

    def clean(self):
        clean_data=super().clean()
        password=clean_data.get('password')
        confirm_password=clean_data.get('confirm_password')
        if password!=confirm_password:
            raise forms.ValidationError("Password dos not match")
