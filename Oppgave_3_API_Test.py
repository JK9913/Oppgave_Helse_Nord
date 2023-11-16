import requests
from Oppgave_2 import hentPasientIDFraBruker, provIgjen




def xmlEllerJson():
    inputFraBruker = input("Hvilket format ønsker du?\n1.JSON\n2.XML\nSkriv 1 eller 2: ")
    while inputFraBruker != "1" and inputFraBruker != "2":
        inputFraBruker = input("Ikke gyldig input!\n1.JSON\n2.XML\nSkriv 1 eller 2: ")
    if inputFraBruker == "1":
        return "JSON"
    else:
        return "XML"

def requestXML(id):
    try:
        response = requests.get(f"http://127.0.0.1:5000/patient_XML/{id}")
    except Exception as err:
        failed = input(f"Connection failed with message: {err}")
    print(response.text)

def requestJSON(id):
    try:
        response = requests.get(f"http://127.0.0.1:5000/patient_JSON/{id}")
    except Exception as err:
        failed = input(f"Connection failed with message: {err}")
    print(response.text)   



def main():
    responsType = xmlEllerJson()
    pasientID = hentPasientIDFraBruker()

    if responsType == "JSON":
        requestJSON(pasientID)
    else:
        requestXML(pasientID)


if __name__ == "__main__":
    loop = True

    while loop:
        main()
        loop = provIgjen()