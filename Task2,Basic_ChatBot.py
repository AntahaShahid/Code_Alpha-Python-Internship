#TASK 2: Basic Chatbot
print("************")

def get_response(user_input):
    user_input = user_input.lower()

    if user_input in ["hello", "hi", "hey"]:
        return "Hi!"
    elif user_input in ["how are you", "how are you doing"]:
        return "I'm fine, thanks!"
    elif user_input in ["bye", "goodbye", "exit"]:
        return "Goodbye!"
    else:
        return "Sorry, I didn't understand that."

def run_chatbot():
    print("Welcome to the chatbot. Type something to begin.")
    print("Type 'bye' or 'exit' to end the conversation.")

    while True:
        user_message = input("You: ")

        response = get_response(user_message)
        print("Bot:", response)

        if response == "Goodbye!":
            break

# Start the chatbot
run_chatbot()
