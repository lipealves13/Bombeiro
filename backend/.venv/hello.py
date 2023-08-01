from flask import FlasK
app = Flask(__name__)
desastre = False

@app.route("/")
def mensagem():
        if desastre:
            return "Desastre"
        else:
            return "Nada para Reportar"

@app.route("/desastre", methods=["POST"])
def set_desastre():
    global desastre
    desastre = True
    return "Desastre definido como True"

@app.route("/desastre", methods=["DELETE"])
def reset_desastre():
    global desastre
    desastre = False
    return "Desastre definido como False"
