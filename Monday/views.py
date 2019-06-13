from django.shortcuts import render
from django.http import JsonResponse
from Monday import monday_inference
from django.views.decorators.csrf import ensure_csrf_cookie
@ensure_csrf_cookie
def index(request):
    return render(request, 'Monday/load.html')


def chat(request):
    if request.is_ajax():
        text = request.POST['input']
        data = {'response': monday_inference.get_response(text)}
        return JsonResponse(data)
    else:
        monday_inference.initialize_monday()
        return render(request, 'Monday/chat.html')
