import socket
from flask import flask.jsonify
app_port = 5000

hostname = socket.gethostname()

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(
        msg = "Hello, Container Hostname is: "+ hostname + "on port: " + str(app_port)
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(app_port), debug=True)
