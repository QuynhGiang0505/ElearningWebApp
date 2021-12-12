from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username', 'email', 'password1', 'password2']

	def clean(seft):
		cleaned_data =super().clean()
		email=seft.cleaned_data.get('email')
		if User.objects.filter(email=email).exists():
	 			raise forms.ValidationError('Email is already exists!')
