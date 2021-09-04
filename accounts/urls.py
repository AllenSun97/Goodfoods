from django.urls import path
from . import views
from .views import MenuView

urlpatterns = [
    path('', views.home, name="home"),
    path('menu/', MenuView.as_view(), name="menu"),
    path('menu/add_to_cart/<int:pk>', views.add_to_cart, name="add_to_cart"),
    path('contact/', views.contact, name="contact"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('update_item/', views.updateItem, name="update_item"),
    path('process_order/', views.processOrder, name="process_order"),
]