from django.contrib import admin
from .models import *


@admin.register(Card)
class Card(admin.ModelAdmin):
    model = Card
    list_display = ('topic', 'front', 'back', 'created_at', 'updated_at')
    

@admin.register(Topic)
class Topic(admin.ModelAdmin):
    model = Topic
    list_display = ('topic', 'subject', 'created_at', 'updated_at')
    extra = 1
    

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    model = Subject
    list_display = ('subject', 'created_at', 'updated_at')   
    

@admin.register(Quiz)
class QuizAdmin(admin.ModelAdmin):
    model = Quiz
    list_display = ('name', 'topic', 'created_at', 'updated_at')   

    
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    model = Question
    list_display = ('quiz', 'card', 'created_at', 'updated_at')
    
    
@admin.register(Choice)
class ChoiceAdmin(admin.ModelAdmin):
    model = Choice
    list_display = ('question', 'card', 'is_correct', 'created_at', 'updated_at')
