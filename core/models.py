from django.db import models

# Create your models here.


class Question(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()


class QuestionOption(models.Model):
    option = models.CharField(max_length=100)
    question = models.ForeignKey(
        Question, related_name='options', on_delete=models.CASCADE)


class Vote(models.Model):
    student = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now=True)
    question = models.ForeignKey(
        Question, related_name='votes', on_delete=models.CASCADE)
    content = models.ForeignKey(
        QuestionOption, on_delete=models.CASCADE, null=True)
