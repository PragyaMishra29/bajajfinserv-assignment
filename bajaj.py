from flask import Flask, request, jsonify

app = Flask(__name__)

# Helper function to find the highest lowercase alphabet
def find_highest_lowercase(data):
    lowercase_letters = [char for char in data if char.islower()]
    if lowercase_letters:
        return [max(lowercase_letters)]
    return []

# Route for POST request
@app.route('/bfhl', methods=['POST'])
def handle_post():
    try:
        user_data = request.json
        data = user_data.get('data', [])
        
        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]
        highest_lowercase_alphabet = find_highest_lowercase(data)
        
        response = {
            "is_success": True,
            "user_id": "john_doe_17091999",
            "email": "john@xyz.com",
            "roll_number": "ABCD123",
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": highest_lowercase_alphabet
        }
        
        return jsonify(response), 200
    except Exception as e:
        return jsonify({
            "is_success": False,
            "message": str(e)
        }), 400

# Route for GET request
@app.route('/bfhl', methods=['GET'])
def handle_get():
    response = {
        "operation_code": 1
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)
