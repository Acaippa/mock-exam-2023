from django.forms import ModelForm, TextInput, Textarea, EmailInput, DateInput, Select
from .models import Ticket 

class TicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = ('Sender_navn', 'Sender_epost', 'Sender_status', 'Emne', 'Melding')

        labels = {
            "Sender_navn" : "Navn:",
            "Sender_epost" : "E-post:"
        }

        widgets = {
            "Sender_navn" : TextInput(attrs={"placeholder" : "Ditt fulle navn:", "class" : "form-control"}),
            "Sender_epost" : EmailInput(attrs={"placeholder" : "Din Email:", "class" : "form-control"}),
            "Sender_status" : Select(attrs={"placeholder" : "Din Email:", "class" : "form-control"}),
            "Emne" : TextInput(attrs={"placeholder" : "Forklar problemet kort:", "class" : "form-control"}),
            "Melding" : Textarea(attrs={"placeholder" : "Forklar problemet i detalj:", "class" : "form-control"}),
        }


class EditTicketForm(ModelForm):
    class Meta:
        model = Ticket
        fields = '__all__'

        widgets = {
             "Dato_lukket" : DateInput(attrs={"type" : "date"}),
        }