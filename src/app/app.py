from flask import Flask, render_template, redirect, url_for


app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/libs/<path:path>")
def redirect_js_imports(path):
    print(path)
    if path.find("2") != -1:
        new_path = "libqi-js/libs/qi/2/qi.js"
    else:
        new_path = "libqi-js/libs/" + path

    return redirect(url_for("static", filename=new_path))


if __name__ == "__main__":
    # disable browser caching
    app.config["SEND_FILE_MAX_AGE_DEFAULT"] = 0
    app.run(debug=True, host="0.0.0.0", port=80)
