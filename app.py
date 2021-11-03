from flask import Flask, request
import os

app = Flask(__name__)
basedir = os.getcwd()


@app.route("/upload", methods=["POST"])
def upload():
    path = request.args.get("path")
    data = request.data
    path = basedir + path
    if not os.path.exists(path):
        os.makedirs(path)
    with open(f"{path}/{filename}.{ext}", "wb") as f:
        f.write(data)
    return f"http://cdn.al7rbi.tk{path}/{filename}.{ext}"


@app.route("/<path:path>")
def get(path):
    with open("/"+path, "rb") as f:
        return f.read()

@app.route("/")
def home():
    return "<center><h1>Welcome in Alharbi CDN</h1></center>"

@app.route("/favicon.ico")
def dump():
    return ""

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=30)
