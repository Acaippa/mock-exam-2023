from django.db import models
from colorfield.fields import ColorField

class Avdeling(models.Model):
    Navn = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "Avdelinger"

def get_default_avdeling():
    return Avdeling.objects.filter(Navn="Tildelning")

class Status(models.Model):
    Navn = models.CharField(max_length=60)
    Farge = ColorField(default="#FFFFFF")

    class Meta:
        verbose_name_plural = "Statuser"


def get_default_status():
    return Status.objects.filter(Navn="Åpen")

class Teknikker(models.Model):
    Navn = models.CharField(max_length=100)
    Email = models.EmailField(max_length=100)
    Avdeling = models.ForeignKey(Avdeling, default=get_default_avdeling, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name_plural = "Teknikkere"

class Ticket(models.Model):
    Emne = models.CharField(max_length=100)
    Sender_epost = models.EmailField(max_length=100)
    Sender_navn = models.CharField(max_length=100)
    Melding = models.TextField(max_length=2000)
    # Bilde = models.ImageField
    Tildelt = models.ForeignKey(Teknikker, on_delete=models.DO_NOTHING, null=True, blank=True)
    Tildelt_avdeling = models.ForeignKey(Avdeling, on_delete=models.DO_NOTHING, default=get_default_avdeling, null=True, blank=True)
    Dato_lagd = models.DateField(auto_now_add=True)
    Status = models.ForeignKey(Status, default=get_default_status, on_delete=models.DO_NOTHING, null=True, blank=True)