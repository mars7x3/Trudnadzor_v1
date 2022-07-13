from django.shortcuts import render
from .models import *
from news.models import News
from other.models import Partner


def home(request):
    about_title = About.objects.all()
    about_text = AboutText.objects.all()
    about_image = AboutImage.objects.all()
    about_video = AboutVideo.objects.all()
    about_task = AboutTask.objects.all()
    about_task_text = TaskText.objects.all()
    about_task_image = TaskImage.objects.all()
    about_power = Power.objects.all()
    about_power_text = PowerText.objects.all()
    home_news = News.objects.all().order_by('-date')
    partners = Partner.objects.all()
    gos_organ = GosOrgan.objects.all()
    context = {"about_text": about_text, "about_title": about_title, "about_image": about_image,
               "about_video": about_video, "about_task": about_task, "about_task_text": about_task_text,
               "about_task_image": about_task_image, "about_power": about_power, "partners": partners,
               "about_power_text": about_power_text, "home_news": home_news, 'gos_organ': gos_organ}
    return render(request, 'home/home.html', context)


