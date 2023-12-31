from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('subjects/', views.SubjectList.as_view(), name='subject-list'),
    path('subjects/<int:subject_id>/topics/', views.TopicsInSubject.as_view(), name='topics_in_subject'),
    path('topics/', views.TopicList.as_view(), name='topic-list'),
    path('subjects/<int:subject_id>/topics/<int:topic_id>/cards/', views.CardsInTopics.as_view(), name='cards_in_topic'),
    path('cards/', views.CardList.as_view(), name="cards-list"),
    path('quiz/', views.QuizList.as_view(), name="quiz-list"),
    path('quiz/<int:quiz_id>/flashcards/', views.CardsInQuiz.as_view(), name="flashcards"),
    path('quiz/<int:quiz_id>/flash_quiz/', views.FlashQuiz.as_view(), name="flash_quiz"), 
    path('<int:quiz_id>/submit_quiz/', views.SubmitQuiz.as_view(), name='submit_quiz'),
]

