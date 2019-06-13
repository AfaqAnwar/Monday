import _deployment.inference
import string
import re
import random
import requests
from google import google
import urllib.parse

greetings_unformatted = ["hello", "hi", "yo", "what up", "whats up"]
greetings_formatted = ["Hello!", "Hi", "Yo!", "What's up?", "Hey...", "How are you doing?"]
goodbyes = ["Bye", "Bye!", "Bye Bye!", "See you later.", "Talk to you later!", "Take it easy.", "It was nice talking to you, so long."]
error_phrases = ["I can't seem to understand you.", "I have no clue what you're talking about...", "You want to try that again?", "?", "I'm sorry, that makes no sense."]
picture_api = ['https://aws.random.cat/meow', "https://random.dog/woof.json", "http://shibe.online/api/shibes?count=10&urls=true&httpsUrls=true", "https://randomfox.ca/floof/"]
fact_api = "http://randomuselessfact.appspot.com/random.json?language=en"
calculator_api = "http://api.mathjs.org/v4/?expr="

"""
Allows Rennon to generate a response to various inputs using a combination of rules and Machine Learning.
@Author Afaq Anwar
@Version 06/13/2019
"""


def get_response(user_input):
    # Avoids invalid input with no legitimate characters.
    letters_found = re.search('[a-zA-Z]', user_input)
    unwanted_characters = re.search(r'[^\x00-\x7f]', user_input)

    if not letters_found or unwanted_characters:
        return random.choice(error_phrases)
    
    modified_input = user_input.translate(str.maketrans('', '', no_punctuation_besides_math()))
    modified_input = modified_input.lower()
   
    # Avoids invalid input that is too short.
    if len(modified_input) <= 1:
        return random.choice(error_phrases)
    
    # Rules to help supplement the conversation and keep some information concrete.
    if modified_input in greetings_unformatted:
        return random.choice(greetings_formatted)
    elif "bye" in modified_input:
        return random.choice(goodbyes)
    elif "who" in modified_input and modified_input.endswith("are you"):
        return "I'm Rennon, a chatbot. No I'm not sentient, maybe I will be, who knows..."
    elif "who is" in modified_input and modified_input.endswith("Rennon"):
        return "I'm Rennon!"
    elif "who" in modified_input and modified_input.endswith("made you"):
        return "I was made by Afaq Anwar, a 17 year old Computer Science student."
    elif "your name" in modified_input:
        return "My name is Rennon. I'm just a chatbot."
    elif "about yourself" in modified_input:
        return "Rennon here! I'm just a chatbot, I can look up information, do math, and talk to you!"
    elif "help me" in modified_input:
        return "I'm not exactly sure what I can do..."

    # Checks to see if the user might want Rennon to show them an image.
    if "show" in modified_input or "download" in modified_input or "bring up" in modified_input:
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
    if "tell" in modified_input or "give me" in modified_input:
        if "fact" in modified_input:
            json_request = requests.get(fact_api)
            data = json_request.json()
            return data['text']

    # Checks to see if the user wanted to make a calculation.
    query = modified_input
    if "what is" in modified_input:
        query = modified_input[modified_input.index("is") + 3:].replace(" ", "")
    if math_check(query):
        url_encoded_request = urllib.parse.quote(query)
        request = requests.get(calculator_api + url_encoded_request)
        data = query + " = " + request.text
        return data

    # Allows Rennon to query a vast array of topics using Wikipedia and Google.
    if modified_input.endswith("is"):
        if "who" in modified_input:
            # Note the query is one index behind the theoretical start of the subject, this is to account for spacing errors.
            query = modified_input[modified_input.index("who") + 3: len(modified_input) - 2]
            return obtain_information(query)
        elif "what" in modified_input:
            query = modified_input[modified_input.index("what") + 4: len(modified_input) - 2]
            return obtain_information(query)

    if "tell" in modified_input or "who is" in modified_input or "what is" in modified_input:
        obj_index = len(modified_input)
        if "tell" in modified_input and "more about" in modified_input or "tell" in modified_input and "about" in modified_input:
            obj_index = modified_input.index("about") + 5
        elif "who is" in modified_input or "what is" in modified_input and not math_check(modified_input[modified_input.index("is") + 2:].replace(" ", "")):
            obj_index = modified_input.index("is") + 2
        if obj_index < len(modified_input):
            query = modified_input[obj_index:]
            return obtain_information(query)

    response = _deployment.inference.inference(user_input)
    best_answer_index = response["best_index"]
    return response.get("answers")[best_answer_index]


# Checks to see if a string is an arithmetic operation.
def math_check(user_input):
    is_math = True
    for i in user_input:
        if i not in ['+', '-', '*', '%', '.', '/'] and not i.isdigit():
            return False
    return is_math


# Returns a string without all punctuation besides arithmetic operators.
def no_punctuation_besides_math():
    custom_punctuation = string.punctuation
    for c in custom_punctuation:
        if c in ['+', '-', '*', '%', '.', '/']:
            custom_punctuation = custom_punctuation.replace(c, "")
    return custom_punctuation


# Obtains information from Wikipedia through a Google search.
def obtain_information(query):
    # Searches the first 3 pages.
    search_results = google.search(query, 3)
    for result in search_results:
        if "wikipedia" in result.link:
            return result.description + "</br>" + "</br> You can find more information from the " + "<a href=" + result.link + " target='_blank'>" + "source" + "</a>."
    return "I was not able to find anything about that."
