from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.pals_list, name='pals_list'),
    url(r'^pal/(?P<name>\w+)/$', views.pal_profile, name='pal_profile'),
]