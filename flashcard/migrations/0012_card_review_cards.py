# Generated by Django 5.0 on 2023-12-28 13:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flashcard', '0011_review'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='review_cards',
            field=models.ManyToManyField(blank=True, to='flashcard.review'),
        ),
    ]
