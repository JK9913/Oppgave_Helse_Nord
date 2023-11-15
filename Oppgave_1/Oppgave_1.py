from zeep import Client
import time, os

# Henter ut working directory
absolutePath = os.path.dirname(__file__)

# Kombinerer working directory med wsdl-filen for å kunne lese den
wsdl = os.path.join(absolutePath, "TextCasing.wsdl")
client = Client(wsdl)

def main(client):
    userInput = input("Skriv en tekst: ")
    timeStart = time.perf_counter()
    response = client.service.InvertStringCase(userInput)
    timeStop = time.perf_counter()
    print(f"{response} \nprogrammet brukte {round((timeStop-timeStart)*1000,2)} ms.")

# Spørr bruker om ny tekst og sjekk respons
def tryAgain():
    askUser = input("Vil du prøve en til tekst? (Y/N): ")
    
    while askUser.lower() != "n" and askUser.lower() != "y": 
        askUser = input("Vennligst bruk bokstavene Y (ja) eller N (nei). Vil du skrive en til tekst?: ")
    

    return askUser.lower() == "y"

        

if __name__ == "__main__":
    
    # Settes til true for å starte første kjøring av programmet
    userWantsToTryAgain = True

    # Looper til bruker er ferdig
    while userWantsToTryAgain:
        main(client)

        # Spørr brukeren om å prøve igjen
        userWantsToTryAgain = tryAgain()

        


    







