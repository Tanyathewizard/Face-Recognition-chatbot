import random
import re
from intent_data import data  # Importing intent keywords and responses

# Function to get a reply based on user input
def get_reply(user_input):
    msg = user_input.lower().strip()

    for category, values in data.items():
        for keyword in values["keywords"]:
            if re.search(r'\b' + re.escape(keyword) + r'\b', msg):
                response = random.choice(values["responses"])
                if category == "exit":
                    return response, True  # Reply and signal to exit
                return response, False  # Reply but continue chat

    return None, False  # No match found, no reply

# Function to start the chatbot conversation
def start_chatbot(user_name):
    print(f"Hello {user_name.capitalize()}, how can I help you today?")
    while True:
        user_input = input("You: ")
        reply, should_exit = get_reply(user_input)

        if reply:
            print("Assistant:", reply)
        else:
            # No reply if input doesn't match any intent
            continue

        if should_exit:
            break
