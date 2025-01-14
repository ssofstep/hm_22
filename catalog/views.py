from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product


class HomeView(TemplateView):
    template_name = 'catalog/home.html'


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'



class ProductDetailView(DetailView):
    model = Product

class ProductListView(ListView):
    model = Product
