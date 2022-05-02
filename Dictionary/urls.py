from django.urls import path
from Dictionary import views

urlpatterns = [ 
    path('', views.home, name='home'),
    path('word', views.word, name='word'),
]