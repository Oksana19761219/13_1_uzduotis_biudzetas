from biudzeto_operacijos import skaiciuoti_biudzeto_balansa, \
    parodyti_biudzeto_ataskaita, \
    prideti_islaidu_irasa, \
    prideti_pajamu_irasa, \
    ispejimas

from flask import Flask, request, render_template



app = Flask(__name__)

@app.route("/")
def pradzia():
    return render_template("index.html")

@app.route("/pajamos.html")
def pajamos():
    return render_template("pajamos.html")

@app.route("/islaidos.html")
def islaidos():
    return render_template("islaidos.html")

@app.route("/balansas.html")
def balansas():
    pajamos, islaidos, balansas = skaiciuoti_biudzeto_balansa()
    return render_template("balansas.html", pajamos = pajamos, islaidos = islaidos, balansas = balansas)

@app.route("/biudzeto_ataskaita.html")
def ataskaita():
    pajamos, islaidos = parodyti_biudzeto_ataskaita()
    return render_template("biudzeto_ataskaita.html", pajamos = pajamos, islaidos=islaidos)

@app.route("/pajamos.html", methods=['POST'])
def ivesti_pajamas():
    if request.method == "POST":
        suma = request.form['suma']
        siuntejas = request.form['siuntejas']
        informacija = request.form['informacija']
        try:
            suma = float(suma)
            prideti_pajamu_irasa(suma, siuntejas, informacija)
            return render_template("index.html")
        except ValueError:
            return render_template("pajamos.html", ispejimas = ispejimas)
    else:
        return render_template("pajamos.html")


@app.route("/islaidos.html", methods= ['POST'])
def ivesti_islaidas():
    if request.method == "POST":
        suma = request.form['suma']
        atsiskaitymo_budas = request.form['atsiskaitymo_budas']
        isigyta_preke_paslauga = request.form['isigyta_preke_paslauga']
        try:
            suma = float(suma)
            prideti_islaidu_irasa(suma, atsiskaitymo_budas, isigyta_preke_paslauga)
            return render_template("index.html")
        except ValueError:
            return render_template("islaidos.html",ispejimas = ispejimas)
    else:
        return render_template("islaidos.html")


if __name__ == "__main__":
    app.run()