from django.urls import path
from . import views

urlpatterns = [
    path('', views.OsobaList.as_view()),
    #path('<int:pk>/', views.osoba_detail),
]