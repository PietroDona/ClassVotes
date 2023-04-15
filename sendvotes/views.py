from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from core.models import Question, QuestionOption, Vote


def sendvote(request, question_id):
    question = Question.objects.get(id=question_id)
    options = question.options.all()
    context = {"question": question, "options": options}
    return render(request, "sendvotes/vote.html", context)


def registervote(request, question_id, option_id):
    user_session_key = request.session.session_key
    question = Question.objects.get(id=question_id)
    vote, _ = Vote.objects.get_or_create(
        student=user_session_key, question=question)
    selected_option = QuestionOption.objects.get(id=option_id)
    vote.content = selected_option
    vote.save()
    return JsonResponse({'vote': vote.content.option})
