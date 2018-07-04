from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.pals_list, name='pals_list'),
]