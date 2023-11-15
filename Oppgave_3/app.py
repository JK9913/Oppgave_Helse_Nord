import os, json
from flask import Flask
from Oppgave_2.Oppgave_2_V2  import Pasient, requestAPI
# Lager instanse av flask
app = Flask(__name__)

# Route fungerer som endpoints. String i parantes forteller hva som skal trigge de forskjellige funksjonene.
@app.route('/')
def index():
    return "Server works"

@app.route('/greet')
def say_hello():
    return 'Hello from Server'

@app.route('/patient_JSON/{id}')
def getPatientInfo():
    response = requestAPI

