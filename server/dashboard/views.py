from django.shortcuts import render
from django.contrib.auth.signals import user_logged_out, user_logged_in
from django.dispatch import receiver
from django.contrib import messages

from ticket.models import Ticket

# Create your views here.
def home_view(request):
    return render(request, "index.html", {})

def dashboard_home_view(request):
    tickets = Ticket.objects.all()

    return render(request, "dashboard_home.html", {"tickets" : tickets})

@receiver(user_logged_out)
def on_user_logged_out(sender, request, **kwargs):
    messages.add_message(request, messages.INFO, 'Du er logget ut!')

@receiver(user_logged_in)
def on_user_logged_out(sender, request, **kwargs):
    messages.add_message(request, messages.INFO, f'Du er logget inn som {request.user}!')