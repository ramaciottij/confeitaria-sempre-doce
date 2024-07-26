from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def inicial():
    return render_template("index.html")

@app.route("/contatos")
def contato():
    return  render_template("contato.html")

@app.route("/sobre")
def sobre():
    return  render_template("sobre.html")

@app.route("/modelos")
def modelos():
    return  render_template("modelos.html")

if __name__ == '__main__':
    app.run()

