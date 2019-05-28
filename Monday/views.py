from django.shortcuts import render
from django.http import JsonResponse
from Rennon._deployment import inference


# Create your views here.
def index(request):
    return render(request, 'Monday/load.html')


def chat(request):
    if request.is_ajax():
        text = request.POST.get("chat", None)
        result = inference.inference(text)
        return JsonResponse({'response': result})
    else:
        return render(request, 'Monday/chat.html')
