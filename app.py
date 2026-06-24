from flask import Flask, request, jsonify, send_file
import webbrowser

app = Flask(__name__)

@app.route("/")
def home():
    return send_file("index.html")

@app.route("/submit", methods=["POST"])
def submit():

    data = request.json

    url = data.get("url")

    print("Received URL:", url)

    webbrowser.open_new(url)

    return jsonify({
        "message": "Browser opened successfully!"
    })

if __name__ == "__main__":
    app.run(debug=True)