from django.urls import path

from sendvotes import views

urlpatterns = [
    path("<int:question_id>/vote", views.sendvote, name="vote"),
    path("<int:question_id>/<int:option_id>/register",
         views.registervote, name="register"),
]
