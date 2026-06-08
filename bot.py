# ============================================
# Project 1 : Rule-Based AI Chatbot
# DecodeLabs Industrial Training - Batch 2026
# ============================================

# STEP 1 - THE KNOWLEDGE BASE (Dictionary)

responses = {
    "hello"         : "Hey there! How can I help you?",
    "hi"            : "Hi! Good to see you!",
    "how are you"   : "I am just a bot, but I am doing great!",
    "what is your name" : "I am RuleBot, your simple AI assistant!",
    "what can you do"   : "I can answer simple questions based on my rules!",
    "bye"           : "Goodbye! Have a great day!",
    "good morning"  : "Good Morning! Hope you have a wonderful day!",
    "good night"    : "Good Night! Sleep well!",
    "thanks"        : "You are welcome!",
    "help"          : "You can ask me greetings or simple questions!"
}


# STEP 2 - STARTING THE CHATBOT
print("============================================")
print("        Welcome! I am RuleBot 🤖            ")
print("   Type 'exit' anytime to stop chatting    ")
print("============================================")
print()


# STEP 3 - THE INFINITE LOOP (Heartbeat of the chatbot)

while True:

    # STEP 4 - TAKE INPUT FROM USER & SANITIZE IT

    user_input = input("You: ").lower().strip()


    # STEP 5 - EXIT STRATEGY

    if user_input == "exit":
        print("Bot: Goodbye! See you next time!")
        break


    # STEP 6 - DICTIONARY LOOKUP USING .get()

    reply = responses.get(user_input, "I don't understand that. Type 'help' to see what I can do!")


    # STEP 7 - PRINT THE REPLY
    print("Bot:", reply)