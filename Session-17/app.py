from flask import Flask, redirect, render_template, jsonify, url_for, request, send_file
from flask_sqlalchemy import SQLAlchemy
from Project_Judge import main
import multiprocessing, os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///submissions.db'
db = SQLAlchemy(app)
test_case_dir = "./Project_Judge/TestCases/"

class Submission(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    result = db.Column(db.PickleType, nullable=False)

    def __repr__(self):
        return "<Submission Id " + str(self.id) + " >"

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "GET":
        return render_template("home.html")
    else:
        f = request.files.get("python")
        id_ = len(Submission.query.all()) + 1
        filename = "./Submissions/" + str(id_) + ".py" 
        f.save(filename)
        args = []
        for test_case_no in os.listdir(test_case_dir):
            root = os.path.join(test_case_dir, test_case_no)
            arg = (filename, os.path.join(root, "input.txt"), os.path.join(root, "correct_output.txt"), test_case_no)
            args.append(arg)
        p = multiprocessing.Pool(2)

        results = p.starmap(main.run, args)
        submission = Submission(id=id_, result=results)
        db.session.add(submission)
        db.session.commit()
        return redirect("/submission/" + str(id_))


@app.route("/submission/<id>")
def result(id):
    if request.args.get("download")  == "True":
        filename = "./Submissions/" + str(id) + ".py" 
        return send_file(filename, as_attachment=True, mimetype="application", attachment_filename="submitted_code.py")
    id = int(id)
    submission = Submission.query.filter_by(id=id).first()
    if submission is None:
        return "No submission found with that Id"
    results = submission.result
    return render_template("results.html", results = results, id=id)


@app.route("/leaderboard")
def leaderboard():
    lb = []
    for row in Submission.query.all():
        score = 0
        for tc in row.result:
            if tc[1] == "Pass":
                score += 100
        lb.append((row.id, score))
    def key(x):
        return -x[1]

    lb = sorted(lb, key=key)
    return render_template("leaderboard.html", lbs=lb)


if __name__ == "__main__":
    app.run()