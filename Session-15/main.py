from flask import Flask


app = Flask("__main__")


@app.route("/")
def home():
	return "Manu is the Owner"

# home = app.route("/home")

if __name__ == "__main__":
	app.run(port=8000)
