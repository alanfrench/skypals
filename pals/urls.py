from django.conf.urls import url
from django.urls import path
from . import views
# with regex (gross)
# urlpatterns = [
#     url(r'^$', views.pals_list, name='pals_list'),
#     url(r'^pal/(?P<name>\w+)/$', views.pal_profile, name='pal_profile'),
# ]

urlpatterns = [
    path('', views.indexView, name='index'),
    path('quiz/', views.quizView, name='quizView'),
    path('quiz/<str:name>/', views.questionView, name='questionView'),
    path('pals/', views.palsList, name='palsList'),
    path('pals/pal/<str:name>', views.palProfile, name='palProfile'),
]