# hotel_reviews

Hotel reviews service allows users living at Hotel Kong Arthur to create and delete reviews about the hotel

To run the service create and run a virtual environment

python3 -m venv .venv
source .venv/bin/activate

run the app
python3 app.py


Api endpoints:

'/reviews' Method = GET
fetches all reviews and posts them when using postman

'/reviews/guest/<int:guest_id>' Method = GET
Fetches reviews filtered by a guest id

'/reviews/<int:id>' Method = GET
Fetches reviews filtered by a review id

'/review' Method = POST
Creates a new review

'/review/<int:review_id>' Method DELETE
Deletes a review based on a specific review id
