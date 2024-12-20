from django.views.generic import ListView, DetailView, TemplateView

from catalog.models import Product

from django.shortcuts import render

from catalog.models import Product


# def home(request):
#     return render(request, 'home.html')


class HomeView(TemplateView):
    template_name = 'catalog/home.html'


# def contacts(request):
#     return render(request, 'contacts.html')


class ContactsView(TemplateView):
    template_name = 'catalog/contacts.html'


# def product_detail(request, pk):
#     product = Product.objects.get(pk=pk)
#     context = {
#         "product_name": product.name,
#         "product_description": product.description,
#         "product_image": product.image,
#         "product_category": product.category,
#         "product_price": product.price,
#         "product_created_at": product.created_at,
#         "product_updated_at": product.updated_at
#     }
#     return render(request, "product_detail.html", context=context)


class ProductDetailView(DetailView):
    model = Product


# def products_list(request):
#     products = Product.objects.all()
#     context = {"products": products}
#     return render(request, 'home.html', context)


class ProductListView(ListView):
    model = Product
