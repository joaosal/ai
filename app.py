from flask import Flask, request, jsonify, render_template
from vectara import Vectara
import os

app = Flask(__name__)

# Set up Vectara API client
client = Vectara(
    customer_id=os.getenv('CUSTOMER_ID'),    # Replace with your Vectara Customer ID
    #corpus_id='3',        # Replace with your Vectara Corpus ID
    api_key=os.getenv('VECTARA_API_KEY')  # Store your API key in environment variables
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')

    if not user_message:
        return jsonify({'reply': "I didn't receive any message!"})

    # Query Vectara
    response = client.query(3, user_message)

    print(response)

    if response and response.results:
        reply = response.results[0].text
    else:
        reply = "I'm not sure how to respond to that."

    return jsonify({'reply': reply})

if __name__ == '__main__':
    app.run(debug=True)