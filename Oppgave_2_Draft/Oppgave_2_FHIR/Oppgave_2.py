from fhirclient import client
from datetime import datetime
import math
settings={
    'app_id': 'my_web_app',
    'api_base': 'http://hapi.fhir.org/baseR4'
}
smart = client.FHIRClient(settings=settings)


def hentIDFraBruker():
    id = input("Skriv en pasient-ID: ")
    return id

def fhirSporring(id):
    import fhirclient.models.patient as p
    pasient = p.Patient.read(f"{id}", smart.server)
    return pasient


def main(server):
    id = hentIDFraBruker()

    
    try:
        pasient = fhirSporring(id)
        print(f"navn: {pasient.name[0].given[0]}")
        print(f"Kjønn: {pasient.gender}")
        try:
            print(f"Fødselsdato: {datetime.strptime(pasient.birthDate.isostring, '%Y-%M-%d').strftime('%d.%m.%Y')}")
            print(f"Alder: {math.floor((datetime.now()-datetime.strptime(pasient.birthDate.isostring, '%Y-%M-%d')).days/365)}")
        except Exception as err:
            print(f"Fødselsdato ikke definert. Feilmelding: {err}")
    except Exception as err:
        print(f"ID: {id}, er ikke gylidg. Feilmelding: {err}")


if __name__ == "__main__":
    loop = True
    while loop:
        main(smart)

