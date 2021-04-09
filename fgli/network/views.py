from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Answer

# Create your views here.

def network(request):
	all_questions = Question.objects.filter()
	context = {'all_questions': all_questions}
	return render(request, 'network/network.html',context)

