from django.urls import path
#from recipes.views import contato, home, sobre
from . import views

app_name = 'recipes'


urlpatterns = [
    #path('', views.home),  # Home
    path('', views.home, name="home"),
 
    #path('recipes/', views.home),  # Home
    path('recipes/<int:id>/', views.recipe),  # /recipes/3/
    #path('contato/', contato),  # /contato/
    path('recipes/<int:id>/', views.recipe, name="recipe"),

]