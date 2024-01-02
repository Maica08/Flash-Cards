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
from django.urls import reverse_lazy
from .models import *
from .forms import *


@method_decorator(login_required, name='dispatch')
class HomePageView(ListView):
    model = Card
    context_object_name = "home"
    template_name = "home.html"
    paginate_by = 10
    
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
    paginate_by = 12
    
    def get_queryset(self):
        return Subject.objects.filter(user=self.request.user)


@method_decorator(login_required, name='dispatch')
class SubjectCreateView(CreateView):
    model = Subject
    form_class = SubjectForm
    template_name = "create-subject.html"
    success_url = reverse_lazy("subject-list")
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        

@method_decorator(login_required, name='dispatch')
class SubjectUpdateView(UpdateView):
    model = Subject
    form_class = SubjectForm
    template_name = "update-subject.html"
    success_url = reverse_lazy("subject-list")
    

@method_decorator(login_required, name='dispatch')
class SubjectDeleteView(DeleteView):
    model = Subject
    template_name = "del-subject.html"
    success_url = reverse_lazy("subject-list")
    

@method_decorator(login_required, name='dispatch')    
class TopicsInSubject(ListView):
    context_object_name = "topics"
    template_name = "topics-in-subject.html"
    paginate_by = 12
    
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
        
        topics = Topic.objects.filter(user=self.request.user)
        grouped_topics = {}
        for topic in topics:
            subject = topic.subject
            if subject not in grouped_topics:
                grouped_topics[subject] = []
            grouped_topics[subject].append(topic)

        context['grouped_topics'] = [{'grouper': subject, 'list': topics} for subject, topics in grouped_topics.items()]

        return context
    
    
@method_decorator(login_required, name='dispatch')
class TopicCreateView(CreateView):
    model = Topic
    form_class = TopicForm
    template_name = "create-topic.html"
    success_url = reverse_lazy("topic-list")
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        

@method_decorator(login_required, name='dispatch')
class TopicUpdateView(UpdateView):
    model = Topic
    form_class = TopicForm
    template_name = "update-topic.html"
    success_url = reverse_lazy("topic-list")
    

@method_decorator(login_required, name='dispatch')
class TopicDeleteView(DeleteView):
    model = Topic
    template_name = "del-topic.html"
    success_url = reverse_lazy("topic-list")
    

@method_decorator(login_required, name='dispatch')    
class CardsInTopics(ListView):
    context_object_name = "cards"
    template_name = "cards-in-topic.html"
    paginate_by = 4
    
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
class CardCreateView(CreateView):
    model = Card
    form_class = CardForm
    template_name = "create-card.html"
    success_url = reverse_lazy("cards-list")
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        

@method_decorator(login_required, name='dispatch')
class CardUpdateView(UpdateView):
    model = Card
    form_class = CardForm
    template_name = "update-card.html"
    success_url = reverse_lazy("cards-list")
    

@method_decorator(login_required, name='dispatch')
class CardDeleteView(DeleteView):
    model = Card
    template_name = "del-card.html"
    success_url = reverse_lazy("cards-list")
    

@method_decorator(login_required, name='dispatch')        
class QuizList(ListView):
    model = Quiz
    context_object_name = "quiz"
    template_name = "quiz.html"
    paginate_by = 12
    
    def get_queryset(self):
        return Quiz.objects.filter(user=self.request.user)
    

@method_decorator(login_required, name='dispatch')
class QuizCreateView(CreateView):
    model = Quiz
    form_class = QuizForm
    template_name = "create-quiz.html"
    success_url = reverse_lazy("quiz-list")
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        

@method_decorator(login_required, name='dispatch')
class QuizUpdateView(UpdateView):
    model = Quiz
    form_class = QuizForm
    template_name = "update-quiz.html"
    success_url = reverse_lazy("quiz-list")
    

@method_decorator(login_required, name='dispatch')
class QuizDeleteView(DeleteView):
    model = Quiz
    template_name = "del-quiz.html"
    success_url = reverse_lazy("quiz-list")
    

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
class QuestionList(ListView):
    model = Question
    context_object_name = "question"
    template_name = "questions.html"
    
    def get_queryset(self):
        return Question.objects.filter(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        questions = Question.objects.filter(user=self.request.user)
        grouped_questions = {}
        for question in questions:
            quiz = question.quiz
            if quiz not in grouped_questions:
                grouped_questions[quiz] = []   
            grouped_questions[quiz].append(question)

        context['grouped_questions'] = [{'grouper': quiz, 'list': questions} for quiz, questions in grouped_questions.items()]

        return context

@method_decorator(login_required, name='dispatch')
class QuestionCreateView(CreateView):
    model = Question
    form_class = QuestionForm
    template_name = "create-question.html"
    success_url = reverse_lazy("question-list")
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

        

@method_decorator(login_required, name='dispatch')
class QuestionUpdateView(UpdateView):
    model = Question
    form_class = QuestionForm
    template_name = "update-question.html"
    success_url = reverse_lazy("question-list")
    

@method_decorator(login_required, name='dispatch')
class QuestionDeleteView(DeleteView):
    model = Question
    template_name = "del-question.html"
    success_url = reverse_lazy("question-list")
    

@method_decorator(login_required, name='dispatch')
class ChoiceList(ListView):
    model = Choice
    context_object_name = "choice"
    template_name = "choices.html"
    
    def get_queryset(self):
        return Choice.objects.filter(user=self.request.user)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        choices = Choice.objects.filter(user=self.request.user)
        grouped_choices = {}
        
        for choice in choices:
            question = choice.question
            quiz = question.quiz
            
            if quiz not in grouped_choices:
                grouped_choices[quiz] = {}

            if question not in grouped_choices[quiz]:
                grouped_choices[quiz][question] = []

            grouped_choices[quiz][question].append(choice)

        context['grouped_choices'] = [{'quiz': quiz, 'questions': [{'question': question, 'choices': choices} for question, choices in choices.items()]} for quiz, choices in grouped_choices.items()]

        return context
    

@method_decorator(login_required, name='dispatch')
class ChoiceCreateView(CreateView):
    model = Choice
    form_class = ChoiceForm
    template_name = "create-choice.html"
    success_url = reverse_lazy("choice-list")
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)
        

@method_decorator(login_required, name='dispatch')
class ChoiceUpdateView(UpdateView):
    model = Choice
    form_class = ChoiceForm
    template_name = "update-choice.html"
    success_url = reverse_lazy("choice-list")
    

@method_decorator(login_required, name='dispatch')
class ChoiceDeleteView(DeleteView):
    model = Choice
    template_name = "del-choice.html"
    success_url = reverse_lazy("choice-list")
    

@method_decorator(login_required, name='dispatch')
class FlashQuiz(View):
    template_name = "flash-quiz.html"

    def get(self, request, *args, **kwargs):
        quiz_id = kwargs.get('quiz_id')
        quiz = get_object_or_404(Quiz, id=quiz_id)
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
