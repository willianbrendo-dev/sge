from django.shortcuts import render
from app.metrics import get_sales_metrics
from django.views.generic import ListView, CreateView, DetailView
from .models import Outflow
from .forms import OutflowForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from rest_framework import generics
from .serializers import OutflowSerializer


class OutflowListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):

    model = Outflow
    template_name = 'outflow_list.html'
    context_object_name = 'outflows'
    paginate_by = 10
    permission_required = 'outflows.view_outflow'
    


    def get_queryset(self):
        queryset = super().get_queryset()
        product = self.request.GET.get('product')
        if product:
            queryset = queryset.filter(product__title__icontains=product)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['sales_metrics'] = get_sales_metrics()
        return context

class OutflowCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Outflow
    form_class = OutflowForm
    template_name = 'outflow_form.html'
    success_url = '/outflows/list'
    permission_required = 'outflows.add_outflow'

class OutflowDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Outflow
    template_name = 'outflow_detail.html'
    context_object_name = 'outflows'
    permission_required = 'outflows.view_outflow'

class OutflowCreateListAPIView(generics.ListCreateAPIView):
    queryset = Outflow.objects.all()
    serializer_class = OutflowSerializer

class OutflowRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Outflow.objects.all()
    serializer_class = OutflowSerializer
