from django.contrib import admin
from .models import Question, Answer, Blog_Post, UserRoles

# Register your models here.
admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Blog_Post)
admin.site.register(UserRoles)