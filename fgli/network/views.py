from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Question, Answer, UserRoles
from django.contrib.auth.forms import  AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages 
from .forms import NewUserForm
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
			messages.info(request, f"User Is Professional: {user.myrole.all()}")
			login(request, user)
			return redirect('/network/')
		else:
			for msg in form.error_messages:
				messages.error(request, f"{msg}: {form.error_messages[msg]}")

	form = NewUserForm
	messages.info(request, f"Bryan is so cute")
	return render(request,
				  'network/register.html',
				   context={'form':form})

def mentorapp(request):
	all_questions = User.objects.filter()
	context = {'all_questions': all_questions}
	return render(request, 'network/mentorapp.html',context)
