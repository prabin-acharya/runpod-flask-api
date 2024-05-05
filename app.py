from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World! from runpod'

if __name__ == '__main__':
    app.run(host='0.0.0.0')  # Runs on default port 5000 
