# --------------------------------------------
# Task 4 (Extended): Smart Rule-Based Chatbot
# --------------------------------------------

import datetime
import random

def chatbot_reply(user_input):
    """
    Function to return chatbot's response based on user input.
    Uses simple rule-based logic (if-elif statements).
    """

    # Convert input to lowercase for matching
    user_input = user_input.lower().strip()

    # Greeting responses
    if user_input in ("hi", "hello", "hey"):
        return random.choice(["Hello there! 👋", "Hey! How can I help you?", "Hi! Nice to see you."])
    
    elif "how are you" in user_input:
        return "I'm just a bunch of code, but I'm feeling great! How about you?"
    
    elif "your name" in user_input:
        return "I'm SmartBot 🤖 — your friendly virtual assistant!"
    
    elif "fine" in user_input or "good" in user_input:
        return "Glad to hear that! 😊"

    # Date and Time
    elif "time" in user_input:
        now = datetime.datetime.now().strftime("%I:%M %p")
        return f"The current time is {now}."
    
    elif "date" in user_input:
        today = datetime.date.today().strftime("%B %d, %Y")
        return f"Today's date is {today}."
    
    # Simple jokes
    elif "joke" in user_input:
        jokes = [
            "Why did the computer show up at work late? It had a hard drive! 😂",
            "Why do programmers hate nature? It has too many bugs! 🐞",
            "What do you call a fish that programs? A cod-er! 🐟"
        ]
        return random.choice(jokes)

    # Simple math support
    elif "add" in user_input or "sum" in user_input:
        try:
            nums = [int(s) for s in user_input.split() if s.isdigit()]
            if len(nums) >= 2:
                return f"The sum is {sum(nums)}."
            else:
                return "Please provide at least two numbers to add."
        except:
            return "Sorry, I couldn’t calculate that."

    elif "weather" in user_input:
        return "I can't fetch real weather data, but I hope it's sunny and bright where you are! ☀️"

    # Small talk
    elif "thank" in user_input:
        return "You're welcome! 😊"
    
    elif "who made you" in user_input:
        return "I was created by a Python programmer just like you!"
    
    elif "help" in user_input:
        return "Sure! I can chat, tell jokes, show date/time, do simple math, or just keep you company!"

    # Exit commands
    elif user_input in ("bye", "goodbye", "exit"):
        return "Goodbye! 👋 It was nice chatting with you."
    
    # Default fallback
    else:
        return "Hmm... I didn’t quite get that. Try asking something else!"

# --------------------------------------------
# Main Chat Loop
# --------------------------------------------
print("🤖 SmartBot: Hello! I'm your chat buddy. Type 'help' to know what I can do.")
print("Type 'bye' anytime to end the chat.\n")

while True:
    user_message = input("You: ")
    response = chatbot_reply(user_message)
    print("SmartBot:", response)

    if user_message.lower() in ("bye", "goodbye", "exit"):
        break

print("\n💬 Chat ended. Have a great day!")
