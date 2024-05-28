from django.shortcuts import render

# Create your views here.
def home(request):
    context = {}
    return render(request, 'home.html', context)

def mission(request):
    context = {}
    return render(request, 'mission.html', context)

def whoweworkwith(request):
    context = {}
    return render(request, 'who-we-work-with.html', context)

def careers(request):
    context = {}
    return render(request, 'careers.html', context)

def whatwedo(request):
    context = {}
    return render(request, 'what-we-do.html', context)
    
def publication(request):
    context = {}
    return render(request, 'publication.html', context)

def whoweare(request):
    context = {}
    return render(request, 'who-we-are.html', context)

def contact(request):
    context = {}
    return render(request, 'contact.html', context)

def apply(request):
    context = {}
    return render(request, 'apply.html', context)