from Rennon._deployment import modified_inference
import string
import random

greetings_unformated = ["hello", "hi", "yo", "what up", "whats up"]
greetings_formatted = ["Hello!", "Hi", "Yo!", "What's up?", "Hey..."]

"""
Rules to help supplement Monday with conversing with the user.
@Author Afaq Anwar
@Version 05/29/2019
"""


def get_response(user_input):
    modified_input = user_input.translate(str.maketrans('', '', string.punctuation))
    modified_input = modified_input.lower()

    if modified_input in greetings_unformated:
        return random.choice(greetings_formatted)
    elif "who" in modified_input and modified_input.endswith("are you"):
        return "I'm Monday, a chatbot. No I'm not sentient, maybe I will be, who knows..."
    elif "who" in modified_input and modified_input.endswith("made you"):
        return "I was made by Afaq Anwar, a 17 year old Computer Science student."
    else:
        result = modified_inference.inference(user_input)
        best_idx = result.get("best_index")
        return str(result.get("answers")[best_idx])
