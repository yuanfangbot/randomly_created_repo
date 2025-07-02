from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to the API Service",
        "status": "OK"
    })

@app.route('/data')
def get_data():
    data = {
        "id": 1,
        "name": "Sample Data",
        "description": "This is a sample API response."
    }
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)