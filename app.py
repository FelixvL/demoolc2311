from flask import Flask
import felix


app = Flask(__name__)

@app.route("/vijfde/<verschillend>/<nogeen>")
def vijfde(verschillend, nogeen):
    return "<p>Je hebt meegegeven: "+verschillend+" EN "+nogeen+"</p>"

@app.route("/vierde")
def vierde():
    return felix.felixmethode()

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/tweede")
def anders():
    vara = 3
    vara += 15
    return "<p>Hele andere reactie</p>"+str(vara)

@app.route("/derde")
def derde():
    vara = 3
    vara += 15
    return "{ \"opdracht\" : \"Hele andere reactie\", \"aantal\" : \""+str(vara)+"\"}"