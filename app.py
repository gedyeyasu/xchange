import datetime
import requests
import os
from flask import Flask, render_template, request, session
from flask_session import Session

app = Flask(__name__)


app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.config["access_key"] = os.environ.get("access_key")

Session(app)

@app.route("/")
def index():

	#value to be sent to form
	
	res= requests.get("http://data.fixer.io/api/symbols?access_key=access_key")
	if res.status_code != 200:
		return (str("Poor Connection please refersh the page"))
	data=res.json()
	currencies=data["symbols"]

		
	return render_template("index.html", currencies=currencies)


@app.route("/convert", methods=["POST", "GET"])
def convert():


	#returned value from the form
	base_syb=request.form.get("base_syb")
	xch_syb=request.form.get("target_syb")
	base_val=request.form.get("amount")

	
	res2=requests.get("http://data.fixer.io/api/latest?access_key=access_key")
	if res2.status_code != 200:
		return (str("Poor Connection please refersh the page"))
	ret=res2.json()
	
	# just to return error
	if ret["success"]:
		#calculate target amount
		#convert first base to euro
		base_rate=ret["rates"][base_syb]
		euro=float(float(base_val) / float(base_rate))


		#convert then euro to target currency
		target_rate=ret["rates"][xch_syb]
		result=float(euro*float(target_rate))
		result=str(round(result,2))
		date=datetime.datetime.today()

	else:
		return("Api request error") # just to return error


	return render_template("result.html",amount=base_val,base_syb=base_syb,result=result, xch_syb=xch_syb, date=date)

if __name__=='__main__':
    app.run()