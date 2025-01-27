from flask import Flask, request, jsonify, render_template
import nltk
from nltk.chat.util import Chat, reflections

# Download NLTK data
nltk.download('punkt')

# Define chatbot responses
pairs = [
    [
        r"hi|hello|hey",
        ["Hello! How can I assist you today?", "Hi there! How can I help you?"]
    ],
    [
        r"what is your name?",
        ["I am a customer support chatbot. You can call me ChatBot!"]
    ],
    [
        r"how are you?",
        ["I'm just a bot, but I'm here to help you!"]
    ],
    [
        r"what can you do?",
        ["I can answer your questions about our products, services, and more. Just ask!"]
    ],
    [
        r"thank you|thanks",
        ["You're welcome!", "Glad to help!"]
    ],
    [
        r"bye|goodbye",
        ["Goodbye! Have a great day!", "Bye! Feel free to come back anytime."]
    ],
    [
        r"(.*) (price|cost) (.*)",
        ["For pricing information, please visit our website or contact our sales team."]
    ],
    [
        r"(.*) (support|help) (.*)",
        ["Our support team is available 24/7. Please visit our support page or email us at support@example.com."]
    ],
    [
        r"(.*)",
        ["I'm sorry, I didn't understand that. Can you please rephrase your question?"]
    ]
]

# Initialize the chatbot
chatbot = Chat(pairs, reflections)

# Create Flask app
app = Flask(__name__)

# Serve the HTML frontend
@app.route('/')
def home():
    return render_template('index.html')

# Handle chatbot interactions
@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')  # Get user input from the request
    response = chatbot.respond(user_input)    # Get chatbot response
    return jsonify({'response': response})    # Return response as JSON

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)