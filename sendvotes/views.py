from django.shortcuts import render

# Create your views here.
from core.models import Question, QuestionOptions, Vote


def sendvote(request, question_id):
    question = Question.objects.get(id=question_id)
    options = question.options.all()
    context = {"question": question, "options": options}

    print(context)

    return render(request, "sendvotes/vote.html", context)
