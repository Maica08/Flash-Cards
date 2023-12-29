from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404
from .models import *
from .forms import *


class HomePageView(ListView):
    model = Card
    context_object_name = "home"
    template_name = "home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

class SubjectList(ListView):
    model = Subject
    context_object_name = "subject"
    template_name = "subjects.html"
    
class TopicsInSubject(ListView):
    context_object_name = "topics"
    template_name = "topics-in-subject.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        subject_id = self.kwargs.get('subject_id')
        subject = get_object_or_404(Subject, id=subject_id)
        context['subject'] = subject
        return context
    
    def get_queryset(self):
        subject_id = self.kwargs['subject_id']
        subject = get_object_or_404(Subject, id=subject_id)
        return Topic.objects.filter(subject=subject)
    
    
class TopicList(ListView):
    model = Topic
    context_object_name = "topic"
    template_name = "topics.html"
        
    
class CardsInTopics(ListView):
    context_object_name = "cards"
    template_name = "cards-in-topic.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        topic_id = self.kwargs.get('topic_id')
        topic = get_object_or_404(Topic, id=topic_id)
        context['topic'] = topic
        return context
    
    def get_queryset(self):
        topic_id = self.kwargs['topic_id']
        topic = get_object_or_404(Topic, id=topic_id)
        return Card.objects.filter(topic=topic)
    
    
class CardList(ListView):
    model = Card
    context_object_name = "card"
    template_name = "cards.html"

    

