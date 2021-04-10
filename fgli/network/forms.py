from django import forms
from .models import Question, Answer
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django.contrib import messages 
from django.utils.safestring import mark_safe



class NewUserForm(UserCreationForm):

	first_name = forms.CharField(max_length=50)
	last_initial = forms.CharField(max_length=1)
	email = forms.CharField(max_length=100)

	class Meta:

		model = User

		fields = ['first_name', 'last_initial', 'email', 'username', 'password1', 'password2']

	def is_valid(self, request):
		valid = super(NewUserForm,self).is_valid()

		if not valid:
			return valid

		formemail = self.cleaned_data['email']

		#add in our verification of form
		if User.objects.filter(email=formemail):
			messages.error(request, "Email is not unique in system")
			return False

		return True 

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_initial']
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user
