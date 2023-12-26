from django.contrib import admin
from .models import *


# @admin.register(Card)
class CardInline(admin.TabularInline):
    model = Card
    list_display = ['front', 'back', 'created_at', 'updated_at']
    extra = 1
    

# @admin.register(Topic)
class TopicInline(admin.TabularInline):
    model = Topic
    list_display = ['topic', 'flash_cards', 'created_at', 'updated_at']
    extra = 1
    inlines = [
        CardInline,
        ]

# @admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    model = Subject
    list_display = ['subject', 'topics', 'created_at', 'updated_at']   
    inlines = [
        TopicInline,
    ]


admin.site.register(Subject)
admin.site.register(Topic)
admin.site.register(Card)
