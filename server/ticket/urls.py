from django.urls import path
from .views import ticket_register_view, ticket_edit_view, ticket_remove_view, multiple_ticket_remove_view

urlpatterns = [
    path("register", ticket_register_view),
    path("edit/<int:ticketId>", ticket_edit_view), 
    path("remove/<int:ticketId>", ticket_remove_view),
    path("remove-r/<str:ticketIds>", multiple_ticket_remove_view),
]