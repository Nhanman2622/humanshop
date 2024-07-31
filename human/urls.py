from django.urls import path
from human import views

app_name="Human"



urlpatterns=[
    path("", views.home, name='home'),
    path("product/", views.product, name='product'),
    path("more/", views.them, name='more' ),
    path("contact/", views.contact, name='contact'),
    path("product/<slug:product_slug>", views.productdetails, name='productdetails'),
    path("manager/", views.manager, name='manager'),
    path("manager/productsad/", views.productsmg, name='productsad' ),
    path("manager/themsad/", views.themsmg, name='themsad'),
    path("manager/add/product", views.add_products, name='addpr'),
    path("manager/edit/product/<str:product_id>", views.edit_products, name='editpr'),
    path("manager/delete/product/<str:product_id>", views.delete_products, name='deletepr')

]
