from .views import comment_list
from django.urls import path

urlpatterns = [
    path('',comment_list)
]