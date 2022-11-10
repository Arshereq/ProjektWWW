from django.urls import path
from . import views

urlpatterns = [
    path('', views.DruzynaList.as_view()),
    #path('<int:pk>/', views.druzyna_detail),
]