# Generated by Django 4.2 on 2023-04-15 14:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_alter_questionoptions_question_alter_vote_question"),
    ]

    operations = [
        migrations.RenameModel(
            old_name="QuestionOptions",
            new_name="QuestionOption",
        ),
    ]