from flask import Flask, request


app = Flask(__name__)


@app.route("/api/upper/<string:string>", methods=["GET"])
def method_name(string):
    try:
        upper_string = string.upper()
        return {"result": upper_string}, 200
    except:
        return {"result": ""}, 404

@app.route("/api/lower/<string:string>", methods=["GET"])
def method_names(string):
    try:
        lower_string = string.lower()
        return {"result": lower_string}, 200
    except:
        return {"result": ""}, 400