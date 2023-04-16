from django.shortcuts import render, redirect
from .models import Ticket
from .forms import TicketForm, EditTicketForm


from django.contrib import messages

def check_if_logged_in(request):
    if request.user.is_authenticated == False:
        return False
    else:
        return True

# Create your views here.
def ticket_register_view(request):
    
    form = TicketForm()

    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, "Ticket lagt til!", extra_tags="notification")

    return render(request, "ticket/register_ticket.html", {'form' : form}) # Ticket registrasjons siden



def ticket_edit_view(request, ticketId):
    if check_if_logged_in(request):
    
        ticket = Ticket.objects.get(id=ticketId)

        form = EditTicketForm(instance=ticket)

        if request.method == "POST":
            form = EditTicketForm(data = request.POST, instance=ticket)
            if form.is_valid():
                form.save() 
                messages.add_message(request, messages.SUCCESS, "Ticket oppdatert!", extra_tags="notification")
                return redirect("/dashboard/home")

        return render(request, "ticket/edit_ticket.html", {"form" : form, "ticketId" : ticketId})

    else:
        return redirect("/accounts/login")

def ticket_remove_view(request, ticketId):
    if check_if_logged_in(request):

        ticket = Ticket.objects.get(id=ticketId)
        ticket.delete()
        messages.add_message(request, messages.SUCCESS, "Ticket fjernet!", extra_tags="notification")

        return redirect("/")
    else:
        return redirect("/accounts/login")

def multiple_ticket_remove_view(request, ticketIds):
    if check_if_logged_in(request):

        for ticketId in ticketIds.split(","):
            ticket = Ticket.objects.get(id=ticketId)
            ticket.delete()

        return redirect("/dashboard/home")
    else:
        return redirect("/accounts/login")
