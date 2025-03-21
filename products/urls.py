from django.urls import path
from . import views


urlpatterns = [
    path('products/list', views.ProductListView.as_view(), name='products-list'),
    path('products/create', views.ProductCreateView.as_view(), name='products-create'),
    path('products/<int:pk>/detail/', views.ProductDetailView.as_view(), name='products-detail'),
    path('products/<int:pk>/update/', views.ProductUpdateView.as_view(), name='products-update'),
    path('products/<int:pk>/delete/', views.ProductDeleteView.as_view(), name='products-delete'),

    path('api/v1/products/', views.ProductCreateListApiView.as_view(), name='product-create-list-api-view'),
    path('api/v1/products/<int:pk>/', views.ProductRetrieveUpdateDestroyApiView.as_view(), name='product-detail-api-view'),
]