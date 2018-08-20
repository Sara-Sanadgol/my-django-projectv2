from django.urls import path
from perfume import views

urlpatterns = [
    path('', views.scent_list, name='scent_list'),
]