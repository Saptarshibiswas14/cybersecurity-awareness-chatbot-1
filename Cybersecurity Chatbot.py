cybersecurity_faq = {
    "what is phishing": "Phishing is when attackers trick you to reveal personal information. Always verify links!",
    "how to create strong password": "Use 12+ characters with upper/lowercase, numbers, and special symbols.",
    "what is 2fa": "Two-Factor Authentication adds an extra verification step after your password.",
    "tips for safe browsing": "Check for HTTPS, don't click suspicious links, update your software regularly."
}
def chatbot_response(user_input):
    user_input = user_input.lower()
    for key in cybersecurity_faq:
        if key in user_input:
            return cybersecurity_faq[key]
    return "I'm sorry, I don't have information about that. Please try another cybersecurity topic!"

while True:
    user_input = input("You: ")
    if user_input.lower() in ['exit', 'quit']:
        print("Bot: Stay safe! Goodbye. 👋")
        break
    response = chatbot_response(user_input)
    print(f"Bot: {response}")
