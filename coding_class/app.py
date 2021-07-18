from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/new")
def home() :
    return render_template("index_1.html")
@app.route("/best")
def best_movie() :
    return render_template("best_movie_1.html")
@app.route("/best_tv")
def best_tv() :
    return render_template("best_tv_1.html")
@app.route("/detail/<int:movie_id>")
def detail() :
    return render_template("detail_1.html")


if __name__ == '__main__' :
    app.run(debug=True)