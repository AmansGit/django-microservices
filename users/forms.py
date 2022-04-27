from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile


class UserForm(UserCreationForm):
	first_name = forms.CharField(max_length=50, required=True,
		widget=forms.TextInput(attrs={'placeholder': '*Your First Name'}))
	last_name = forms.CharField(max_length=50, required=True,
		widget=forms.TextInput(attrs={'placeholder': '*Your Last Name'}))
	username = forms.EmailField(max_length=254, required=True,
		widget=forms.TextInput(attrs={'placeholder': '*Email-id'}))
	password1 = forms.CharField(
		widget=forms.PasswordInput(attrs={'placeholder': '*Password', 'class': 'password'}))
	password2 = forms.CharField(
		widget=forms.PasswordInput(attrs={'placeholder': '*Confirm Password', 'class': 'password'}))

	# recaptcha Token
	token = forms.CharField(
		widget=forms.HiddenInput())

	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'username', 'password1', 'password2')



class AuthForm(AuthenticationForm):
	username = forms.CharField(max_length=254, required=True,
		widget=forms.TextInput(attrs={'placeholder': '*Email-id'}))
	password = forms.CharField(
		widget=(forms.PasswordInput(attrs{'placeholder': 'password'})))

	class Meta:
		model = User
		fields = ('username', 'password')



class UserProfileForm(forms.ModelForm):
	address = forms.CharField(max_length=200, required=True, widget=forms.HiddenInput())
	town = forms.CharField(max_length=100, required=True, widget=forms.HiddenInput())
	post_code = forms.CharField(max_length=6, required=True, widget=forms.HiddenInput())
	country = forms.CharField(max_length=20, required=True, widget=forms.HiddenInput())
	longitude = forms.CharField(max_length=30, required=True, widget=forms.HiddenInput())
	latitude = forms.CharField(max_length=30, required=True, widget=forms.HiddenInput())

	# profile_picture = forms.ImageField(upload_to='/image')

	class Meta:
		model = UserProfile
		fields = ('address', 'town', 'post_code', 'country', 'longitude', 'latitude')
