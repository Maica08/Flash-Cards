from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),
    path('subjects/', views.SubjectList.as_view(), name='subject-list'),
    path('subjects/<int:subject_id>/topics/', views.TopicsInSubject.as_view(), name='topics_in_subject'),
    path('topics/', views.TopicList.as_view(), name='topic-list'),
    path('subjects/<int:subject_id>/topics/<int:topic_id>/cards/', views.CardsInTopics.as_view(), name='cards_in_topic'),
    path('cards/', views.CardList.as_view(), name="cards-list"),
]

