from django.urls import path
from . import views


urlpatterns = [
    path('suppliers/list', views.SupplierListView.as_view(), name='supplier-list'),
    path('suppliers/create', views.SupplierCreateView.as_view(), name='supplier-create'),
    path('suppliers/<int:pk>/detail/', views.SupplierDetailView.as_view(), name='supplier-detail'),
    path('suppliers/<int:pk>/update/', views.SupplierUpdateView.as_view(), name='supplier-update'),
    path('suppliers/<int:pk>/delete/', views.SupplierDeleteView.as_view(), name='supplier-delete'),

    path('api/v1/suppliers/', views.SupplierCreateListAPIView.as_view(), name='supplier-create-list-api-view'),
    path('api/v1/suppliers/<int:pk>/', views.SuppliersRetrieveUpdateDestroyAPIView.as_view(), name='supplier-detail-api-view'),
]