from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Sample data for the portfolio
projects = [
    {
        "title": "Project 1",
        "description": "Description of project 1.",
        "url": "https://example.com/project1"
    },
    {
        "title": "Project 2",
        "description": "Description of project 2.",
        "url": "https://example.com/project2"
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
    app.run(debug=True)
