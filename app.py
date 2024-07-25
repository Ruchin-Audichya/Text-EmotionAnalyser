from flask import Flask, request, jsonify
from flask_cors import CORS
from textblob import TextBlob

app = Flask(__name__)
CORS(app)  

def analyze_sentiment(text):
    blob = TextBlob(text)
    sentiment = blob.sentiment.polarity
    return sentiment

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    text = data.get('text', '')
    sentiment = analyze_sentiment(text)
    
    result = {
        'sentiment': 'Positive' if sentiment > 0 else 'Negative' if sentiment < 0 else 'Neutral',
        'score': sentiment
    }
    
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
