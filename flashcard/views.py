from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views import View
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.views.generic.list import ListView
from django.shortcuts import get_object_or_404
from django.contrib import messages
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .models import *
from .forms import *


@method_decorator(login_required, name='dispatch')
class HomePageView(ListView):
    model = Card
    context_object_name = "home"
    template_name = "home.html"
    
    def get_queryset(self):
        return Card.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


@method_decorator(login_required, name='dispatch')
class SubjectList(ListView):
    model = Subject
    context_object_name = "subject"
    template_name = "subjects.html"
    
    def get_queryset(self):
        return Subject.objects.filter(user=self.request.user)


@method_decorator(login_required, name='dispatch')    
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
        return Topic.objects.filter(user=self.request.user, subject=subject)
    

@method_decorator(login_required, name='dispatch')    
class TopicList(ListView):
    model = Topic
    context_object_name = "topic"
    template_name = "topics.html"
    
    def get_queryset(self):
        return Topic.objects.filter(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        # Retrieve all topics and organize them by subject
        topics = Topic.objects.filter(user=self.request.user)
        grouped_topics = {}
        for topic in topics:
            subject = topic.subject
            if subject not in grouped_topics:
                grouped_topics[subject] = []
            grouped_topics[subject].append(topic)

        # Convert the dictionary to a list for regrouping in the template
        context['grouped_topics'] = [{'grouper': subject, 'list': topics} for subject, topics in grouped_topics.items()]

        return context
    
        

@method_decorator(login_required, name='dispatch')    
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
        return Card.objects.filter(user=self.request.user, topic=topic)
    

@method_decorator(login_required, name='dispatch')    
class CardList(ListView):
    model = Card
    context_object_name = "card"
    template_name = "cards.html"
    
    def get_queryset(self):
        return Card.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        cards = Card.objects.filter(user=self.request.user)
        grouped_cards = {}
        for card in cards:
            topic = card.topic
            if topic not in grouped_cards:
                grouped_cards[topic] = []   
            grouped_cards[topic].append(card)

        context['grouped_cards'] = [{'grouper': topic, 'list': cards} for topic, cards in grouped_cards.items()]

        return context
    
        

@method_decorator(login_required, name='dispatch')        
class QuizList(ListView):
    model = Quiz
    context_object_name = "quiz"
    template_name = "quiz.html"
    
    def get_queryset(self):
        return Quiz.objects.filter(user=self.request.user)

@method_decorator(login_required, name='dispatch')
class CardsInQuiz(ListView):
    context_object_name = "flashcards"
    template_name = "cards-in-quiz.html"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        quiz_id = self.kwargs.get('quiz_id')
        quiz = get_object_or_404(Quiz, id=quiz_id)
        context['quiz'] = quiz
        return context
    
    def get_queryset(self):
        quiz_id = self.kwargs['quiz_id']
        quiz = get_object_or_404(Quiz, id=quiz_id)
        return Card.objects.filter(user=self.request.user, flash_quiz=quiz)


@method_decorator(login_required, name='dispatch')
class FlashQuiz(View):
    template_name = "flash-quiz.html"

    def get(self, request, *args, **kwargs):
        quiz_id = kwargs.get('quiz_id')
        quiz = get_object_or_404(Quiz, id=quiz_id)
        # cards = Card.objects.filter(flash_quiz=quiz)

        # # Debugging: Print cards to the console
        # print("Cards:", cards)

        questions = Question.objects.filter(user=self.request.user, quiz=quiz)
        
        print("Questions:", questions)

        context = {
            'quiz': quiz,
            'questions': questions,
        }

        return render(request, self.template_name, context)


class SubmitQuiz(View):
    template_name = "quiz-result.html"

    def post(self, request, *args, **kwargs):
        quiz_id = kwargs.get('quiz_id')
        quiz = get_object_or_404(Quiz, id=quiz_id)
        questions = Question.objects.filter(user=self.request.user, card__in=quiz.card_set.all())

        # Retrieve selected choices from the form data
        score = 0
        selected_choices = {}
        for question in questions:
            selected_choice_id = int(request.POST.get(f'question_{question.id}', 0))
            selected_choices[question.id] = selected_choice_id

            print(f"Selected choices: {selected_choices}")
            print(f"Question: {question}")
            
            for choice in question.choice_set.all():
                selected_choice = selected_choices.get(question.id, None)
                if selected_choice == choice.id and choice.is_correct:
                    score += 1
                        
        
        print(f"Score: {score}")
                            
        context = {
            'quiz': quiz,
            'questions': questions,
            'selected_choices': selected_choices,
            'score': score,
        }

        return render(request, self.template_name, context)
