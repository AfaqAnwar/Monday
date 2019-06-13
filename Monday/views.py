from django.shortcuts import render
from django.http import JsonResponse
from Monday import rennon_inference
from django.views.decorators.csrf import ensure_csrf_cookie
@ensure_csrf_cookie
def index(request):
    return render(request, 'Monday/load.html')


def chat(request):
    if request.is_ajax():
        text = request.POST['input']
        data = {'response': rennon_inference.get_response(text)}
        return JsonResponse(data)
    else:
        return render(request, 'Monday/chat.html')
