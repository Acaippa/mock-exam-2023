# innlevering prøveeksamen 2023
Dette er min innlevering av Prøveeksamen 2023. Under vil du også finne brukerveiledning for nettsiden.

## Hvordan Logge seg inn som administrator
**Om du vil legge til Brukere eller Grupper (avdelinger)** må du først gå inn på serverens hjemmeside. Deretter legge til /admin i URL'en. For eks. "localhost:8000/admin".
I boksen som kommer opp skriver du inn ditt brukernavn og passord. (Det er per nå kun Administrator, Rune og Magnus som kan logge seg inn i admin siden)


![image](https://user-images.githubusercontent.com/106773288/219670423-1b60a81f-96ce-4f71-8eca-a73446161129.png)


Når du er logget inn, trenger vi kun å fokusere på dette området.

### Legge til en ny bruker / annsatt 
For å legge til en ny annsatt på, trykker vi på +Add vedsiden av Users.


![image](https://user-images.githubusercontent.com/106773288/219671321-b1a54776-82ae-4dc5-a20e-723e294110cf.png)


Her vil du se brukeroversikten, som er alle brukerne lagret i databasen. For å legge til en ny bruker, se etter ADD USER+ øverst i høyre hjørne


![image](https://user-images.githubusercontent.com/106773288/219671699-7a022e94-f803-4e2a-9704-c9517c17ca89.png)


Deretter fyller du ut brukernavn og passord. Fint om Rune eller Magnus kommer til vedkommende som det skal lages konto til, slik at vedkommende kan skrive inn sitt eget brukeravn og passord.
Deretter kommer du til refigeringssiden til brukeren. Du vil goså komme hit om du trykker på brukeren i brukeroversikten. Om du ønsker at den nye brukeren skal ha tilgang til Admin siden, kan du krysse av "Staff Status" under Permissions.


![image](https://user-images.githubusercontent.com/106773288/219673102-27bfbb28-bca7-4f8f-ac62-d99657196ecd.png)


Under Permissions kan du endre på hvilke grupper som brukeren skal være en del av ved å trykke på gruppen og deretter pilen som peker til høyre, slik at gruppenavnet havnet i boksen til høyre.

![image](https://user-images.githubusercontent.com/106773288/219674586-e835ca9a-54d4-4b51-bb65-2f25cca3737b.png)



Trykk deretter på SAVE for å lagre endringene.


## Legge til en ny Avdeling / Group
Start med å trykke på +ADD til høyre for groups

![image](https://user-images.githubusercontent.com/106773288/219675582-5bc452b1-7cb8-460f-99ac-a9709b79cd84.png)


Skriv deretter inn navnet og trykk på SAVE for å lagre.


## Hvordan legge til nye statuser


Start med å trykke på +ADD til høyre for Statuser


![image](https://user-images.githubusercontent.com/106773288/219675898-159e3593-f340-487b-81be-61e589d0fd46.png)


Skriv deretter inn navnet på statusen og trykk på SAVE for å lagre. Ettersom farger på statuser ikke er implementert enda, kan du la denne stå som hvit.


Ved å kun trykke på enten Statuser, eller Tickets, vil du kunne se en oversikt over alle enhetene av de i databasen. Trykk på en av de for å endre på en spesifik enhet.

![image](https://user-images.githubusercontent.com/106773288/219676520-1c5ded47-60de-4cd2-8a6a-b6bcb9ab6ebc.png)


# Legg til ny database enhet


Her forklares det hvordan man kan legge til nye enheter i databasen
## Definer modellen i models.py

inne i server > tickets > models.py vil du finne en python representasjon av modellene i databasen. Referer til https://docs.djangoproject.com/en/4.1/ref/models/fields/ for en dybdeforklaring.

For å lage en ny modell, må man lage en klasse som arver egenskapende til en innebygd modul i Django.


![image](https://user-images.githubusercontent.com/106773288/219677610-44fca2b6-5d7e-44e0-9af1-301fb44dc976.png)


Over ser du Status modellen som blir brukt i nettsiden.
``__str__`` funskjonen blir brukt for å bestemme hvilket navn som skal vises i databaseoversikten når man ser på enheten.
``Meta`` Underklassen har en funskjon som endrer pluralet til enhetsnavnet. Slik at det blir "stauser" og ikke "statuss".


For at Django nå skal legge til den nye modellen i Databasen, må du gå inn i ``Consollen`` og ``CD`` inn i plasseringen til ``manage.py`` filen. 
Deretter må kommandoen ``python manage.py makemigrations`` og ``pyhton manage.py migrate`` kjøres for at databasen skal oppdatere seg. Dette må gjøres hver gang man endrer på noe i models.py filen.
