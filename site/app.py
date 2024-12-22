from flask import Flask, render_template, jsonify
import requests

app = Flask(__name__)

# Replace with your NewsAPI key
API_KEY = 'f1ac37cc26c34f28bf560f1b22ab0d3c'
NEWS_URL = "https://newsapi.org/v2/everything?q=cybersecurity&sortBy=publishedAt&apiKey=" + API_KEY

# Expanded historical cyberattacks database
historical_attacks = [
    {"name": "Morris Worm", "year": 1988, "description": "The first-ever worm to spread through the internet, causing widespread disruption."},
    {"name": "ILOVEYOU Virus", "year": 2000, "description": "A computer worm that spread through email and caused billions of dollars in damages."},
    {"name": "Stuxnet", "year": 2010, "description": "A sophisticated cyberattack targeting Iran's nuclear facilities."},
    {"name": "Mirai Botnet", "year": 2016, "description": "A massive DDoS attack caused by infected IoT devices."},
    {"name": "Yahoo Data Breach", "year": 2013, "description": "Over 3 billion accounts compromised in one of the largest data breaches."},
    {"name": "Marriott International Breach", "year": 2018, "description": "Data breach affecting 500 million guests, including sensitive information."},
    {"name": "WannaCry Ransomware", "year": 2017, "description": "Ransomware attack that affected thousands of organizations worldwide."},
    {"name": "SolarWinds Hack", "year": 2020, "description": "A major supply chain attack that affected numerous US government agencies."},
    # Additional attacks can be added here...
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/fetch_news')
def fetch_news():
    try:
        response = requests.get(NEWS_URL)
        if response.status_code == 200:
            news = response.json()
            return jsonify(news['articles'][:50]) # Return top 50 news articles
        else:
            return jsonify({'error': 'Failed to fetch news'}), 500
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/historical_attacks')
def get_historical_attacks():
    return jsonify(historical_attacks)

if __name__ == '__main__':
    app.run(debug=True)
