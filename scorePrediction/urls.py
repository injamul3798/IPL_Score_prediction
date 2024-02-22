from django.urls import path
from prediction import views

urlpatterns = [
    path('', views.home, name='home'),
    path('result/', views.result, name='result'),
]
