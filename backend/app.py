from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {"message": "CI/CD Kubernetes Demo Running"}

@app.route("/api")
def api():
    return {"status": "API working"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)