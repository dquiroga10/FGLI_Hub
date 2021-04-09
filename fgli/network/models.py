from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions', null=True)
	question = models.CharField(max_length=500)
	

	def __str__(self):
		return f"question: {self.question}"

class Answer(models.Model):
	question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='questions', null=True)
	answer = models.CharField(max_length=500)

	def __str__(self):
		return f"question id: {question.id} answer: {self.answer}"
