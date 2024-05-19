from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return 'Chatbot is running'

@app.route('/chat', methods=['POST'])
def chat():
    # Retrieve user message from the request
    user_message = request.form['message']
    
    # Your chatbot logic goes here
    bot_response = respond_to_message(user_message)
    
    # Return the bot response as JSON
    return jsonify({'response': bot_response})

def respond_to_message(message):
    # Example simple echo bot
    return "You said: " + message

if __name__ == '__main__':
    app.run(debug=True)
