# Monday
Monday was a Machine Learning Chatbot deployed through a Django Web Application.

This branch, Rennon, is a Deep Learning Chatbot that uses a [Tensorflow backend](https://github.com/AfaqAnwar/Rennon).

### More About Monday
Monday currently communicates through a web application developed with Django, Jquery, and some simple Ajax requests.

Monday also has a few features!

Here are some phrases that can invoke certain features.

Including the following phrases in a sentence will result in Monday displaying a meme or a random photo.

```
<show || bring up> + < image || meme || photo >
```

Including the following phrases in a sentence will result in Monday sending a random fact.

```
<tell || give me> + <fact>
```

Inluding the following phrase in a sentence will allow Monday to calculate your given expression.

```
<what is> + ANY MATHEMATICAL EXPRESSION
```

Including the following phrases in a sentence will allow Monday to run a search for any known piece of information.

```
<who || what> + ANY SUBJECT + [end of sentence]<is> 
<tell> + <more about || about> + ANY SUBJECT || <who is || what is> + ANY SUBJECT 
```

  _Example Statements_

  * _Can you show me a meme?_
  
  * _Bring up any image._
  
  * _Tell me a random fact._
  
  * _Give me a fact please._
  
  * _What is 9 + 10?_

  * _Do you know who Jarvis is?_

  * _Can you tell me about Artificial Intelligence?_

  * _Can you tell me what Machine Learning is?_

### API Uages

#### JSON
 * [Random Cat Image](https://aws.random.cat/meow)
 * [Random Dog Image](https://random.dog/woof.json)
 * [Random Shiba Inu Images (10)](http://shibe.online/api/shibes?count=10&urls=true&httpsUrls=true)
 * [Random Fox Image](https://randomfox.ca/floof/)
 * [Random Facts](http://randomuselessfact.appspot.com/random.json?language=en)
 * [Calculator API](http://api.mathjs.org/)

#### Custom
 * [Google Search API built for Python](https://github.com/abenassi/Google-Search-API)

## Hosting Locally

### Requirements for Hosting Locally
I recommend you install Anaconda and create a virtual Python environment, this is the simplest and cleanest way to get the project running locally.

Although this tutorial is Linux based, the commands should be the same except for directiories and some minor CLI commands.
[Reccomended Tutorial for seamless installation.](https://www.pugetsystems.com/labs/hpc/Install-TensorFlow-with-GPU-Support-the-Easy-Way-on-Ubuntu-18-04-without-installing-CUDA-1170/)

[Additional Anaconda Documentation](https://docs.anaconda.com/anaconda/)

### Prerequisites
```

    Rennon release model 0.1 || 1.0 [1.0 is Recommended]

    Python 3.6.X

    Tensorflow-GPU Version 1.4.0 +  
      ~Following the Anaconda installation will also install all other required packages along with Tensorflow-GPU

    tqdm

    colorama

    regex

    python-Levenshtein

    requests
    
    sqlparse
    
    Django
    
    Google Search API built for Python 
    
```

### Steps
  1. Clone this repository onto your local machine.
  2. Download one of the [Rennon release models](https://www.github.com/AfaqAnwar/Rennon/releases) and extract the ```_deployment```      folder into the root folder ```Monday/```.
  3. Edit ```Monday/Rennon/settings.py``` to include a unique secret key.
  4. Edit ```Monday/Rennon/settings.py``` to include 'localhost' within ALLOWED_HOSTS.
  4. Open a CLI and CD into the main project directory ```Monday/``` with your existing Python virtual environment active.
  5. Run the following command ```python manage.py runserver```. 
  6. Open a browser and navigate to ```localhost:8000```.
