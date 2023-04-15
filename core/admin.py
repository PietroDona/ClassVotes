from django.contrib import admin

from core.models import Question, Vote, QuestionOption
# Register your models here.

admin.site.register(Question)
admin.site.register(Vote)
admin.site.register(QuestionOption)
