from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def signup(request):
    return render(request, 'signup.html')

def signin(request):  # Updated here
    return render(request, 'signin.html')
def dashboard(request):  # Updated here
    return render(request, 'dashbord.html')
