from django.contrib import admin

from core.models import Question, Vote, QuestionOptions
# Register your models here.

admin.site.register(Question)
admin.site.register(Vote)
admin.site.register(QuestionOptions)
