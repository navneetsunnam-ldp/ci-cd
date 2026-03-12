from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "This is CI/CD Demo 2"}

@app.route("/api")
def api():
    return {"status": "API working"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)