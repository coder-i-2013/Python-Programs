from nltk.chat.util import Chat, reflections

pairs = [
    (r"hello|hi|hey", ["Hi there!", "Hello! How can I assist you?"]),
    (r"how are you", ["I'm just a bunch of code, but I'm functioning perfectly!", "Doing great, thank you!"]),
    (r"(.*) your name", ["I am your friendly chatbot!", "You can call me AI Companion!"]),
    (r"(.*)bad", ["I am sorry to hear that",]),
    (r"(.*)good,great", ["I am glad to hear it",]),
    (r"quit", ["Goodbye! Have a great day!", "Bye! Feel free to chat again anytime!"]),
]

chatbot = Chat(pairs, reflections)


print("Chatbot: Hello! Type 'quit' to end the chat.")
chatbot.converse()