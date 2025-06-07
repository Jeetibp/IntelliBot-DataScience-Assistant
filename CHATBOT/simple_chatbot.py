#!/usr/bin/env python3
"""
IntelliBot - Standalone Script Version
Run this script to start the chatbot in console mode
"""

def simple_chatbot():
    """Simple rule-based chatbot for demonstration"""
    responses = {
        "hello": "Hi there! How can I help you today?",
        "hi": "Hello! What can I do for you?",
        "how are you": "I'm doing great! Thanks for asking.",
        "what is your name": "I'm IntelliBot, your AI assistant!",
        "bye": "Goodbye! Have a great day!",
        "thank you": "You're welcome! Happy to help!",
        "help": "I can chat with you and answer questions. Try asking me something!"
    }
    
    print("🤖 IntelliBot Console Version")
    print("Type 'quit' to exit")
    print("-" * 30)
    
    while True:
        user_input = input("You: ").strip().lower()
        
        if user_input in ['quit', 'exit', 'bye']:
            print("Bot: Goodbye! Thanks for chatting!")
            break
        
        # Simple keyword matching
        response = "I'm not sure about that. Can you ask something else?"
        for key, value in responses.items():
            if key in user_input:
                response = value
                break
        
        print(f"Bot: {response}")

if __name__ == "__main__":
    simple_chatbot()
