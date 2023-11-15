from zeep import Client
import time

wsdl = "https://www.dataaccess.com/webservicesserver/TextCasing.wso?wsdl"
client = Client(wsdl)

def main(client):
    userInput = input("Skriv en tekst: ")
    timeStart = time.perf_counter()
    response = client.service.InvertStringCase(userInput)
    timeStop = time.perf_counter()
    print(f"{response} \nprogrammet brukte {round((timeStop-timeStart)*1000,2)} ms.")


if __name__ == "__main__":
    main(client)






