def chat_with_user():
    """A simple chatbot that responds to user input"""
    
    # Welcome message
    print("Chatbot: Hello! I'm a friendly chatbot. Type 'bye' to exit.")
    print("-" * 50)
    
    # Keep chatting until user says bye
    while True:
        # Get user input
        user_input = input("You: ").lower()  # Convert to lowercase for easier matching
        
        # Check what the user said and respond accordingly
        if user_input == "bye" or user_input == "exit" or user_input == "quit":
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        elif user_input == "hello" or user_input == "hi" or user_input == "hey":
            print("Chatbot: Hello there! How are you doing today?")
        
        elif user_input == "how are you" or user_input == "how are you?":
            print("Chatbot: I'm doing great, thank you for asking! How about you?")
        
        elif user_input == "what is your name" or user_input == "what is your name?":
            print("Chatbot: My name is ChatBot! Nice to meet you!")
        
        elif user_input == "help":
            print("Chatbot: I can respond to greetings, tell you my name, and chat with you!")
            print("         Try saying: hello, how are you, what is your name, or bye")
        
        elif user_input == "":
            print("Chatbot: You didn't say anything. Please type something!")
        
        else:
            print(f"Chatbot: You said '{user_input}'. That's interesting! Tell me more!")


# Run the chatbot
if __name__ == "__main__":
    chat_with_user()
