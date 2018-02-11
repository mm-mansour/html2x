import os
from flask import Flask, request, send_from_directory, redirect, url_for
import flask

app = Flask(__name__)

print(flask.__version__)


@app.route("/", methods=["GET"])
def process_file():
    os.system("killall firefox")

    params = request.args.to_dict(flat=True)
    link = params["link"]
    extension = params.get("extension", "png")
    wh = params.get("wh", None)

    if wh is None:
        os.system("/usr/bin/firefox -headless -screenshot downloads/output.png {}".format(link))
    else:
        print("here")
        os.system("/usr/bin/firefox -headless -screenshot downloads/output.png {} --window-size={}".format(link, wh))

    if extension != "png":
        os.system("convert downloads/output.png downloads/output.{}".format(extension))

    return redirect(url_for("serve_file", filename="output.{}".format(extension)))


@app.route("/downloads/<filename>")
def serve_file(filename):
    return send_from_directory("./downloads/", filename)


@app.route("/hello")
def hello_world():
    return "Hello, Docker!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7000, threaded=True)
