from django.urls import path
from catalog.apps import CatalogConfig
from .views import ProductListView, ProductDetailView, HomeTemplateView, ContactsTemplateView

app_name = CatalogConfig.name

urlpatterns = [
    path('', HomeTemplateView.as_view(), name='home'),
    path('contacts/', ContactsTemplateView.as_view(), name='contacts'),
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('product_detail/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
]
