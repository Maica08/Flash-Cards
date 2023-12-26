from django.contrib import admin
from .models import *


@admin.register(Card)
class Card(admin.ModelAdmin):
    model = Card
    list_display = ('front', 'back', 'created_at', 'updated_at')
    

@admin.register(Topic)
class Topic(admin.ModelAdmin):
    model = Topic
    list_display = ('topic', 'subject', 'created_at', 'updated_at')
    extra = 1
    

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    model = Subject
    list_display = ('subject', 'created_at', 'updated_at')   
    