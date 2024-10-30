from flask import Flask, jsonify, request
from services.review import fetch_review, create_review, delete_review

app = Flask(__name__)


########### CRUD method GET ############

@app.route('/reviews', methods=['GET'])
def get_all_reviews():
    reviews = fetch_review()
    return jsonify(reviews)

@app.route('/reviews/guest/<int:guest_id>', methods=['GET'])
def get_review(guest_id):
    reviews = fetch_review()
    return jsonify([review for review in reviews if review['guestID'] == id])

@app.route('/reviews/<int:id>', methods=['GET'])
def get_review(id):
    reviews = fetch_review()
    return jsonify([review for review in reviews if review['reviewID'] == id])

########### CRUD method Post ############

@app.route('/review', methods=['POST'])
def add_review():
    data = request.get_json()
    if not data:
        return jsonify({"error": "Invalid json data"}), 400
    
    result, status_code = create_review(data)
    return jsonify(result), status_code


########### CRUD method DELETE ############

@app.route('/review/<int:review_id>', methods=['DELETE'])
def remove_review(review_id):
    result, status_code = delete_review(review_id)
    return jsonify(result), status_code


app.run(host='0.0.0.0', port=6000)