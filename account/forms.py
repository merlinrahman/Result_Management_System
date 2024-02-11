from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from account.models import MyUser




class UserRegistrationForm(UserCreationForm):
    password1=forms.CharField(label="Password", max_length=20, widget=forms.PasswordInput(attrs={'class':'form-control shadow-none'}))
    password2=forms.CharField(label="Confirm Password", max_length=20, widget=forms.PasswordInput(attrs={'class':'form-control shadow-none'}))
    class Meta:
        model = MyUser
        fields = ('full_name', 'email','password1','password2')

        widgets={
            'email':forms.TextInput(attrs={'class':'form-control shadow-none'}),
            'full_name':forms.TextInput(attrs={'class':'form-control shadow-none', 'oninput': "this.value = this.value.replace(/[^a-zA-Z]/g, '')"}),
            
            
        }


class UserLoginForm(forms.ModelForm):
    password = forms.CharField(label="password", widget=forms.PasswordInput)

    class Meta:
        model = MyUser
        fields = ('email','password')

    def clean(self):
        if self.is_valid():
            email=self.cleaned_data['email']
            password=self.cleaned_data['password']

            if not authenticate(email=email,password=password):
                raise forms.ValidationError("Invalid Login Credentials")
