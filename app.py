from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Assalam o Alaikum! Meri pehli Azure app 🚀</h1><p>Week 7 · NIAI × NAVTTC</p>"
