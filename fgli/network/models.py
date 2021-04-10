from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions', null=True)
    title = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=50, null=True)
    question = models.CharField(max_length=10000)
    datetime = models.DateTimeField(auto_now=True)
    answers_tot = models.IntegerField(default=0)
    
    def __str__(self):
        return f"question: {self.question}"

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='questions', null=True)
    answer = models.CharField(max_length=500)
    datetime = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"question id: {question.id} answer: {self.answer}"

class Blog_Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog', null=True)
    name = models.CharField(max_length=100)
    text = models.CharField(max_length=10000)

    def __str__(self):
        return f"blog: {self.name}"

class UserRoles(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='myrole', null=True)
    professional = models.BooleanField(default=False)

    def __str__(self):
        return f"role: {self.professional}" 