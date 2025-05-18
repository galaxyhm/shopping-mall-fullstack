from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="home_page_url_name"),
    path("products/", views.products, name="products_page_url_name"),
    path("login/", views.login, name="login_page_url_name"),
    path("singup/", views.singup, name="signup_page_url_name"),
]
