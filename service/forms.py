from django import forms
class User_Registeration(forms.Form):
    name=forms.CharField(max_length=100)
    email=forms.EmailField()
    phone=forms.NumberInput()
    message=forms.CharField(widget=forms.Textarea())
    image=forms.ImageField()
    password=forms.CharField(widget=forms.PasswordInput())
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    check=forms.CheckboxInput()

