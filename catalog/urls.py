from django.urls import path

from blog.views import ProductCreateView, ProductUpdateView
from catalog.apps import CatalogConfig
from catalog.views import HomeView, ContactsView, ProductDetailView, ProductListView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('', ContactsView.as_view(), name='contacts'),
    path("product_detail/<int:pk>", ProductDetailView.as_view(), name='product_detail'),
    path('home', ProductListView.as_view(), name='product_list'),
    path('products/create_product', ProductCreateView.as_view(), name='product_list'),
    path('products/update_product/<int:pk>', ProductUpdateView.as_view(), name='product_list')
]