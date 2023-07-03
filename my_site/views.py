from django.shortcuts import render
from django.http import FileResponse
from django.conf import settings
import os

def home(request):
    return render(request, "home.html")


def about(request):
    return render(request, "about.html")

def service(request):
    return render(request, "service.html")

def portfolio(request):
    return render(request, "portfolio.html")

def contact(request):
    return render(request, "contact.html")

def download(request):
    file = os.path.join(settings.BASE_DIR, 'my_site/static/my_site/moncv.pdf')

    fileOpened = open(file, 'rb')

    return FileResponse(fileOpened)