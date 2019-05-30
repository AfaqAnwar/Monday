from Rennon._deployment import modified_inference
import string
import random

greetings = ["hello", "hi", "yo", "whats up", "what up"]


def get_response(user_input):
    modified_input = user_input.translate(str.maketrans('', '', string.punctuation))
    modified_input = modified_input.lower()

    if modified_input in greetings:
        return random.choice(greetings)
    elif "who" in modified_input and modified_input.endswith("are you"):
        return "I'm Monday, a chatbot. No I'm not sentient, maybe I will be, who knows..."
    elif "who" in modified_input and modified_input.endswith("made you"):
        return "I was made by Afaq Anwar, a 17 year old Computer Science student."
    else:
        result = modified_inference.inference(user_input)
        best_idx = result.get("best_index")
        return str(result.get("answers")[best_idx])
