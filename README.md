# K&L Ticket system - Prøveeksamen 2023
Jeg har fått i oppgave å lage ett ticket-system for bedriften Kjelvik og Lundestad. Jeg har i den annledning brukt web-rammeverket Django. Denne dokumentasjonen vil ta for seg oppsettet til Django rammeverket, og hvordan du kan utvidde databasen.
Denne veiledningen er rettet mot nye utviklere, men det trengs medium kunnskaper om [Python](https://www.python.org/) sjekk gjerne ut [Python OOP](https://realpython.com/python3-object-oriented-programming/). Referer gjerne også til Django's dokumenasjon [her](https://docs.djangoproject.com/en/4.2/). En grunnleggende forståelse av HTML er også nødvendig. [HTML](https://www.w3schools.com/html/)

## Beskrivelse av oppsett

### Django og klienter

Django tar imot forespørsler fra klienter, og sender tilbake ett svar i form av en HTML fil. Det som er intressant for oss utviklere, er at django har mulighet til å sende en såkalt ["context"](https://docs.djangoproject.com/en/4.2/ref/templates/api/#:~:text=Rendering%20a%20context%C2%B6). Som i denne sammenhengen vil si at man kan sende variabler fra back-end i Django, og vise disse i nettleseren. Disse contextene er ofte spørringer fra en database. 

En simplifisert kobling mellom Django og en klient kan derfor visualiseres som følger:


![image](https://user-images.githubusercontent.com/106773288/232400148-63739002-d41f-4513-9075-9139c5f2cfc0.png)

### Django i detalj
Videre, så skal veiledningen fordype seg i Django's komunikasjon innad i seg selv. Dette skal vi gjøre ved en intuitiv oppbygning av ett nytt database-objekt i Django prosjektet vårt. Referer [hit](https://docs.djangoproject.com/en/4.2/intro/tutorial01/) for oppstart av projektet.


Dette er slik Django prosseserer en forespørsel:



![unnamed0](https://user-images.githubusercontent.com/106773288/232402049-9c605d4c-ac77-453d-a4f7-c8c106add307.svg)

For å fordype oss i denne, så skal vi trinnvis gå gjennom hvordan vi legger til en ny databasemodell i Django, og hvordan vi viser den hos sluttbrukeren.

Filen urls.py router de forskjellige URL 'ene Django mottar, til en funskjon i views.py. I dette eksempelet skal vi route URL 'en `/home` til en funskjon som returnerer index.html.

``` PYTHON
# urls.py

from django.urls import path

from . import views

urlpatterns = [
path("/home", views.home_view) # Bind /home til home_view funskjonen i views.py
]

```

```PYTHON
# views.py

from django.shortcuts import render

def home_view(request):
    return render(request, "home.html", {}) # <- Din context her...

```

Dictionariet, som er det siste parameteret vi passer inn i funskjonen `render`, i views.py er contexten som vi kan be Django sende til klienten. Her binder vi navnet på variabelen vi sender, med verdien på den. for eks;

`{ "brukere" : [bruker1, bruker2, bruker3] }`


Vil man lage en ny modell i databasen og fremvise den for brukeren derimot, så må vi lage en database-modell først. Referer til [Django models-dokumentasjon](https://docs.djangoproject.com/en/4.2/topics/db/models/) for oversikt over forskjellige `Field types`. Under er ett eksempel på hvordan vi kan legge til en bok som en rad i databasen.

![unnamed1](https://user-images.githubusercontent.com/106773288/232408107-38932e10-034a-4b88-ac6c-5e77c22b8d0b.svg)

Slik vil objektet "Bok" se ut.

```PYTHON
# models.py

from django.db import models

class Bok:
    tittel = models.CharField(max_length=255) # En streng med max 255 bokstaver.
    forfatter = models.CharField(max_length=255)

```


Nå som vi har laget en modell for hvordan "Bok" skal se ut i databasen, må faktisk legge den til i Django's innebygde database. Dette gjøres ved å kjøre to kommandoer i samme mappe der `manage.py` bor.
`python manage.py makemigrations` og deretter
`python manage.py migrate`. Om du ikke får opp noen Error-meldinger etter å ha kjørt disse kommandoene, kan vi gå videre.

For å forenkle prosessen av å legge til en ny bok i databasen, så skal vi registrere modellen i admin.py.

```PYTHON
# admin.py

from django.contrib import admin
from .models import Bok # Modellen vi nettop lagde!

admin.site.register(Bok) # Legg til modellen i admin panelet
```

Nå skal det være mulig å logge deg inn på admin siden i Django prosjektet ditt, og se "Boks" (Django pluraliserer på engelsk, dette kan endres om du vil det [link](https://stackoverflow.com/questions/2587707/django-fix-admin-plural#:~:text=Well%20well%2C%20it%20seems%20like%20the%20Meta%20class%20approach%20still%20works.%20So%20placing%20a%20meta%20class%20inside%20your%20model%20will%20still%20do%20the%20trick%3A)). Om du trykker add, så kan du legge til nye bok-objekter i databasen. *NB!* Merk at du må ha en superuser definert i Django for å få tilgang til admin panelet. Kjør kommandoen `python manage.py createsuperuser` og fyll inn de ønskede parameterne for å opprette det.

Etter å ha lagt inn ett par bok-objekter, så kan vi gå videre til å faktisk vise de på nettsiden.

i `views.py` var det andre parameteret `home.html`. Dette er HTML filen som vi skal sende til brukeren. Først og fremst må vi legge til en `templates` mappe der `home.html` kan bo. Referer til [denne](https://docs.djangoproject.com/en/4.2/howto/overriding-templates/) lenken på hvordan det konfigureres. Inne i `/templates` legger vi til en ny fil; `home.html`.

```HTML
# home.html

<h1> Alle bøker i databasen </h1>
{{boker}} <!-- https://docs.djangoproject.com/en/4.2/ref/templates/language/ -->

```

Det siste vi trenger å gjøre da, er å legge til contexten i `views.py`

```PYTHON
# views.py

from django.shortcuts import render
from .models import Bok

def home_view(request):
    return render(request, "home.html", {"boker" : Bok.objects.all()}) # <- Hent ut alle bøkene i databasen. Unngå ÆØÅ i variabelnavn. (Bøker -> Boker)

```

Gratulerer! Du har nå knyttet sammen en database til en nettside. Les over veiledningen flere ganger og bruk internettet om du sitter fast noe sted. Django er ett fantastisk rammeverk med massevis av muligheter. God koding!
