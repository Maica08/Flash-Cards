# Generated by Django 5.0 on 2023-12-27 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard', '0005_quiz_quizflashcard_quiz_flashcards'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quiz',
            options={'verbose_name_plural': 'Quizzes'},
        ),
    ]