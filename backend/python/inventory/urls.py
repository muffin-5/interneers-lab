from django.urls import path
from . import views

urlpatterns = [
    path("products/", views.list_products, name="list_products"),
    path("products/<int:pk>/", views.get_product, name="get_product"),
    path("products/create/", views.create_product, name="create_product"),
    path("products/<int:pk>/update/", views.update_product, name="update_product"),
    path("products/<int:pk>/delete/", views.delete_product, name="delete_product"),
]
