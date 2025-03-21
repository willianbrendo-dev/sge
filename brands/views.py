from django.views.generic import ListView, CreateView, DetailView, UpdateView, DeleteView
from .models import Brand
from .forms import BrandForm
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from rest_framework import generics
from .serializers import BrandSerializer


class BrandListView(LoginRequiredMixin, PermissionRequiredMixin, ListView):

    model = Brand
    template_name = 'brand_list.html'
    context_object_name = 'brands'
    paginate_by = 10
    permission_required = 'brands.view_brand'
    


    def get_queryset(self):
        queryset = super().get_queryset().order_by('name')
        name = self.request.GET.get('name')
        if name:
            queryset = queryset.filter(name__icontains=name).order_by('name')
        return queryset

class BrandCreateView(LoginRequiredMixin, CreateView):
    model = Brand
    form_class = BrandForm
    template_name = 'brand_form.html'
    success_url = '/brands/list'
    permission_required = 'brands.add_brand'


class BrandDetailView(LoginRequiredMixin,DetailView):
    model = Brand
    template_name = 'brand_detail.html'
    context_object_name = 'brand'
    permission_required = 'brands.view_brand'
    

class BrandUpdateView(LoginRequiredMixin,UpdateView):
    model = Brand
    form_class = BrandForm
    template_name = 'brand_update.html'
    success_url = '/brands/list'
    permission_required = 'brands.change_brand'
    

class BrandDeleteView(LoginRequiredMixin, DeleteView):
    model = Brand
    template_name = 'brand_delete.html'
    success_url = '/brands/list'
    permission_required = 'brands.delete_brand'


class BrandCreateListAPIView(generics.ListCreateAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

class BrandRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer

