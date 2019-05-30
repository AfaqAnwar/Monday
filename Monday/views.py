from django.shortcuts import render
from django.http import JsonResponse
from Monday import monday_inference


# Create your views here.
def index(request):
    return render(request, 'Monday/load.html')


def chat(request):
    if request.is_ajax():
        # Simple TF Model Only, to be replaced with more complex script.
        text = request.POST['input']
        data = {'response': monday_inference.get_response(text)}
        return JsonResponse(data)
    else:
        return render(request, 'Monday/chat.html')
