from django.shortcuts import render
from django.http import JsonResponse
from django.db.models import Count
from core.models import Question

# Create your views here.


def displayquestion(request, question_id):
    question = Question.objects.get(id=question_id)
    context = {"question": question}
    return render(request, "teacher/displayquestion.html", context)


def dataquestion(request, question_id):
    question = Question.objects.get(id=question_id)
    options = question.options.all()
    votes = question.votes.all()

    test = {o.option: votes.filter(content=o).aggregate(
        Count("id")).get("id__count") for o in options}

    return JsonResponse({"data": test})
