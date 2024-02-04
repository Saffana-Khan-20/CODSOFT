# Task 1
# Rule Based Chatbot
# Chatbot rules
rules = {
    "What is your name?": "My name is Chatbot.",
    "How are you?": "I'm doing well, thank you!",
    "What is capital of India?": "Capital of India is New Delhi.",
}

# Logic
def chatbot_response(user_input):
    for pattern, response in rules.items():
        if pattern in user_input:
            return response
    return "I'm sorry, I don't understand."

# Testing chatbot
user_input = input("User: ")
chatbot_output = chatbot_response(user_input)
print("Chatbot:", chatbot_output)
