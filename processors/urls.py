from django.urls import path
from . import views

urlpatterns = [
    path('', views.comparison, name='comparison'),
    path('api/search/', views.search_processors, name='search_processors'),
    path('api/processor/<int:pk>/', views.processor_detail, name='processor_detail'),
]
