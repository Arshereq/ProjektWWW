from django.urls import path
from . import views

urlpatterns = [
    path('', views.druzyna_list),
    path('<int:pk>/', views.druzyna_detail),
]