from django.urls import path

from teacher import views

urlpatterns = [
    # path("", views.index, name=""),
]


urlpatterns = [
    path("<int:question_id>/display",
         views.displayquestion, name="displayquestion"),
    path("<int:question_id>/data",
         views.dataquestion, name="dataquestion"),
]
