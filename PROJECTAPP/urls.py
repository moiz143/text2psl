from django.urls import path
from . import views

urlpatterns = [

    path('', views.home, name='home-page'),
    path('demo', views.demo, name='demo-page'),
    path('getenglish', views.getEnglish, name='getEnglish'),
    path('geturdu', views.getUrdu, name='getUrdu'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('about_team', views.about_team, name='about_team'),
    path('about_credits', views.about_credits, name='about_credits'),

    path('hamnosys', views.hamnosys, name='hamnosys')
]
