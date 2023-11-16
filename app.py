import re, json
from flask import Flask
from Oppgave_2  import requestAPI, lagClass
import xml.etree.ElementTree as ET

# Lager instanse av flask
app = Flask(__name__)
    

# Route fungerer som endpoints. String i parantes forteller hva som skal trigge de forskjellige funksjonene.
@app.route('/')
def index():
    return "Server works"

@app.route('/greet')
def say_hello():
    return 'Hello from Server'

@app.route('/patient_JSON/<id>')
def getPatientInfo(id):
    # fjerner "id="
    id = re.findall("[0-9]*$", id)[0]
    response = requestAPI(id)

    if response.status_code == 200:
        pasientInfo = lagClass(response.json())
        
        # Lag en JSON string for å returnere
        data = {}
        data["navn"] = pasientInfo.navn
        data["etternavn"] = pasientInfo.etternavn
        data["alder"] = pasientInfo.finnAlder()
        json_string = json.dumps(data)
        return json_string

    else:
        return f"Pasient finnes ikke. Prøv igjen. {id}, {response.status_code}, {response.text}"
    
@app.route('/patient_XML/<id>')
def getPatientInfoXML(id):
    response = requestAPI(id)

    if response.status_code == 200:
        pasientInfo = lagClass(response.json())

        # Lag XML for å returnere
        root = ET.Element("Patient")

        forNavn = ET.SubElement(root, "fornavn")
        etternavn = ET.SubElement(root, "etternavn")
        alder = ET.SubElement(root, "alder")

        forNavn.text = pasientInfo.navn
        etternavn.text = pasientInfo.etternavn
        alder.text = pasientInfo.finnAlder()

        return ET.tostring(root, encoding="unicode")
    
    else:
        return f"Pasient finnes ikke. Prøv igjen. {id}, {response.status_code}, {response.text}"

