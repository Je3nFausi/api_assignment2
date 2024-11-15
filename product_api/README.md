Product API with Flask

This project demonstrates a simple REST API for managing products built with Flask in Python.

Setting Up the Environment:


Create a Virtual Environment (Optional):

It's recommended to create a virtual environment to isolate project dependencies.
Use .venv module:
python -m venv .venv


Activate the virtual environment:
Windows: .venv\Scripts\activate
Linux/macOS: source venv/bin/activate
Install Flask:

Within your virtual environment (if activated) or your main environment, run:
pip install Flask


Running the API Server:

Navigate to Project Directory:

Open your terminal and navigate to the directory containing your project files (e.g., product_api).
Start the Server:

Run the following command:
python app.py


This will start the Flask development server, typically accessible at http://127.0.0.1:5000/ by default (check the console output for the exact URL).
Testing the API Endpoints:

Option 1: Manually using tools like Postman or curl

Postman:

Install Postman (https://www.postman.com/).
Create a POST request to http://127.0.0.1:5000/products with a JSON body containing product data (e.g., name, description, price).
Send the request and observe the response. You should receive a 201 Created status code for successful creation.
You can also create a GET request to http://127.0.0.1:5000/products to retrieve all products.
curl:

Open your terminal.
Send a POST request with JSON data:
Bash
curl -X POST http://127.0.0.1:5000/products -H "Content-Type: application/json" -d '{"name": "Headphones", "description": "Noise-canceling headphones", "price": 199.99}'
Use code with caution.

Send a GET request to retrieve all products:
curl http://127.0.0.1:5000/products


Option 2: Running the provided client.py script

Run the Script:

In your terminal, within the project directory, run:
python client.py


Observe the Output:

The script will attempt to create a new product and then retrieve all products, printing the results to the console.
Uploading the Project to a GitHub Repository:

Create a GitHub Repository:

Create a new repository on GitHub (https://github.com/).
Version Control (Git):

Initialize a Git repository in your project directory:
git init


Add all files:
git add .


Commit the changes:
git commit -m "Initial commit"


Push to GitHub:

Add the remote repository URL:
git remote add origin <your_github_repo_url>


Push your local commits to the remote repository:
git push -u origin main


Additional Notes:

Replace placeholders like <your_github_repo_url> with your actual information.
This is a basic setup; consider error handling, authentication, and database integration for production use.
This README.md file should provide a comprehensive guide for setting up, running, and testing your product API project.






