from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def home(request):
#     return HttpResponse("<h1>Welcome to ERP Dummy App</h1>")

def dashboard(request):
    return render(request,'core/dashboard.html')