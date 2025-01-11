from flask import Flask, request, jsonify

app = Flask(__name__)

books = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925, "status": "available"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960, "status": "available"},
    {"id": 3, "title": "1984", "author": "George Orwell", "year": 1949, "status": "checked out"}
]

@app.route('/api/books', methods=['POST'])
def add_book():
    new_book = request.get_json()
    new_book["id"] = len(books) + 1
    new_book["status"] = "available"  
    books.append(new_book)
    return jsonify(new_book), 201

@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify(books)


@app.route('/api/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((item for item in books if item["id"] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({"error": "Book not found"}), 404

@app.route('/api/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((item for item in books if item["id"] == book_id), None)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    updates = request.get_json()
    book.update(updates)
    return jsonify(book)

@app.route('/api/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [item for item in books if item["id"] != book_id]
    return jsonify({"message": "Book deleted"}), 200

@app.route('/api/search', methods=['GET'])
def search_books():
    query = request.args.get('query')
    if not query:
        return jsonify({"error": "Query parameter is required"}), 400
    results = [book for book in books if query.lower() in book["title"].lower() or query.lower() in book["author"].lower()]
    return jsonify(results)

@app.route('/api/checkout/<int:book_id>', methods=['POST'])
def checkout_book(book_id):
    book = next((item for item in books if item["id"] == book_id), None)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    if book["status"] == "checked out":
        return jsonify({"error": "Book is already checked out"}), 400
    book["status"] = "checked out"
    return jsonify({"message": "Book checked out", "book": book})

@app.route('/api/return/<int:book_id>', methods=['POST'])
def return_book(book_id):
    book = next((item for item in books if item["id"] == book_id), None)
    if not book:
        return jsonify({"error": "Book not found"}), 404
    if book["status"] == "available":
        return jsonify({"error": "Book is already available"}), 400
    book["status"] = "available"
    return jsonify({"message": "Book returned", "book": book})

if __name__ == '__main__':
    app.run(debug=True)
