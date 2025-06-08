from django.urls import path
from catalog.apps import CatalogConfig
from .views import home, contacts, product_detail, product_list

app_name = CatalogConfig.name

urlpatterns = [
    path('', home, name='home'),
    path('contacts/', contacts, name='contacts'),
    path('product_list/', product_list, name='product_list'),
    path('product_detail/<int:pk>/', product_detail, name='product_detail'),
]
