from django.urls import path
from catalog.apps import CatalogConfig
from catalog.views import home, contacts, product_detail, products_list

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('', contacts, name='contacts'),
    path("product_detail/<int:pk>", product_detail, name='product_detail'),
    path('home', products_list, name='products_list')
]