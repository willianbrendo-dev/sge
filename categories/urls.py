from django.urls import path
from . import views



urlpatterns = [
    path('categories/list', views.CategoryListView.as_view(), name='categories-list'),
    path('category/create', views.CategoryCreateView.as_view(), name='category-create'),
    path('category/<int:pk>/detail/', views.CategoryDetailView.as_view(), name='category-detail'),
    path('category/<int:pk>/update/', views.CategoryUpdateView.as_view(), name='category-update'),
    path('category/<int:pk>/delete/', views.CategoryDeleteView.as_view(), name='category-delete'),

    path('api/v1/categories/', views.CategoryCreateListAPIView.as_view(), name='category-create-list-api-view'),
    path('api/v1/categories/<int:pk>/', views.CategoryRetrieveUpdateDestroyAPIView.as_view(), name='category-retrieve-update-destroy-api-view'),
]