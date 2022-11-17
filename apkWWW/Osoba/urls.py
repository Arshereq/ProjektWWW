from django.urls import path, include
from . import views

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', views.osoba_list),
    path('<int:pk>/', views.osoba_detail),
    path('delete/<int:pk>/', views.osoba_delete),
    path('api-auth/', include('rest_framework.urls')),
]