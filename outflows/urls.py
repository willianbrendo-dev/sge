from django.urls import path
from . import views


urlpatterns = [
    path('outflows/list', views.OutflowListView.as_view(), name='outflows-list'),
    path('outflows/create', views.OutflowCreateView.as_view(), name='outflows-create'),
    path('outflows/<int:pk>/detail/', views.OutflowDetailView.as_view(), name='outflows-detail'),

    path('api/outflows/', views.OutflowCreateListAPIView.as_view(), name='outflow-create-list-api-view'),
    path('api/outflows/<int:pk>/', views.OutflowRetrieveAPIView.as_view(), name='outflow-detail-api-view'),
]