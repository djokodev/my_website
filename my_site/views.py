from django.shortcuts import render
from django.http import FileResponse
from django.conf import settings
import os

def home(request):
    return render(request, "home.html")


def download(request):
    file = os.path.join(settings.BASE_DIR, 'my_site/static/my_site/cv.pdf')

    fileOpened = open(file, 'rb')

    return FileResponse(fileOpened)