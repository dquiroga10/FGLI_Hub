from django.contrib import admin
from .models import Question, Answer, Blog_Post, UserRoles, MentorApplication

# Register your models here.
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Blog_Post)
admin.site.register(UserRoles)
admin.site.register(MentorApplication)