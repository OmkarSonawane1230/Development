while True:
    q=input("You: ").lower()
    if "hi" in q: print("Bot: Hello")
    elif "name" in q: print("Bot: Chatbot")
    elif "bye" in q: print("Bot: Bye"); break
    else: print("Bot: ?")
