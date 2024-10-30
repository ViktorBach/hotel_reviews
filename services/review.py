import json
import sqlite3

############   Database connection function   ##########

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

############   Fetch the guest data   ##########

def fetch_review():
    # load json data from local file 
    with open('json_db.json', 'r') as f:
        full_data = json.load(f)


        reviews = full_data if isinstance(full_data, list) else full_data.get('review', [])

        # filtering and transforming the guest data
        filstered_reviews = [
            {
                "guestID": review["GuestID"],
                "rating": review["Rating"],
                "comment": review["Comment"],
                "date": review["Date"]
            }
            for review in reviews
        ]

        return filstered_reviews
    return []

#fetch and print the filtered guest data
review_data = fetch_review()
print(review_data)

############   Create new guest data   ##########

def create_review(data):
    # Extract data fields from the request
    guestID = data.get("GuestID")
    rating = data.get("Rating")
    comment = data.get("Comment")
    date = data.get("Date")

    # Verify that mandatory fields are present
    if not guestID or not rating or not date:
        return {"error": "guestID, rating, and date are required fields"}, 400

    # Insert data into the database
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        '''
        INSERT INTO Review (GuestID, Rating, Comment, Date) 
        VALUES (?, ?, ?, ?)
        ''',
        (guestID, rating, comment, date)
    )
    conn.commit()
    review_id = cursor.lastrowid
    conn.close()

    # Return confirmation with the new guest's ID
    return {"message": "Review created successfully", "reviewID": review_id}, 201


############   Delete guest    ##########

def delete_review(review_id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        'DELETE FROM Review where ReviewID = ?',
        (review_id,)
    )
    conn.commit()
    conn.close()

    if cursor.rowcount == 0:
        return {"error": "Review not found"}, 404
    
    # return confirmation of successful removel
    return {"message": "Review deleted successfully"}, 200
