from flask import Flask, render_template, request, redirect



app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("form.html", val=False, ans=None)
    else:
        n1 = request.form.get("n1")
        n2 = request.form.get("n2")
        ans = int(n1) + int(n2)
        return render_template("form.html", val=True, ans=ans)
    
# @app.route("/<username>")
# def function(username):
#     return redirect("/")


@app.route("/<n1>/<n2>")
def sum(n1, n2):
    return str(int(n1)+int(n2))

# @app.route("/<path1>/<path2>")
# def function(path1, path2):
#     return path1 + " " + path2

if __name__ == "__main__":
    app.run()