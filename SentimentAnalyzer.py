from textblob import TextBlob

def analyze_sentiment(text):
    
    blob = TextBlob(text)
    
    sentiment = blob.sentiment.polarity
    return sentiment

def main():
    print("Welcome to the EmotionInsights Analyzer!")
    user_input = input("Enter a sentence to analyze: ")

    sentiment = analyze_sentiment(user_input)

    if sentiment > 0:
        print("The sentiment of the input text is Positive.")
    elif sentiment < 0:
        print("The sentiment of the input text is Negative.")
    else:
        print("The sentiment of the input text is Neutral.")

if __name__ == "__main__":
    main()
