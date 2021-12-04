from django.urls import path, include
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
        #Leave as empty string for base url
	path('', views.store, name="store"),
	path('register/', views.register, name="register"),
	path('', include("django.contrib.auth.urls")),
	path('cart/', views.cart, name="cart"),
	path('checkout/', views.checkout, name="checkout"),
	path('search/',views.search ,name="search"),
	path('product/<slug:slug>',views.single, name="single_product")

]