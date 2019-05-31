from Rennon._deployment import modified_inference
import string
import random
import requests, json
from google import google

greetings_unformated = ["hello", "hi", "yo", "what up", "whats up"]
greetings_formatted = ["Hello!", "Hi", "Yo!", "What's up?", "Hey...", "How are you doing?"]
picture_api = ['https://aws.random.cat/meow', "https://random.dog/woof.json", "http://shibe.online/api/shibes?count=10&urls=true&httpsUrls=true", "https://randomfox.ca/floof/"]
fact_api = "http://randomuselessfact.appspot.com/random.json?language=en"
"""
Rules to help supplement Monday with conversing with the user.
@Author Afaq Anwar
@Version 05/31/2019
"""


def get_response(user_input):
    modified_input = user_input.translate(str.maketrans('', '', string.punctuation))
    modified_input = modified_input.lower()
    # Checks to see if the user might want Monday to show them an image.
    if "show" in modified_input:
        if "picture" in modified_input or "image" in modified_input or "photo" in modified_input or "gif" in modified_input:
            choice = random.choice(picture_api)
            json_request = requests.get(choice)
            data = json_request.json()
            if choice is picture_api[0]:
                return data['file']
            elif choice is picture_api[1]:
                return data['url']
            elif choice is picture_api[2]:
                return random.choice(data)
            elif choice is picture_api[3]:
                return data['image']
        elif "meme" in modified_input:
            json_request = requests.get("https://meme-api.herokuapp.com/gimme")
            data = json_request.json()
            return data['url']
    # Checks to see if the user wants random facts.
    if "tell" in modified_input:
        if "fact" in modified_input:
            json_request = requests.get(fact_api)
            data = json_request.json()
            return data['text']
    # Allows monday to query a vast array of topics using Wikipedia and Google.
    if "tell" in modified_input or "who is" in modified_input or "what is" in modified_input:
        obj_index = len(modified_input)
        if "tell" in modified_input and "more about" in modified_input or "tell" in modified_input and "about" in modified_input:
            obj_index = modified_input.index("about") + 5
        elif "who is" in modified_input or "what is":
            obj_index = modified_input.index("is") + 2
        if obj_index < len(modified_input):
            query = modified_input[obj_index:]
            search_results = google.search(query, 1)
            for result in search_results:
                if "wikipedia" in result.link:
                    return result.description + "</br>" + "To read more visit the following link" + "</br>" + result.link
        else:
            return "I was not able to find anything about that."
    # Rules to help supplement the conversation and keep some information concrete.
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
    elif "help me" in modified_input:
        return "I'm not exactly sure what I can do..."
    else:
        result = modified_inference.inference(user_input)
        best_idx = result.get("best_index")
        return str(result.get("answers")[best_idx])


