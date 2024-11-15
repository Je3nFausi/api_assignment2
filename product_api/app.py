from flask import Flask, request, jsonify
from models import Product  # Import Product class

app = Flask(__name__)

# In-memory product list (replace with database later)
products = []

@app.route('/products', methods=['GET', 'POST'])
def products_handler():
    if request.method == 'GET':
        # Get all products
        return jsonify([p.__dict__ for p in products])

    elif request.method == 'POST':
        # Create a new product
        try:
            data = request.get_json()
            new_product = Product(data['name'], data['description'], data['price'])
            products.append(new_product)
            return jsonify(new_product.__dict__), 201  # Created
        except (KeyError, TypeError):
            return jsonify({'error': 'Invalid product data'}), 400  # Bad Request

if __name__ == '__main__':
    app.run(debug=True)
#This code defines two endpoints:
#/products (GET): Retrieves a list of all products in JSON format.
#/products (POST): Accepts a JSON object containing product data and creates a new product. It validates the data and returns appropriate status codes (201 for success, 400 for errors).
