

from nltk.chat.util import Chat, reflections

pairs = [
    (r'hi|hello|hey', ['Hello! How can I help you today?']),
    (r'how are you[\?]?', ['I am just a bot, but I am doing great!']),
    (r'what is your name[\?]?', ['I am a chatbot created with NLTK.']),
    (r'bye|goodbye|quit', ['Goodbye! Have a nice day!']),
    (r'(.*) your name[\?]?', ['My name is Chatbot.']),
    (r'who are you[\?]?', ['I am a chatbot created to assist you.']),
    (r'how can I (help|assist) you[\?]?', ['You can ask me questions!']),
    (r'(.*)', ['Sorry, I didn’t quite get that. Can you please rephrase?'])
]

def chatbot():
    print("Hi! I'm a chatbot. Type 'quit', 'bye', or 'goodbye' to exit.")
    chat = Chat(pairs, reflections)
    
    while True:
        try:
            user_input = input("You: ").strip().lower()
            if user_input in ['quit', 'bye', 'goodbye']:
                print("Chatbot: Goodbye! Have a nice day!")
                break
            response = chat.respond(user_input)
            print("Chatbot:", response)
        except (KeyboardInterrupt, EOFError):
            print("\nChatbot: Goodbye! Have a nice day!")
            break

chatbot()




