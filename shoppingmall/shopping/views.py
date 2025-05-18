from django.shortcuts import render


def index(request):
    context = {
        "title": "Shopping Mall",
        "description": "Welcome to the shopping mall",
    }
    return render(request, "shopping/index.html", context=context)


def products(request):
    pass


def login(request):
    pass


def singup(request):
    pass


# Create your views here.
