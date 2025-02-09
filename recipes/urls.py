from django.urls import path
#from recipes.views import contato, home, sobre
from . import views

app_name = 'recipes'


urlpatterns = [
    #path('', views.home),  # Home
    path('', views.home, name="home"),
    path('recipes/category/<int:category_id>/',
         views.category, name="category"),
    path('recipes/<int:id>/', views.recipe, name="recipe"),

]