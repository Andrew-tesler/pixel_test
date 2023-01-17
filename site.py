from flask import Flask, render_template, make_response

app = Flask(__name__)

@app.route("/")
def index():
    html = "<!DOCTYPE html><html><head><title>IT Support</title></head><body><h1>No IT support until 40!!</h1></body></html>"
    return make_response(html)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
