from django.forms import ModelForm
from django import forms
from .models import *


class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = "__all__"


class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = "__all__"


class CardForm(ModelForm):
    class Meta:
        model = Card
        fields = "__all__"


class QuizForm(ModelForm):
    class Meta:
        model = Quiz
        fields = "__all__"


class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = "__all__"

