from django.shortcuts import render
from .models import *


def activities_view(request):
    activities = FAQ.objects.all()
    context = {"activities": activities}
    return render(request, 'activities/FAQ.html', context)


def gallery(request):
    images = Gallery.objects.all()
    context = {"images": images}
    return render(request, 'activities/gallery.html', context)


def link_view(request):
    link = Link.objects.all()
    context = {'link': link}
    return render(request, 'activities/links.html', context)


def statistic(request):
    return render(request, "activities/statistic.html")

