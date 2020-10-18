from django.contrib import admin
from django.urls import path
from problems.views import indexPage, homePage, QuestionList, autocomplete

app_name = 'problems'

urlpatterns = [

    path ('',homePage.as_view(), name = 'home'),
    path ('base',indexPage.as_view(), name = 'base'),
    path('questions/',QuestionList, name = 'question'),
    path('autocomplete/', autocomplete, name='autocomplete')
]
