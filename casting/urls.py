from django.conf.urls import patterns, url
from django.views.generic import TemplateView, DetailView, CreateView

from . import views
from .views import CastShow, CastShowDone

urlpatterns = patterns("",
    url(r"^(?P<pk>\d+)/$", CastShow.as_view(), name="cast_show"),
    url(r"^done/$", CastShowDone.as_view(), name="cast_show_done"),
)
