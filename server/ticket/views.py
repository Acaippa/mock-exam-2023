from django.shortcuts import render, redirect
from .models import Ticket
from .forms import TicketForm, EditTicketForm
from django.contrib.auth.decorators import login_required


from django.contrib import messages

# Create your views here.
def ticket_register_view(request):
    form = TicketForm()

    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Ticket lagt til!", extra_tags="notification")

    return render(request, "ticket/register_ticket.html", {'form' : form}) # Ticket registrasjons siden


@login_required(login_url="/accounts/login/")
def ticket_edit_view(request, ticketId):
    ticket = Ticket.objects.get(id=ticketId)

    form = EditTicketForm(instance=ticket)

    if request.method == "POST":
        form = EditTicketForm(data = request.POST, instance=ticket)
        if form.is_valid():
            form.save() 
            messages.add_message(request, messages.SUCCESS, "Ticket oppdatert!", extra_tags="notification")
            return redirect("/dashboard/home")

    return render(request, "ticket/edit_ticket.html", {"form" : form, "ticketId" : ticketId})

@login_required(login_url="/accounts/login/")
def ticket_remove_view(request, ticketId):
    ticket = Ticket.objects.get(id=ticketId)
    ticket.delete()
    messages.add_message(request, messages.SUCCESS, "Ticket fjernet!", extra_tags="notification")

    return redirect("/")

@login_required(login_url="/accounts/login/")
def multiple_ticket_remove_view(request, ticketIds):
    for ticketId in ticketIds.split(","):
        ticket = Ticket.objects.get(id=ticketId)
        ticket.delete()

    return redirect("/dashboard/home")
