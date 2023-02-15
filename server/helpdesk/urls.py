
from django.contrib import admin
from django.urls import path, include
import ticket.urls as ticket_url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ticket/', include(ticket_url)) # Inkluder URL'er fra ticket appen
]
