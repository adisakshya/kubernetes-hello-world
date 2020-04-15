from flask import Flask
app = Flask(__name__)

@app.route('/')
def blog():
    return "Flask in Kubernetes cluster"

if __name__ == '__main__':
    app.run(threaded=True, host='0.0.0.0', port=5000)