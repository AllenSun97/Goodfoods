from django.urls import path
from . import views
from .views import MenuView

urlpatterns = [
    path('', views.home, name="home"),
    path('menu/', MenuView.as_view(), name="menu"),
    path('contact/', views.contact, name="contact"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
]