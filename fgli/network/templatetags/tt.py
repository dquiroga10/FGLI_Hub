from django import template
from ..models import Question, Answer, UserRoles
from django.contrib.auth.models import User 

register = template.Library()

@register.filter(name='usercount')
def usercount(req):
    ct = User.objects.filter()
    return ct.count()

@register.filter(name='questioncount')
def questioncount(req):
    ct = Question.objects.filter()
    return ct.count()

@register.filter(name='answercount')
def answercount(req):
    ct = Answer.objects.filter()
    return ct.count()

@register.filter(name='professionals')
def proessional(req):
    ct = UserRoles.objects.filter(professional=True)
    return ct

