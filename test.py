import requests

def main():
	res=requests.get("http://data.fixer.io/api/symbols?access_key=23bd78a271bd8f29985a755297f0560a")
	
	li={'adam':'boy', 'alice':'girl', }
	data=res.json()
	base=data["symbols"]

	res2=requests.get("http://data.fixer.io/api/convert?access_key=23bd78a271bd8f29985a755297f0560a& from = base_syb& to = xch_syb& amount = base_val")
	ret=res2["result"]
	

	for items in base.values:
		print(items)


	#	for item in data:
	#	print("with for lopp")
	#for lists in base:
	#	print(lists)


if __name__ == '__main__':
	main()