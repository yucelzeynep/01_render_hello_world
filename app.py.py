# Import the Flask class from the flask module
from flask import Flask

# Create an instance of the Flask class
app = Flask(__name__)

# Define a route for the root URL ("/")
@app.route('/')
def hello():
    # This function will be called when accessing the root URL
    return 'Hello, World!'  # Return a simple string response

# Check if the script is run directly (not imported)
if __name__ == '__main__':
    # Run the application on the local development server
    app.run(host='0.0.0.0', port=5000)  # Accessible from any IP on port 5000