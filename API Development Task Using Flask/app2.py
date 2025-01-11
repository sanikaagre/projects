from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

books = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "year": 1925, "status": "available"},
    {"id": 2, "title": "To Kill a Mockingbird", "author": "Harper Lee", "year": 1960, "status": "available"},
    {"id": 3, "title": "1984", "author": "George Orwell", "year": 1949, "status": "checked out"}
]

@app.route('/')
def index():
    return render_template('frontend.html', books=books)

@app.route('/api/books', methods=['GET'])
def get_books():
    return jsonify(books)


if __name__ == '__main__':
    app.run(debug=True)
