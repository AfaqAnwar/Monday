from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='monday'),
    path('chat', views.chat, name='chat')
]

