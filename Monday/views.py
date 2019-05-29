from django.shortcuts import render
from django.http import JsonResponse
from Rennon._deployment import inference


# Create your views here.
def index(request):
    return render(request, 'Monday/load.html')


def chat(request):
    if request.is_ajax():
        # Simple TF Model Only, to be replaced with more complex script.
        text = request.POST['input']
        result = inference.inference(text)
        indexBest = result.get("best_index")
        data = {'response': result.get("answers")[indexBest]}
        print(text)
        print(data)
        return JsonResponse(data)
    else:
        return render(request, 'Monday/chat.html')
