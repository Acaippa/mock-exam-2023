from django.shortcuts import render
from .models import Ticket
from .forms import TicketForm

# Create your views here.
def ticket_register_view(request):
    return render(request, "ticket/register_ticket.html", {'form' : TicketForm()}) # Ticket registrasjons siden