from django.urls import path
from recipes.views import contato, home, sobre
#from recipes.views import home

urlpatterns = [
    path('', home),  # Home
    path('sobre/', sobre),  # /sobre/
    path('contato/', contato),  # /contato/
]