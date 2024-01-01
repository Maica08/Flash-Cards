from django.forms import ModelForm
from django import forms
from .models import *


class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = ["subject"]        
        
    def save(self, commit=True, user=None):
        instance = super().save(commit=False)
        if user:
            instance.user = user
        if commit:
            instance.save()
        return instance


class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = ["topic", "subject"]        
        
    def save(self, commit=True, user=None):
        instance = super().save(commit=False)
        if user:
            instance.user = user
        if commit:
            instance.save()
        return instance


class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = ["front", "back", "topic", "flash_quiz"]
        
    def save(self, commit=True, user=None):
        instance = super().save(commit=False)
        if user:
            instance.user = user
        if commit:
            instance.save()
        return instance


class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        fields = ["name", "topic"]
    
    def save(self, commit=True, user=None):
        instance = super().save(commit=False)
        if user:
            instance.user = user
        if commit:
            instance.save()
        return instance


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        fields = ["quiz", "card"]    
        
    
    def save(self, commit=True, user=None):
        instance = super().save(commit=False)
        if user:
            instance.user = user
        if commit:
            instance.save()
        return instance


class ChoiceForm(ModelForm):
    class Meta:
        model = Choice
        fields = ["question", "card", "is_correct"] 
        
    
    def save(self, commit=True, user=None):
        instance = super().save(commit=False)
        if user:
            instance.user = user
        if commit:
            instance.save()
        return instance

