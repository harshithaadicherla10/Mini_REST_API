from flask import Flask, jsonify, request

app = Flask(__name__)

# ==================================================
# In-Memory Database (List of Dictionaries)
# ==================================================
books = [
    {"id": 1, "title": "Python Basics"},
    {"id": 2, "title": "Flask for Beginners"}
]

# ==================================================
# Home Route
# ==================================================
@app.route('/')
def home():
    return "Mini REST API for Book Management"

# ==================================================
# GET - All Books
# ==================================================
@app.route('/books', methods=['GET'])
def get_all_books():
    return jsonify(books), 200

# ==================================================
# GET - Book by ID
# ==================================================
@app.route('/books/<int:book_id>', methods=['GET'])
def get_book_by_id(book_id):
    book = next((b for b in books if b["id"] == book_id), None)

    if not book:
        return jsonify({"error": "Book not found"}), 404

    return jsonify(book), 200

# ==================================================
# POST - Add New Book
# ==================================================
@app.route('/books', methods=['POST'])
def add_book():
    data = request.get_json()

    if not data or "title" not in data:
        return jsonify({"error": "Book title is required"}), 400

    new_id = books[-1]["id"] + 1 if books else 1
    new_book = {
        "id": new_id,
        "title": data["title"]
    }

    books.append(new_book)
    return jsonify(new_book), 201

# ==================================================
# PUT - Update Book by ID
# ==================================================
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    data = request.get_json()
    book = next((b for b in books if b["id"] == book_id), None)

    if not book:
        return jsonify({"error": "Book not found"}), 404

    if "title" in data:
        book["title"] = data["title"]

    return jsonify(book), 200

# ==================================================
# DELETE - Remove Book by ID
# ==================================================
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = next((b for b in books if b["id"] == book_id), None)

    if not book:
        return jsonify({"error": "Book not found"}), 404

    books.remove(book)
    return jsonify({"message": "Book deleted successfully"}), 200

# ==================================================
# Run Application
# ==================================================
if __name__ == '__main__':
    app.run(debug=True)
