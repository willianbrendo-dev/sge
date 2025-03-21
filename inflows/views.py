from django.views.generic import ListView, CreateView, DetailView
from .models import Inflow
from .forms import InflowForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from rest_framework import generics
from .serializers import InflowSerializer


class InflowListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):

    model = Inflow
    template_name = 'inflow_list.html'
    context_object_name = 'inflows'
    paginate_by = 10
    permission_required = 'inflows.view_inflow'


    def get_queryset(self):
        queryset = super().get_queryset()
        product = self.request.GET.get('product')
        if product:
            queryset = queryset.filter(product__title__icontains=product)
        return queryset

class InflowCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Inflow
    form_class = InflowForm
    template_name = 'inflow_form.html'
    success_url = '/inflows/list'
    permission_required = 'inflows.add_inflow'

class InflowDetailView(LoginRequiredMixin, PermissionRequiredMixin, DetailView):
    model = Inflow
    template_name = 'inflow_detail.html'
    context_object_name = 'inflows'
    permission_required = 'inflows.view_inflow'


class InflowCreateListApiView(generics.ListCreateAPIView):
    queryset = Inflow.objects.all()
    serializer_class = InflowSerializer

class InflowRetrieveAPIView(generics.RetrieveAPIView):
    queryset = Inflow.objects.all()
    serializer_class = InflowSerializer
