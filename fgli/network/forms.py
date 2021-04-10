from django import forms
from .models import Question, Answer, UserRoles
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import User
from django.contrib import messages 
from django.utils.safestring import mark_safe

class AnswerForm(forms.Form):
	answer = forms.CharField(max_length=1000)

	def is_valid(self, request):
		valid = super(AnswerForm, self).is_valid()

		if not request.user.is_authenticated:
			messages.error(request, "Please create an account or log in")
			return False

		return True

class QuestionForm(forms.Form):
	title = forms.CharField(max_length=100)
	question = forms.CharField(max_length=10000)
	category = forms.CharField(max_length=50)

	def is_valid(self, request):
		valid = super(QuestionForm, self).is_valid()


		if not request.user.is_authenticated:
			messages.error(request, "Please create an account or log in")
			return False

		# valid = super(QuestionForm, self).is_valid()
		# if not valid:
		# 	return valid
		return True

	# def save(self, request, commit=True):
	# 	current_user = request.user
	# 	new_question = Question()
	# 	new_question.user = current_user
	# 	new_question.title = self.cleaned_data['title']
	# 	new_question.question = self.cleaned_data['question']
	# 	new_question.category = self.cleaned_data['category']
	# 	if commit:
	# 		new_question.save()
	# 		current_user.questions.add(new_question)
	# 	return new_question
		

class MentorApp(forms.Form):
	submission_date = forms.DateTimeField()
	email = forms.CharField(max_length=100)
	employer = forms.CharField(max_length=100)
	portfolio = forms.CharField(max_length=150)
	linkedin = forms.CharField(max_length=100)
	answer1 = forms.CharField(max_length=1000)	# Why do you want to be a mentor
	answer2 = forms.CharField(max_length=1000)	# What are your interests and passion projects

	class Meta:

		fields = ['submission_date', 'email', 'employer', 'portfolio', 'linkedin', 'answer1', 'answer2']

	def is_valid(self, request):
		valid = super(MentorApp, self).is_valid()
		if not valid:
			return valid

		formemail = self.cleaned_data['email']
		user = User.objects.filter(email=formemail)
		if not user:
			messages.error(request, "Please use an email that corresponds to an account")
			return False
		role = UserRoles.objects.get(user=user[0].id)
		if role.professional:
			messages.error(request, "User is already a professional")
			return False
		return True

	def save(self, commit=True, user=0):
		current_user = UserRoles.objects.get(user=user.id)
		current_user.professional = True
		current_user.save()
		messages.info("User is now a proessional")
		return current_user


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
