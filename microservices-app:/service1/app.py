from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify( "Welcome to the TEAM{CloudPal Dev!!!}")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)  # Ensure the port matches the one you expose
