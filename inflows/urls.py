from django.urls import path
from . import views


urlpatterns = [
    path('inflows/list', views.InflowListView.as_view(), name='inflows-list'),
    path('inflows/create', views.InflowCreateView.as_view(), name='inflows-create'),
    path('inflows/<int:pk>/detail/', views.InflowDetailView.as_view(), name='inflows-detail'),

    path('inflows/api/list', views.InflowCreateListApiView.as_view(), name='inflow-create-list-api-view'),
    path('inflows/api/<int:pk>', views.InflowRetrieveAPIView.as_view(), name='inflow-detail-api-view'),
]