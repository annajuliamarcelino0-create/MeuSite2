from django.urls import path
from MeuApp import views

#registrar as ursl do app

#qual url corresponde a cada view 
urlpatterns = [
    path('', views.home, name='home'),
    path('contato/', views.contato, name='contato'),
    path('produto/', views.exibir_produtos, name='produtos')
]
