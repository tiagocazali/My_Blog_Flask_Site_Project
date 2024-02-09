from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "VAMOS COMECAR!!!</p>"

@app.route("/teste")
def teste():
    return "Vamos ver se vai dar certo!"

@app.route("/mais")
def mais():
    return "Mais Uma tentativa"


if __name__ == "__main__":
    app.run(debug=True)