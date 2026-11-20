
from flask import Flask

# Create the Flask application
app = Flask(__name__)

# Home page
@app.route("/")
def home():
    return """
    <h1>TraceGuard AI</h1>
    <p>AI-Powered Security Log Analyzer</p>
    <p>Our application is running successfully!</p>
    """

# Start the development server
if __name__ == "__main__":
    app.run(debug=True)
