from flask import Flask, render_template

app = Flask(__name__)
@app.route('/')
def principal():
	return render_template("index.html")
	if request.method == "POST":
		if request.form.get("fruta"):
			frutas.apped(request.form.get("fruta"))
	return render_template("index.html", frutas=frutas)
@app.route('\sobre')
def sobre():
	notas = {"Fulano":5.0, "Beltrano":6.0, "Aluno": 7.0, "Sicrano": 8.5, "Rodrigo":9.5)
	return render_template("sobre.html", notas=notas)

#http://137.0.0.1:5000