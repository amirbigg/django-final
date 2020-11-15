from django import forms
from .models import Profile


class UserRegistrationForm(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))


class UserLoginFrom(forms.Form):
	username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control'}))


class ProfileImageForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('image',)