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
        
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(TopicForm, self).__init__(*args, **kwargs)

        if user:
            self.fields['subject'].queryset = Subject.objects.filter(user=user)
            
        
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
    
    flash_quiz = forms.ModelMultipleChoiceField(queryset=Quiz.objects.all(),
                                           widget=forms.CheckboxSelectMultiple)
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(CardForm, self).__init__(*args, **kwargs)

        if user:
            self.fields['flash_quiz'].queryset = Quiz.objects.filter(user=user)
            self.fields['topic'].queryset = Topic.objects.filter(user=user)
        
    def save(self, commit=True, user=None):
        instance = super().save(commit=False)
        if user:
            instance.user = user
        if commit:
            instance.save()
            self.save_m2m()
        return instance


class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        fields = ["name", "topic"]
        
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(QuizForm, self).__init__(*args, **kwargs)

        if user:
            self.fields['topic'].queryset = Topic.objects.filter(user=user)
    
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
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(QuestionForm, self).__init__(*args, **kwargs)

        if user:
            self.fields['quiz'].queryset = Quiz.objects.filter(user=user)
            self.fields['card'].queryset = Card.objects.filter(user=user)
        
    
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
        
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(ChoiceForm, self).__init__(*args, **kwargs)

        if user:
            self.fields['question'].queryset = Question.objects.filter(user=user)
            self.fields['card'].queryset = Card.objects.filter(user=user)
        
    
    def save(self, commit=True, user=None):
        instance = super().save(commit=False)
        if user:
            instance.user = user
        if commit:
            instance.save()
        return instance

