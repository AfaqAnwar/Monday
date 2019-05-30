from Rennon._deployment import modified_inference
import string
import random
import requests, json

greetings_unformated = ["hello", "hi", "yo", "what up", "whats up"]
greetings_formatted = ["Hello!", "Hi", "Yo!", "What's up?", "Hey...", "How are you doing?"]

"""
Rules to help supplement Monday with conversing with the user.
@Author Afaq Anwar
@Version 05/30/2019
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
    elif "your name" in modified_input:
        return "My name is Monday. I'm just a chatbot."
    elif "about yourself" in modified_input:
        return "Monday here, I'm a chatbot built with Tensorflow, I'm not that smart so take it easy for now please."
    elif "show" in modified_input:
        if "picture" in modified_input:
            return ""
        elif "meme" in modified_input:
            json_request = requests.get("https://meme-api.herokuapp.com/gimme")
            data = json_request.json()
            return data['url']
    else:
        result = modified_inference.inference(user_input)
        best_idx = result.get("best_index")
        return str(result.get("answers")[best_idx])
