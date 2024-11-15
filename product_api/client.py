import requests
from models import Product  # Import Product class for data representation

# API endpoint URL (replace with your actual URL)
api_url = 'http://localhost:5000/products'

# Create a new product
new_product = Product('Laptop', 'Powerful laptop for work and play', 899.99)
product_data = new_product.__dict__  # Convert to dictionary for JSON

response = requests.post(api_url, json=product_data)

if response.status_code == 201:
    created_product = Product(**response.json())  # Convert JSON response to Product object
    print(f"Product created: {created_product}")
else:
    print(f"Error creating product: {response.status_code} - {response.text}")

# Get all products
response = requests.get(api_url)

if response.status_code == 200:
    products = [Product(**p) for p in response.json()]  # Convert JSON list to Product objects
    print("Available products:")
    for product in products:
        print(product)
else:
    print(f"Error retrieving products: {response.status_code} - {response.text}")