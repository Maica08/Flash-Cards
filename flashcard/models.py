from django.db import models

# Create your models here.

class BaseModel(models.Model):
    created_at = models.DateTimeField(auto_now=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        abstract = True


class Subject(BaseModel):
    subject = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.subject


class Topic(BaseModel):
    topic = models.CharField(max_length=100, null=True, blank=True)
    subject = models.ForeignKey(Subject, null=True, blank=True, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.topic


class Quiz(BaseModel):
    name = models.CharField(max_length=255, null=True, blank=True)
    topic = models.ForeignKey(Topic, null=True, blank=True, on_delete=models.CASCADE)
    
    
    class Meta:
        verbose_name_plural = "Quizzes"
    
    def __str__(self):
        return self.name


class Review(BaseModel):
    topic = models.ForeignKey(Topic, null=True, blank=True, on_delete=models.CASCADE)

    
    class Meta:
        verbose_name = "Review"
        
    def __str__(self):
        return self.topic.topic
    
class Card(BaseModel):
    front = models.CharField(max_length=255)
    back = models.TextField()
    topic = models.ForeignKey(Topic, null=True, blank=True, on_delete=models.CASCADE)
    flash_quiz = models.ManyToManyField(Quiz, blank=True)   
    review_cards = models.ManyToManyField(Review, blank=True) 
    
    def __str__(self):
        return self.front

