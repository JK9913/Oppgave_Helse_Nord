import requests, math
from datetime import datetime



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



def main():
    # Få pasient-ID og hent respons fra server
    pasientID = hentPasientIDFraBruker()
    response = requests.get(f"https://hapi.fhir.org/baseR4/Patient/{pasientID}")

    # Sjekk responskode
    if response.status_code == 200:
        print("Gyldig pasient-ID")
        responseJSON = response.json()

        # Går gjennom og printer informasjon som er tilgjgenglig fra spørringen
        for key in responseJSON.keys():
            match key:
                case "name":
                    print(f"Fornavn: {' '.join(responseJSON[key][0]['given'])}")
                    
                    print(f"Etternavn: {responseJSON[key][0]['family']}")
                
                case "gender":
                    print(f"Kjønn: {'Mann' if responseJSON[key] == 'male' else 'Kvinne'}")

                case "birthDate":
                    # Konverter string til datetime
                    tempDato = datetime.strptime(responseJSON[key],"%Y-%m-%d")
                    # Konverterer tilbake til string, men med rett format.
                    print(f"Fødselsdato: {tempDato.strftime('%d.%m.%Y')}")
                    # Finn alder på pasient
                    print(f"Alder: {math.floor((datetime.now()-tempDato).days/365)}")
 

    else:
        print(f"Ikke gyldig pasient-ID. Statuskode: {response.status_code}")





if __name__ == "__main__":
    loop = True

    while loop:
        main()
        loop = provIgjen()

