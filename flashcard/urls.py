from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    # Subjects
    path('subjects/', views.SubjectList.as_view(), name='subject-list'),
    path('subjects/<int:subject_id>/topics/', views.TopicsInSubject.as_view(), name='topics_in_subject'),
    path('subjects/add', views.SubjectCreateView.as_view(), name='subject_add'),
    path('subjects/<pk>', views.SubjectUpdateView.as_view(), name='subject_update'),
    path('subjects/<pk>/delete', views.SubjectDeleteView.as_view(), name='subject_delete'),

    # Topics
    path('topics/', views.TopicList.as_view(), name='topic-list'),
    path('subjects/<int:subject_id>/topics/<int:topic_id>/cards/', views.CardsInTopics.as_view(), name='cards_in_topic'),
    path('topics/add', views.TopicCreateView.as_view(), name='topic_add'),
    path('topics/<pk>', views.TopicUpdateView.as_view(), name='topic_update'),
    path('topics/<pk>/delete', views.TopicDeleteView.as_view(), name='topic_delete'),
    
    # Cards
    path('cards/', views.CardList.as_view(), name="cards-list"),
    path('cards/add', views.CardCreateView.as_view(), name='card_add'),
    path('cards/<pk>', views.CardUpdateView.as_view(), name='card_update'),
    path('cards/<pk>/delete', views.CardDeleteView.as_view(), name='card_delete'),
    
    # Quiz
    path('quiz/', views.QuizList.as_view(), name="quiz-list"),
    path('quiz/<int:quiz_id>/flashcards/', views.CardsInQuiz.as_view(), name="flashcards"),
    path('quiz/add', views.QuizCreateView.as_view(), name='quiz_add'),
    path('quiz/<pk>', views.QuizUpdateView.as_view(), name='quiz_update'),
    path('quiz/<pk>/delete', views.QuizDeleteView.as_view(), name='quiz_delete'),
    
    # Questions
    path('question/', views.QuestionList.as_view(), name="question-list"), 
    path('question/add', views.QuestionCreateView.as_view(), name='question_add'),
    path('question/<pk>', views.QuestionUpdateView.as_view(), name='question_update'),
    path('question/<pk>/delete', views.QuestionDeleteView.as_view(), name='question_delete'),
    
    # Choices
    path('choices/', views.ChoiceList.as_view(), name="choice-list"), 
    path('choices/add', views.ChoiceCreateView.as_view(), name='choice_add'),
    path('choices/<pk>', views.ChoiceUpdateView.as_view(), name='choice_update'),
    path('choices/<pk>/delete', views.ChoiceDeleteView.as_view(), name='choice_delete'),
    
    # Flash Quiz
    path('quiz/<int:quiz_id>/flash_quiz/', views.FlashQuiz.as_view(), name="flash_quiz"), 
    path('<int:quiz_id>/submit_quiz/', views.SubmitQuiz.as_view(), name='submit_quiz'),
]

