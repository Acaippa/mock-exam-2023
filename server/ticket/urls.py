from django.urls import path
from .views import ticket_register_view

urlpatterns = [
    path("register", ticket_register_view)
]