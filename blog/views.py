from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy, reverse

from blog.models import Paper
from catalog.forms import ProductForm
from catalog.models import Product


class ProductCreateView(CreateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('products:product_list')


class ProductUpdateView(UpdateView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('products:product_list')

class PaperListView(ListView):
    model = Paper

    def get_queryset(self):
        return Paper.objects.filter(publication=True)


class PaperDetailView(DetailView):
    model = Paper

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views += 1
        self.object.save()
        return self.object


class PaperCreateView(CreateView):
    model = Paper
    fields = ('title', 'description', 'image', 'publication', 'views')
    success_url = reverse_lazy('blog:paper_list')


class PaperUpdateView(UpdateView):
    model = Paper
    fields = ('title', 'description', 'image', 'publication', 'views')
    success_url = reverse_lazy('blog:paper_list')

    def get_success_url(self):
        return reverse('blog:paper_detail', args=[self.kwargs.get('pk')])


class PaperDeleteView(DeleteView):
    model = Paper
    success_url = reverse_lazy('blog:paper_list')
