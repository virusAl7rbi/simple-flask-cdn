from flask import Flask, request, make_response
import os, mimetypes


app = Flask(__name__)
basedir = os.getcwd()


@app.route("/upload", methods=["POST"])
def upload():
    req_path = request.args.get("path")
    data = request.data
    path = str(basedir + "/" + req_path).rsplit("/",1)[0]+"/"
    if not os.path.exists(req_path):
        os.makedirs(req_path)
    with open('/app/'+req_path, "wb") as f:
        f.write(data)
    return f'http://cdn.al7rbi.cf{req_path}'


@app.route("/<path:path>")
def get(path):
    print(path)
    with open("/app/"+path, "rb") as f:
        r = make_response( f.read())
        r.mimetype = str(mimetypes.guess_type(f"/app/{path}")[0])
        return r

@app.route("/")
def home():
    return "<center><h1>Welcome in Alharbi CDN</h1></center>"

@app.route("/favicon.ico")
def dump():
    return ""

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=30)

