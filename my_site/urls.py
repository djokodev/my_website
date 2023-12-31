from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("download", views.download, name="download"),
    path("about", views.about, name="about"),
    path("service", views.service, name="service"),
    path("portfolio", views.portfolio, name="portfolio"),
    path("contact", views.contact, name="contact"),
]