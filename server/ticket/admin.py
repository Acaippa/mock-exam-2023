from django.contrib import admin
from .models import Ticket, Status

# Register your models here.
admin.site.register(Ticket)
admin.site.register(Status)
