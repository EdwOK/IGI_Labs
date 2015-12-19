from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.db.models import Sum
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.views import generic

from .models import Question, Choice, Comment
from polls.forms import QuestionForm, ChoiceFormSet, QuestionChangeFormSet, CommentForm


class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now())


class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


class AboutView(generic.TemplateView):
    template_name = 'polls/about.html'


class ContactView(generic.TemplateView):
    template_name = 'polls/contact.html'


def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:10]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    votes = question.choice_set.aggregate(Sum('votes'))['votes__sum']
    form = CommentForm()
    return render(request, 'polls/results.html', {'question': question, 'votes': votes, 'form': form})


@login_required
def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = p.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': p,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(p.id,)))


def search(request):
    if request.GET and 'query' in request.GET:
        query = request.GET['query']
        questions = Question.objects.filter(question_text__contains=query)

        if questions.count() > 0:
            context = {'latest_question_list': questions}
        else:
            context = {'info_message': 'No matches found.'}

        return render(request, 'polls/index.html', context)
    else:
        return HttpResponseRedirect('/')


@login_required
def create(request):
    new_question = Question(author=request.user)
    if request.POST:
        form = QuestionForm(request.POST, instance=new_question)
        if form.is_valid():
            poll = form.save(commit=False)
            poll.author = request.user

            formset = ChoiceFormSet(request.POST, instance=poll)
            if formset.is_valid():
                poll.save()
                formset.save()
                return HttpResponseRedirect('/')
        else:
            formset = ChoiceFormSet(instance=new_question)
    else:
        form = QuestionForm(instance=new_question)
        formset = ChoiceFormSet(instance=new_question)

    return render(request, 'polls/create.html', {'form': form, 'formset': formset})


@login_required
def edit(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.user != question.author:
        return HttpResponseRedirect('/')

    if request.POST:
        formset = QuestionChangeFormSet(request.POST, instance=question)
        if formset.is_valid():
            formset.save()
            return HttpResponseRedirect(reverse('polls:detail', args=(question.id,)))
    else:
        formset = QuestionChangeFormSet(instance=question)

    return render(request, "polls/edit.html", {'formset': formset, 'question': question})


@login_required
def comments(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.question = question
            comment.save()
    else:
        form = CommentForm()

    return redirect(reverse('polls:results', args=(question.id,)))


@login_required
def delete(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    question.delete()
    return HttpResponseRedirect('/')
