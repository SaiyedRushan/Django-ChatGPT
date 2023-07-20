from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("chat", views.chatbot, name="chatbot"),
    path("image", views.image, name="image"),
    path("login", views.login, name="login"),
    path("register", views.register, name="register"),
    path("logout", views.logout, name="logout"),
]
