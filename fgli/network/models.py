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

class Blog_Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog', null=True)
    name = models.CharField(max_length=100)
    text = models.CharField(max_length=10000)

    def __str__(self):
        return f"blog: {self.name}"
