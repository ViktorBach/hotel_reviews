from flask import Flask, jsonify, request
from services.guests import fetch_guests, create_review, delete_review

app = Flask(__name__)

@app.route('/guests')
def get_guests():
    return jsonify(fetch_guests())

@app.route('/guests/<int:id>')
def get_guest(id):
    return jsonify([guest for guest in fetch_guests() if guest['guestID'] == id])


app.run(host='0.0.0.0', port=5005)