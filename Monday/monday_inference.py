import chatterbot
from chatterbot import ChatBot
import chatterbot.trainers
from chatterbot.trainers import ChatterBotCorpusTrainer

import string
import random
import requests, json
from google import google
import urllib.parse

monday = ChatBot("Monday")

greetings_unformatted = ["hello", "hi", "yo", "what up", "whats up"]
greetings_formatted = ["Hello!", "Hi", "Yo!", "What's up?", "Hey...", "How are you doing?"]
picture_api = ['https://aws.random.cat/meow', "https://random.dog/woof.json", "http://shibe.online/api/shibes?count=10&urls=true&httpsUrls=true", "https://randomfox.ca/floof/"]
fact_api = "http://randomuselessfact.appspot.com/random.json?language=en"
calculator_api = "http://api.mathjs.org/v4/?expr="
"""
Rules to help supplement Monday with conversing with the user.
@Author Afaq Anwar
@Version 05/31/2019
"""


def initialize_monday():
    trainer = ChatterBotCorpusTrainer(monday)
    trainer.train(
        "chatterbot.corpus.english"
    )


def get_response(user_input):
    modified_input = user_input.translate(str.maketrans('', '', no_punctuation_besides_math()))
    modified_input = modified_input.lower()

    # Rules to help supplement the conversation and keep some information concrete.
    if modified_input in greetings_unformatted:
        return random.choice(greetings_formatted)
    elif "who" in modified_input and modified_input.endswith("are you"):
        return "I'm Monday, a chatbot. No I'm not sentient, maybe I will be, who knows..."
    elif "who is" in modified_input and modified_input.endswith("monday"):
        return "I'm Monday!"
    elif "who" in modified_input and modified_input.endswith("made you"):
        return "I was made by Afaq Anwar, a 17 year old Computer Science student."
    elif "your name" in modified_input:
        return "My name is Monday. I'm just a chatbot."
    elif "about yourself" in modified_input:
        return "Monday here, I'm a chatbot built with Tensorflow, I'm not that smart so take it easy for now please."
    elif "help me" in modified_input:
        return "I'm not exactly sure what I can do..."

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

    # Checks to see if the user wanted to make a calculation.
    if "what is" in modified_input:
        query = modified_input[modified_input.index("is") + 3:].replace(" ", "")
        if math_check(query):
            url_encoded_request = urllib.parse.quote(query)
            request = requests.get(calculator_api + url_encoded_request)
            data = query + " = " + request.text
            return data

    # Allows monday to query a vast array of topics using Wikipedia and Google.
    if "tell" in modified_input or "who is" in modified_input or "what is" in modified_input:
        obj_index = len(modified_input)
        if "tell" in modified_input and "more about" in modified_input or "tell" in modified_input and "about" in modified_input:
            # Note the query is one index behind the theoretical start of the subject, this is to account for spacing errors.
            obj_index = modified_input.index("about") + 5
        elif "who is" in modified_input or "what is" in modified_input and not math_check(modified_input[modified_input.index("is") + 2:].replace(" ", "")):
            obj_index = modified_input.index("is") + 2
        if obj_index < len(modified_input):
            query = modified_input[obj_index:]
            search_results = google.search(query, 1)
            for result in search_results:
                if "wikipedia" in result.link:
                    return result.description + "</br>" + "To read more visit the following link" + "</br>" + result.link
        else:
            return "I was not able to find anything about that."

    response = monday.get_response(modified_input)
    return str(response)


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
