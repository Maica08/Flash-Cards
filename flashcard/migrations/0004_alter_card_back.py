# Generated by Django 5.0 on 2023-12-27 17:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard', '0003_remove_subject_topics_remove_topic_flash_cards_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='back',
            field=models.TextField(),
        ),
    ]
