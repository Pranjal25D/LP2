# 💬 Elementary Rule-Based Chatbot for Customer Interaction

def chatbot():
    responses = {
        "hi": "Hello! How can I help you today?",
        "hello": "Hi there! What can I assist you with?",
        "store hours": "Our store is open from 9 AM to 9 PM every day.",
        "return policy": "You can return any item within 30 days of purchase.",
        "order status": "Please provide your order ID to check the status.",
        "products available": "We offer a wide range of electronics, clothing, and accessories.",
        "bye": "Thank you for visiting! Have a great day!"
    }

    print("\nWelcome to the Customer Support Chatbot! Type 'exit' to end the chat.")

    while True:
        user_input = input("You: ").lower()
        if user_input == "exit":
            print("Chatbot: Goodbye! 👋")
            break

        found = False
        for key in responses:
            if key in user_input:
                print(f"Chatbot: {responses[key]}")
                found = True
                break

        if not found:
            print("Chatbot: I'm sorry, I didn't understand that. Can you please rephrase?")

# Run the chatbot
chatbot()