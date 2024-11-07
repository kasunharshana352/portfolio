from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
import os

app = Flask(__name__)

# Sample data for the portfolio
projects = [
    {
        "title": "Sentiment Analysis",
        "description": "This web app analyses the comments by using an AI model made by me.",
        "url": "https://87f575bd-2dfe-425d-8461-78b4d47dc328-00-2wz26cdqtdyw8.picard.replit.dev/"
    },
    {
        "title": "Shop System",
        "description": "This web app is a stock management app",
        "url": "https://shop-sys.vercel.app/"
    },
    {
        "title": "Project 3",
        "description": "Description of project 3.",
        "url": "https://example.com/project3"
    }
]

@app.route('/')
def home():
    current_year = datetime.now().year  # Get the current year
    return render_template('index.html', projects=projects, current_year=current_year)

@app.route('/contact', methods=['POST'])
def contact():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']
    # Here you can add functionality to handle the message, like sending an email
    print(f"Message from {name} ({email}): {message}")  # For demonstration
    return redirect(url_for('home'))

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))  # Get port from environment
    app.run(host="0.0.0.0", port=port)  # Bind to 0.0.0.0 for external access
