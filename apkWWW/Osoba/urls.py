from django.urls import path, include
from . import views

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', views.osoba_list),
    path('/<int:pk>/', views.osoba_detail),
    path('update/<int:pk>/',views.Osoba_update_delete_add),
    path('delete/<int:pk>/', views.Osoba_update_delete_add),
]