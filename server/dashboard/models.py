from django.db import models

class FAQ(models.Model):
    Tittel = models.CharField(max_length=255)
    Beskrivelse = models.CharField(max_length=2000)

    def __str__(self):
        return self.Tittel

