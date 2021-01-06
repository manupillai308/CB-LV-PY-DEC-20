from flask import Flask, jsonify, render_template, request, send_file

app = Flask(__name__) # Flask("__main__")



# @app.route("/")
# def root():
#     # return jsonify("Hello World")
#     return jsonify([1,2,3,4,5])

@app.route("/", methods=["GET", "POST"])
def pattern():
    if request.method=="GET":
        return render_template("enter_n.html")
    elif request.method == "POST":
        n = request.form.get("n")
        return render_template("pattern.html", n=int(n))


@app.route("/table", methods=["GET", "POST"])
def root():
    if request.method=="GET":
        return render_template("testcase_form.html")
    elif request.method == "POST":
        first_name = request.form.get("fname")
        last_name = request.form.get("lname")
        data = {"first_name":first_name, "last_name":last_name}
        # return render_template("response.html", data=[first_name, last_name])
        return render_template("response.html", data=data)


@app.route("/file", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        # return send_file("./image (1).jpg")
        return render_template("home.html")
    elif request.method == "POST":
        # name = request.form.get("fname") + request.form.get("lname")
        # return jsonify("Hello " + name)
        f = request.files.get("file")
        f.save(f.filename)
        return send_file(f.filename)

@app.route("/work")
def function():
    base = request.args.get("base")
    if base is None:
        return "Success with no base"
    else:
        return "Success with base " + base

# @app.route("/home")
# def home():
#     return jsonify(20+10)

# call_obj = app.route("/")
# root = call_obj(root)


if __name__ == "__main__":
    app.run(debug=True, use_reloader=True)