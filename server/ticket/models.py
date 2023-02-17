from django.db import models
from colorfield.fields import ColorField
from django.contrib.auth.models import User, Group

def get_default_avdeling():
    default = Group.objects.filter(name="Tildelning")
    return default[0] if len(default) != 0 else None

class Status(models.Model):
    Navn = models.CharField(max_length=60)
    Farge = ColorField(default="#FFFFFF")

    def __str__(self):
        return self.Navn

    class Meta:
        verbose_name_plural = "Statuser"


def get_default_status():
    default = Status.objects.filter(Navn="Åpen")
    return default[0] if len(default) != 0 else None


class Ticket(models.Model):
    Emne = models.CharField(max_length=100)
    Sender_epost = models.EmailField(max_length=100)
    Sender_navn = models.CharField(max_length=100)
    Melding = models.TextField(max_length=2000)
    # Bilde = models.ImageField
    Tildelt = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True, blank=True, default=None)
    Tildelt_avdeling = models.ForeignKey(Group, on_delete=models.DO_NOTHING, default=get_default_avdeling, null=True, blank=True)
    Dato_lagd = models.DateField(auto_now_add=True)
    Status = models.ForeignKey(Status, default=get_default_status, on_delete=models.DO_NOTHING, blank=True)

    def __str__(self):
        return f"{self.Emne}  {self.Status}"