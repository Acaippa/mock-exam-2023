from django.contrib import admin
from .models import Ticket, Teknikker, Avdeling, Status

# Register your models here.
admin.site.register(Ticket)
admin.site.register(Teknikker)
admin.site.register(Avdeling)
admin.site.register(Status)