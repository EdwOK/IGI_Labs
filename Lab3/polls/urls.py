from django.conf.urls import url

from . import views
from django.contrib.auth.decorators import login_required

urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'search$', views.search, name='search'),
    url(r'^create/$', views.create, name='create'),
    url(r'^about/$', views.AboutView.as_view(), name='about'),
    url(r'^contact/$', views.ContactView.as_view(), name='contact'),
    url(r'^(?P<pk>[0-9]+)/$', login_required(views.DetailView.as_view()), name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^(?P<question_id>[0-9]+)/edit/$', views.edit, name='edit'),
    url(r'^(?P<question_id>[0-9]+)/delete/$', views.delete, name='delete'),
    url(r'^(?P<question_id>[0-9]+)/comments/$', views.comments, name='comments'),
]
