import requests, math
from datetime import datetime


class Pasient:

    def __init__(self, navn, etternavn, fodselsDato="", kjonn="") -> None:
        self.navn = navn
        self.etternavn = etternavn
        self.fodselsDato = fodselsDato
        self.kjonn = kjonn

    def finnAlder(self):
        if self.fodselsDato == "":
            return "Alder ikke mulig å beregne"
        
        # Konverter string til datetime
        tempDato = datetime.strptime(self.fodselsDato,"%Y-%m-%d")
        # Finn alder på pasient
        return math.floor((datetime.now()-tempDato).days/365)

    def konverterDato(self):
        if self.fodselsDato == "":
            return "Fødselsdato ikke registrert"
        
        # Konverter string til datetime
        tempDato = datetime.strptime(self.fodselsDato,"%Y-%m-%d")
        # Konverterer tilbake til string, men med rett format.
        return tempDato.strftime('%d.%m.%Y')
    
    def oversettKjonn(self):
        return 'Mann' if self.kjonn == 'male' else 'Kvinne'
    


# funksjon for å hente pasient-ID fra bruker
def hentPasientIDFraBruker():
    pasientID = input("Skriv inn pasientens ID: ")
    while not pasientID.isnumeric():
        pasientID = input("Bare tall er godtatt i dette feltet, prøv igjen: ")
    return pasientID

# Funksjon for å spørre bruker om å kjøre flere spørringer
def provIgjen():
    brukerRespons = input("Vil du prøve igjen? (Y/N): ")
    while brukerRespons.lower() != "y" and brukerRespons.lower() != "n":
        brukerRespons = input("Vennligst bruk Y (ja) eller N (nei): ")

    return brukerRespons.lower() == "y"


def requestAPI(id):
    return requests.get(f"https://hapi.fhir.org/baseR4/Patient/{id}")

def lagClass(jsonResponse):
    pasientInfo = Pasient(
            ' '.join(jsonResponse["name"][0]["given"]),
            jsonResponse["name"][0]['family'],
            jsonResponse["birthDate"] if "birthDate" in jsonResponse.keys() else "",
            jsonResponse["gender"] if "gender" in jsonResponse.keys() else ""
        )
    
    return pasientInfo


def main():
    # Få pasient-ID og hent respons fra server
    pasientID = hentPasientIDFraBruker()
    response = requestAPI(pasientID)

    
    if response.status_code == 200:
        print("Gyldig pasient-ID")
        responseJSON = response.json()

        # Lag instanse av pasient class
        pasientInfo = lagClass(responseJSON)

        # Skriv verdier til konsoll
        print(f"Fornavn: {pasientInfo.navn}")
        print(f"Etternavn: {pasientInfo.etternavn}")
        print(f"Kjønn: {pasientInfo.oversettKjonn() if pasientInfo.kjonn != '' else 'Kjønn er ikke registrert.'}")
        print(f"Fødselsdato: {pasientInfo.konverterDato()}")
        print(f"Alder: {pasientInfo.finnAlder()}")

    else:
        print(f"Ikke gyldig pasient-ID. Statuskode: {response.status_code}")





if __name__ == "__main__":
    loop = True

    while loop:
        main()
        loop = provIgjen()

