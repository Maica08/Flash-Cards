# Generated by Django 5.0 on 2023-12-28 06:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard', '0009_remove_quiz_flashcards_alter_quiz_options_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='quiz',
            options={'verbose_name_plural': 'Quizzes'},
        ),
    ]
