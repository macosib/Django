from django.urls import path
from calculator.views import recipes_view

urlpatterns = [
    path('<str:food_name>/', recipes_view, name='recipes_name')
]
