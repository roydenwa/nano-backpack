from flask import Flask, render_template, redirect, url_for


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/libs/<path:path>")
def redirect_js_imports():
    return redirect(url_for("static", filename="libqi-js/libs/"+path))


if __name__ == "__main__":
    # disable browser caching
    app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
    app.run(debug=True, host="0.0.0.0")
