# Simple chatbot in Python

def chatbot_response(user_input):
    # Convert input to lowercase to handle case-insensitive responses
    user_input = user_input.lower()

    # Define responses for common greetings and questions
    if "hello" in user_input or "hi" in user_input:
        return "Hello! How can I assist you today?"
    elif "how are you" in user_input:
        return "I'm just a bot, but I'm here to help! How can I assist you?"
    elif "what is your name" in user_input:
        return "I'm your assistant bot! I don't have a name, but I'm here to help."
    elif "help" in user_input:
        return "I'm here to assist you. You can ask me about simple information, or say 'bye' to end the conversation."
    elif "bye" in user_input:
        return "Goodbye! Have a great day."
    else:
        return "I'm not sure how to respond to that. Could you try asking something else?"

# Main loop for chatting with the bot
print("Welcome to the Chatbot! Type 'bye' to end the conversation.")
while True:
    # Get user input
    user_input = input("You: ")
    
    # Get chatbot response
    response = chatbot_response(user_input)
    print("Bot:", response)
    
    # Exit if the user types 'bye'
    if "bye" in user_input.lower():
        break
