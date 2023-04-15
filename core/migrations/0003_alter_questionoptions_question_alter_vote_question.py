# Generated by Django 4.2 on 2023-04-15 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_rename_title_questionoptions_option"),
    ]

    operations = [
        migrations.AlterField(
            model_name="questionoptions",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="options",
                to="core.question",
            ),
        ),
        migrations.AlterField(
            model_name="vote",
            name="question",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="votes",
                to="core.question",
            ),
        ),
    ]