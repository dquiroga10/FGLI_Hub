from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='questions', null=True)
    title = models.CharField(max_length=100, null=True)
    category = models.CharField(max_length=50, null=True)
    question = models.CharField(max_length=10000, null=False, default="Sample question")
    datetime = models.DateTimeField(auto_now=True)
    answers_tot = models.IntegerField(default=0)
    
    def __str__(self):
        return f"question: {self.question}"

class Answer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='answers', null=True)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='answers', null=True)
    answer = models.CharField(max_length=1000)
    datetime = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"question id: {self.question.id} answer: {self.answer}"

class Blog_Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='blog', null=True)
    name = models.CharField(max_length=100)
    text = models.CharField(max_length=10000)

    def __str__(self):
        return f"blog: {self.name}"

class UserRoles(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='myrole', null=True)
    professional = models.BooleanField(default=False)
    fgli = models.BooleanField(default=False)

    employer = models.CharField(max_length=50, null=True)
    website = models.CharField(max_length=100, null=True)
    linkedin = models.CharField(max_length=100, null=True)
    a1 = models.CharField(max_length=1000, null=True) # Why do you want to be a mentor
    a2 = models.CharField(max_length=1000, null=True) # What are your interests and passion projects

    def __str__(self):
        return f"role: {self.professional}" 

class MentorApplication(models.Model):
    user = models.ForeignKey(UserRoles, on_delete=models.CASCADE, related_name='apps')
    submission_date = models.DateTimeField(auto_now=True)
    employer = models.CharField(max_length=50)
    website = models.CharField(max_length=100)
    linkedin = models.CharField(max_length=100)
    a1 = models.CharField(max_length=1000) # Why do you want to be a mentor
    a2 = models.CharField(max_length=1000) # What are your interests and passion projects

    def __str__(self):
        return f"User: {self.user} SubDate: {self.submission_date}"