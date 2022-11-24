from django.urls import path, include
from . import views

urlpatterns = [
    path('api-auth/', include('rest_framework.urls')),
    path('', views.druzyna_list),
    path('/<int:pk>/', views.druzyna_detail),
    path('update/<int:pk>/', views.Druzyna_update_delete_add),
    path('delete/<int:pk>/', views.Druzyna_update_delete_add),
]