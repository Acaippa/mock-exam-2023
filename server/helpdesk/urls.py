
from django.contrib import admin
from django.urls import path, include, re_path
import ticket.urls as ticket_url
from dashboard.views import home_view, dashboard_home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ticket/', include(ticket_url)), # Inkluder URL'er fra ticket appen
    re_path(r"^accounts/", include("django.contrib.auth.urls")),

    path("", home_view),
    path("dashboard/home", dashboard_home_view)
]
