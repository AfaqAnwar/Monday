from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'Monday/load.html')


def chat(request):
    return render(request, 'Monday/chat.html')
