import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():

	#value to be sent to form
	res= requests.get("http://data.fixer.io/api/symbols?access_key=23bd78a271bd8f29985a755297f0560a")
	data=res.json()
	currencies=data["symbols"]
	
	
	#returned value from the form
	base_syb=request.form.get("base_syb")
	xch_syb=request.form.get("target_syb")
	base_val=request.form.get("amount")


	return render_template("index.html", currencies=currencies)


@app.route("/convert", methods=["POST", "GET"])
def convert():

	#getting value from form
	base_syb=str(request.form.get("base_syb"))
	xch_syb=str(request.form.get("target_syb"))
	base_val=request.form.get("amount")

		

	#converting in to target currency
	res2=requests.get("https://api.exchangeratesapi.io/latest?base=USD&symbols=xch_syb HTTP/1.1")
	ret=res2.json()
	return(str(ret)) # just to return error
	if ret["success"]:
		result=ret["result"]
	else:
		return("Api request error") # just to return error


	return render_template("index.html", result=result)	

if __name__=='__main__':
    app.run(debug=True)