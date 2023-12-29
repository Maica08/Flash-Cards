from django.shortcuts import get_object_or_404
from .models import *


def get_quiz_questions(quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = Card.objects.filter(flash_quiz=quiz)
    return questions

def get_review_questions(review_id):
    review = get_object_or_404(Review, id=review_id)
    questions = review.review_cards.all()
    return questions

