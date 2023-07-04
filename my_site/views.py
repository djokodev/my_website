from django.shortcuts import render, redirect
from django.http import FileResponse
from django.conf import settings
from . forms import ContactForm
from my_site.models import Contact
import os

        
def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = ContactForm()
    return render(request, "contact.html", {"form":form})

def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")

def service(request):
    return render(request, "service.html")

def portfolio(request):
    return render(request, "portfolio.html")


def download(request):
    file = os.path.join(settings.BASE_DIR, 'my_site/static/my_site/moncv.pdf')

    fileOpened = open(file, 'rb')

    return FileResponse(fileOpened)