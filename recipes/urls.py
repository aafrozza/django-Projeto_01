from django.urls import path
#from recipes.views import contato, home, sobre
from . import views

urlpatterns = [
    path('', views.home),  # Home
    #path('recipes/', views.home),  # Home
    path('recipes/<int:id>/', views.recipe),  # /recipes/3/
    #path('contato/', contato),  # /contato/
]