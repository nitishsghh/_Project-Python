import nltk
import random
from nltk.chat.util import Chat, reflections

# Define some patterns and responses
patterns = [
    (r'hi|hello|hey', ['Hello!', 'Hey there!', 'Hi!']),
    (r'how are you?', ["I'm doing well, thank you!", "I'm great, thanks for asking."]),
    (r'what is your name?', ["I'm a chatbot.", "You can call me Chatbot."]),
    (r'(.*) your name?', ["My name is Chatbot.", "I'm known as Chatbot."]),
    (r'(.*) (age|old) are you?', ["I don't have an age.", "I'm just a computer program."]),
    (r'what can you do\?', ["I can chat with you.", "I'm here to answer your questions."]),
    (r'quit', ["Goodbye!", "Bye!"]),
]

# Create a chatbot
chatbot = Chat(patterns, reflections)

# Start the conversation
print("Hello! I'm Chatbot. How can I help you today?")

while True:
    user_input = input("> ")
    response = chatbot.respond(user_input)
    print(response)
    if user_input.lower() == 'quit':
        break
