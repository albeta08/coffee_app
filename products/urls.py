from .views import ProductFormView, ProductListView
from django.urls import path

urlpatterns = [
    path("", ProductListView.as_view(), name="List_product"),
    path("agregar/", ProductFormView.as_view(), name="add_product"),
]
