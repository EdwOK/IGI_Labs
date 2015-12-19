from django.contrib import admin
from polls.models import Choice, Question, Comment


class ChoiceInline(admin.StackedInline):
    model = Choice
    readonly_fields = ('votes',)
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['author', 'question_text']}),
        ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]
    list_display = ('author', 'question_text', 'pub_date', 'was_published_recently')
    list_filter = ['pub_date']
    search_fields = ['question_text']


class CommentAdmin(admin.ModelAdmin):
    list_display = ('content', 'author', 'create_date')
    list_filter = ['create_date']
    search_fields = ['content']

admin.site.register(Choice)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Question, QuestionAdmin)