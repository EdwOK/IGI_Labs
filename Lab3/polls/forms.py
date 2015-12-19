from django.forms import ModelForm, inlineformset_factory, modelform_factory

from .models import Question, Choice, Comment


class QuestionForm(ModelForm):
    class Meta:
        model = Question
        exclude = ['author', 'pub_date']


class ChoiceForm(ModelForm):
    class Meta:
        model = Choice
        exclude = ['votes']


class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['content']

ChoiceFormSet = inlineformset_factory(Question, Choice, form=ChoiceForm, extra=3, can_delete=False)
QuestionChangeFormSet = inlineformset_factory(Question, Choice, form=QuestionForm, extra=0, can_delete=False)