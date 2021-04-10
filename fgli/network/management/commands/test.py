from django.core.management.base import BaseCommand

from network.models import Question, Answer
from django.contrib.auth.models import User
import logging

class Command(BaseCommand):

	help = "Release the spiders"
	def handle(self, *args, **kwargs):
		print(Question.objects.filter())

		for i in Question.objects.filter():
			for j in Answer.objects.filter(question=i.id):
				a = Answer.objects.get(id=j.id)
				a.delete()