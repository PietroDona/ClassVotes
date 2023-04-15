from django.shortcuts import render
from core.models import Question

# Create your views here.


def displayquestion(request, question_id):
    question = Question.objects.get(id=question_id)
    votes = question.votes.all()
    context = {"question": question, "votes": votes}
    return render(request, "teacher/displayquestion.html", context)
