from django.shortcuts import render
from .models import *


def activities_view(request):
    activities = Question.objects.all()
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
    before = StatisticCategory.objects.get(id=1)
    after = StatisticCategory.objects.get(id=2)
    name = StatisticCategory.objects.get(id=3)
    statistic1 = Statistic.objects.filter(number=1)
    statistic2 = Statistic.objects.filter(number=2)
    statistic3 = Statistic.objects.filter(number=3)
    statistic4 = Statistic.objects.filter(number=4)
    statistic5 = Statistic.objects.filter(number=5)
    statistic6 = Statistic.objects.filter(number=6)
    statistic7 = Statistic.objects.filter(number=7)
    statistic8 = Statistic.objects.filter(number=8)
    statistic9 = Statistic.objects.filter(number=9)
    statistic10 = Statistic.objects.filter(number=10)
    statistic11 = Statistic.objects.filter(number=11)

    context = {'before': before, 'after': after, 'name': name, 'statistic1': statistic1, 'statistic2': statistic2,
               'statistic3': statistic3, 'statistic4': statistic4, 'statistic5': statistic5, 'statistic6': statistic6,
               'statistic7': statistic7, 'statistic8': statistic8, 'statistic9': statistic9, 'statistic10': statistic10,
               'statistic11': statistic11}
    return render(request, "activities/statistic.html", context)

