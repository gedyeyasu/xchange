import requests

def main():
	res=requests.get("http://data.fixer.io/api/latest?access_key=23bd78a271bd8f29985a755297f0560a")
	data=res.json()

	base=data["symbols"]
	print(base)



if __name__ == '__main__':
	main()