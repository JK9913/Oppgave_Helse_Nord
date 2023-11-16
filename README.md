# Oppgave_Helse_Nord
Tre oppgaver fra helse nord som må løses.


Oppgave 1:
    Bruker zeep modul for å lettere jobbe med XML format i WSDL. Denne modulen er ikke standard i python og jeg har derfor laget en requirements.txt fil for å installere dependencies. For å installere kjør "pip install -r requirements.txt" i kommandofeltet i mappen til .py filen. Dette vil installere modulen(e) man trenger.

Oppgave 2:
    Kobler til api med requests modulen og bruker pasient ID spørring for å hente informasjon om pasient. Lager en class for pasient som skal inneholde nødvendig data. For hver spørring blir det laget en pasient class som deretter brukes for å skrive til kommandolinjen.

Oppgave 3:
    Oppgave 3 består av flere filer. app.py inneholder webservicen laget med Flask-modulen. Her er det definert noen få spørringer med app.route funksjonen. "/greeting" brukes for å teste serveren. "/pasient_JSON/<id>" gjør det mulig å sende en spørring med en id som gir resultat i JSON (det same gjelder hvis du bytter ut "JSON" med "XML" i URL'en, men vil da returnere XML-format). 

    I koden benyttes modulen xml.etree.ElementTree for å bygge opp xml. For å kjøre webservicen må man først kjøre flask run på appy.py, dette vil starte serveren på 127.0.0.1:5000 (localhost port 5000). Dette er viktig for å kunne teste API'et. Deretter må det åpnes en ny kommandlinje som kjører Oppgave_3_API_Test.py. Hvis ikke dette gjøres vil API'et feile. API-testen er laget for å teste både JSON format og XML format, samt at brukeren kan velge hvilken ID som skal testes. 

    Oppgave_2.py importeres i begge filene til oppgave 3 hvor både class og functions blir brukt. Det er også brukt virtual environment for Flask.