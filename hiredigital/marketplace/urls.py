from django.urls import path

from marketplace.views import add_bulk_products, get_products, ProductView

urlpatterns = [
    path('addBulkProducts', add_bulk_products),
    path('getProducts', get_products),
    path('getProductDetail/<str:pk>', ProductView.as_view(), name="product-detail"),
]
