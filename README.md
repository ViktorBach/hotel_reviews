# Review Microservice

This microservice provides a simple way to post and manage user reviews in a database. It’s built with Python and designed to work as a small service with a few core endpoints, making it ideal for integration in larger projects or for learning about microservice architecture.
Features

    REST API endpoints for creating and retrieving reviews.
    Database Integration for storing and retrieving reviews.
    Lightweight and scalable, perfect for integration into broader projects.

## Getting Started
Prerequisites

Make sure you have the following installed:

    Python 3.8+
    Docker
    VSCode with the Remote - Containers extension (recommended for development).

Setup Instructions

    Clone the repository

    bash

git clone https://github.com/your-username/hotel_reviews.git
cd review-microservice

Install dependencies
Set up a virtual environment and install the required packages:

bash

python -m venv venv
source venv/bin/activate   # For Windows, use `venv\Scripts\activate`

Run the application

bash

    python app.py

Api endpoints:

'/reviews' Method = GET
- fetches all reviews and posts them when using postman

'/reviews/guest/<int:guest_id>' Method = GET
- Fetches reviews filtered by a guest id

'/reviews/<int:id>' Method = GET
- Fetches reviews filtered by a review id

'/review' Method = POST
- Creates a new review

'/review/<int:review_id>' Method DELETE
- Deletes a review based on a specific review id

Database

The microservice is backed by a simple database that stores review data. The database schema includes:

    review ID: Unique identifier for each review
    guest ID: Unique id for each guest
    Rating: 1 - 5
    Text: The content of the review
    Date: DD.MM.YYYY
