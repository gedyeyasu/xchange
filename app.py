import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():

	return render_template("index.html")


@app.route("/rates")
def rates():

	#value to be sent to form
	res= requests.get("http://data.fixer.io/api/latest?access_key=23bd78a271bd8f29985a755297f0560a")
	data=res.json()
	base=data["symbols"]


	#returned value from the form
	base_syb=request.from.get("base_syb")
	xch_syb=request.from.get("xch_syb")
	base_val=request.from.get("base_val")

	return render_template("rates.html")	