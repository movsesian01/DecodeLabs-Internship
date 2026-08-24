responses = {
    "hello": "Hi there! How can I help you today?",
    "hi": "Hello! What can I do for you?",
    "how are you": "I am doing great! How about you?", 
    "i am fine": "That's good to hear! How can I assist you today?",
    "who are you": "I am a simple rule-based AI chatbot.",
    "what are you": "I am a simple rule-based AI chatbot.",
    "what is your name": "I am a simple rule-based AI chatbot.",
    "who made you": "I was created by Maria Bedros Mosesian as a project for her Decode Labs internship!",
    "what internship are you for": "I was created as a project by Maria Bedros Mosesian for her Decode Labs Artificial Intelligence internship!",
    "who is maria bedros mosesian": "Maria Bedros Mosesian is a student intern at Decode Labs and the creator of this chatbot.",
    "what is decode labs": "Decode Labs is a company that provides training and resources for aspiring software developers and data scientists.",
    "which project are you for": "I was created as the first project by Maria Bedros Mosesian for her Decode Labs Artificial Intelligence internship!",
    "what can you do": "I can answer basic questions, greet you, or chat!",
    "help": "You can greet me, ask who I am, or type 'exit' to quit.",
    "i need help": "You can greet me, ask who I am, or type 'exit' to quit.",
    "what do i do": "You can greet me, ask who I am, or type 'exit' to quit.",
    "can you help me": "You can greet me, ask who I am, or type 'exit' to quit.",
    "what can i do": "You can greet me, ask who I am, or type 'exit' to quit.",
    "thank you": "You're welcome! Is there anything else I can help you with?",
    "how do i use you": "You can greet me, ask who I am, or type 'exit' to quit.",
    "how can i use you": "You can greet me, ask who I am, or type 'exit' to quit.",
    "what time is it": "I am not able to tell the time, but you can check your device's clock.",
    "where are you from": "I was created by Maria Bedros Mosesian as a project for her Decode Labs internship!",
    "where are you located": "I am located in the digital realm, ready to assist you!",
    "where are you": "I am located in the digital realm, ready to assist you!",
    "what is your purpose": "I was created for a Decode Labs internship assignment.I am here to assist you with basic questions and provide information.",
    "what is your function": "I am here to assist you with basic questions and provide information.",
    "what is your role": "I am here to assist you with basic questions and provide information.",
    "how can i leave": "You can type 'exit' or 'quit' to end the conversation.",
    "how can i exit": "You can type 'exit' or 'quit' to end the conversation.",
    "how can i quit": "You can type 'exit' or 'quit' to end the conversation.",
    
}

print("Chatbot Initialized! Type 'exit' or 'quit' to stop.\n")

while True:
    raw_input = input("You: ")
    clean_input = raw_input.lower().strip()
    
    if clean_input in ["exit", "quit", "bye"]:
        print("Chatbot: Goodbye! Have a great day.")
        break
    
    reply = responses.get(clean_input, "I do not understand that. Try asking something else.")
    
    print(f"Chatbot: {reply}\n")