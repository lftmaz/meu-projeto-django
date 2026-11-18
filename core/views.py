from django.shortcuts import render

from django.http import JsonResponse
def home(request):
    return JsonResponse({
        "message": "Olá, Django!",
        "status":  "ok"
    })
    # Create your views here.
