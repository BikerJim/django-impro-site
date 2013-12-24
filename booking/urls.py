from django.conf.urls import patterns, url
from django.views.generic import TemplateView, DetailView, CreateView

from . import views
from .views import ReserveTicket, ReserveThanks

urlpatterns = patterns("",
    url(r"^(?P<pk>\d+)/$", ReserveTicket.as_view(), name="reserve_ticket"),
    url(r"^thankyou/$", ReserveThanks.as_view(), name="reserve_thanks"),
)
