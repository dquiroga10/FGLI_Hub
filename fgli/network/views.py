from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Question, Answer, UserRoles, MentorApplication
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages 
from .forms import NewUserForm, MentorApp, QuestionForm, AnswerForm
from django.views.decorators.csrf import csrf_protect
from datetime import datetime
from django.utils.safestring import mark_safe
from django.contrib.auth.models import User


# Create your views here.

def network(request):
	all_questions = Question.objects.filter()
	context = {'all_questions': all_questions}
	return render(request, 'network/network.html',context)


def logout_request(request):
	logout(request)
	messages.info(request, "Logged out successfully!")
	return redirect("/network/")

def login_request(request):
	if request.method == 'POST':
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}")
				messages.info(request, f"{user.email}")
				return redirect('/network/')
			else:
				messages.error(request, "Invalid username or password")
		else:
			messages.error(request, "Invalid username or password")
	form = AuthenticationForm()
	return render(request,
				'network/login.html',
				{'form':form})


def register(request):
	if request.method == 'POST':
		form = NewUserForm(request.POST)
		if form.is_valid(request):
			user = form.save()
			username = form.cleaned_data.get("username")
			messages.success(request, f"New Account Created: {username}")
			ur = UserRoles()
			ur.save()
			user.myrole.add(ur)
			# messages.info(request, f"User Is Professional: {user.myrole.all()}")
			login(request, user)
			return redirect('/network/')
		else:
			for msg in form.error_messages:
				messages.error(request, f"{msg}: {form.error_messages[msg]}")

	form = NewUserForm
	messages.info(request, f"Hi Peter :)")
	return render(request,
				  'network/register.html',
				   context={'form':form})

def mentorapp(request):
	if str(request.user) == 'AnonymousUser':
		messages.info(request, "Please log in to apply to become a mentor.")
		return redirect('/network/login/')
	if request.method == 'POST':
		form = MentorApp(request.POST)
		if form.is_valid(request):
			# username = form.cleaned_data.get('username')
			# password = form.cleaned_data.get('password')
			# user = authenticate(username=username, password=password)
			# if user is not None:
			# 	login(request, user)
			# 	messages.info(request, f"You are now logged in as {username}")
			# 	messages.info(request, f"{user.email}")
			# form.save()
			print(request.user)
			current_user = UserRoles.objects.get(user=request.user)
			new_application =  MentorApplication()
			new_application.user = current_user
			new_application.employer = form.cleaned_data['employer']
			new_application.website = form.cleaned_data['website']
			new_application.linkedin = form.cleaned_data['linkedin']
			new_application.a1 = form.cleaned_data['answer1']
			new_application.a2 = form.cleaned_data['answer2']

			
			current_user.professional = True
			current_user.employer = form.cleaned_data['employer']
			current_user.website = form.cleaned_data['website']
			current_user.linkedin = form.cleaned_data['linkedin']
			current_user.a1 = form.cleaned_data['answer1']
			current_user.a2 = form.cleaned_data['answer2']
			
			messages.info(request,f"User is now a proessional")
			
			current_user.save()
			new_application.save()
			current_user.apps.add(new_application)

			return redirect('/network/')
			# else:
			# 	messages.error(request, "Invalid username or password")
		else:
			messages.error(request, "Could not submit application")
	form = MentorApp()
	return render(request, 'network/mentorapp.html',{'form': form})

def create_question(request):
	if str(request.user) == 'AnonymousUser':
		messages.info(request, "Please log in to ask a question.")
		return redirect('/network/login/')
	if request.method == 'POST':
		form = QuestionForm(request.POST)
		if form.is_valid(request):

			current_user = request.user
			new_question = Question()
			new_question.user = current_user
			new_question.title = form.cleaned_data['title']
			new_question.question = form.cleaned_data['question']
			new_question.category = form.cleaned_data['category']
			
			new_question.save()
			current_user.questions.add(new_question)
			#form.save(request)
			return redirect('/network/')
		else:
			messages.error(request, "Error creating question")
	form = QuestionForm
	return render(request, 'network/newquestion.html',{'form': form})

def create_answer(request, q_id):
	if request.method == 'POST':
		form = AnswerForm(request.POST)
		if form.is_valid(request):
			current_user = request.user
			current_question = Question.objects.get(id=q_id)
			new_answer = Answer()
			new_answer.user = current_user
			new_answer.answer = form.cleaned_data['answer']
			new_answer.question = current_question

			new_answer.save()
			current_question.answers.add(new_answer)
			current_question.answers_tot += 1
			current_user.answers.add(new_answer)

			current_question.save()
			return redirect(f'/network/{q_id}/')
		else:
			messages.error(request, "Error creating answer")
	form = AnswerForm()
	return render(request,'network/newanswer.html',{'form':form})

def specific_question(request, q_id):
	answers = Answer.objects.filter(question = q_id)

	return render(request, 'network/question.html', {'question':Question.objects.get(id=q_id), 'answers': answers})
