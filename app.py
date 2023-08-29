from flask import Flask, render_template
import pandas as pd
from bs4 import BeautifulSoup

app = Flask(__name__)

@app.route('/')
def home():
    # Load your data
    # data = pd.read_csv('your_data.csv')
    
    # Transform your data
    # data = transform_data(data)
    
    # Render HTML content
    # html_content = render_html(data)
    
    # For this example, I will just use some dummy data and HTML content
    data = {'Name': ['John', 'Anna', 'Peter', 'Linda'],
            'Age': [28, 22, 35, 32]}
    df = pd.DataFrame(data)
    html_content = "<html><body><h1>Hello, World!</h1></body></html>"
    
    # Parse the HTML content
    soup = BeautifulSoup(html_content, 'html.parser')
    
    return render_template('index.html', table=df.to_html(classes='data'), html_content=soup.prettify())

# Function to transform your data
def transform_data(data):
    # Your transformation code here
    return data

# Function to render HTML content
def render_html(data):
    # Your rendering code here
    return '<html></html>'

if __name__ == '__main__':
    app.run(debug=True)
