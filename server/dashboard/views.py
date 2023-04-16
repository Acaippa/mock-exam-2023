from django.shortcuts import render, redirect
from django.contrib.auth.signals import user_logged_out, user_logged_in
from django.dispatch import receiver
from django.contrib import messages

from ticket.models import Ticket
from .models import FAQ

# Create your views here.
def home_view(request):
    return render(request, "index.html", {"FAQs" : FAQ.objects.all()})

def dashboard_home_view(request):
    if request.user.is_authenticated == False:
        return redirect("/accounts/login/")
    
    tickets = Ticket.objects.all()

    if request.method == "POST":
        filter = request.POST["filter-select"]
        filter_search = request.POST["filter-search"]
        sort = request.POST["sort-select"]
        
        if filter != "":
            filter_key, filter_value = filter.split(":")

            tickets = tickets.filter(**{filter_key : filter_value})

        if filter_search != "":

            tickets = tickets.filter(**{"Emne__icontains" : filter_search})

        if sort != "":
            tickets = tickets.order_by(sort)

    return render(request, "dashboard_home.html", {"tickets" : tickets})

@receiver(user_logged_out)
def on_user_logged_out(sender, request, **kwargs):
    messages.add_message(request, messages.INFO, 'Du er logget ut!')

@receiver(user_logged_in)
def on_user_logged_out(sender, request, **kwargs):
    messages.add_message(request, messages.INFO, f'Du er logget inn som {request.user}!')