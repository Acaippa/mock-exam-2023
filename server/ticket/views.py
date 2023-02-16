from django.shortcuts import render
from .models import Ticket
from .forms import TicketForm

from django.contrib import messages

# Create your views here.
def ticket_register_view(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Ticket lagt til!", extra_tags="notification")

    return render(request, "ticket/register_ticket.html", {'form' : TicketForm()}) # Ticket registrasjons siden