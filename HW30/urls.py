from django.urls import path
from . import views

urlpatterns = [
    path('person_list/', views.person_list, name='person_list'),
]
