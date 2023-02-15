from django.forms import ModelForm, TextInput, Textarea, EmailInput
from .models import Ticket 

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ('Sender_navn', 'Sender_epost', 'Emne', 'Melding')

        labels = {
            "Sender_navn" : "Navn:",
            "Sender_epost" : "E-post:"
        }

        widgets = {
            "Sender_navn" : TextInput(attrs={"placeholder" : "Ditt fulle navn:"}),
            "Sender_epost" : EmailInput(attrs={"placeholder" : "Din Email:"}),
            "Emne" : TextInput(attrs={"placeholder" : "Forklar problemet kort:"}),
            "Melding" : Textarea(attrs={"placeholder" : "Forklar problemet i detalj:"}),
        }