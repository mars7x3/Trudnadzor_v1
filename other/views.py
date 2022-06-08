from urllib.parse import urljoin

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.mail import send_mail
from django.views import View
from .forms import MailForm, MailForm2
from .models import *
from django.urls import reverse_lazy


def mail(request):
    return render(request, 'mail/mail.html')


def mail1(request):
    return render(request, 'mail/v1.html')


def mail2(request):
    return render(request, 'mail/v2.html')


def mail3(request):
    return render(request, 'mail/v3.html')


def partners(request):
    partner = Partner.objects.all()
    return render(request, 'partners/partners.html', {"partners": partner})


def contacts(request):
    contact1 = Contact.objects.filter(department=1)
    contact2 = Contact.objects.filter(department=2)
    contact3 = Contact.objects.filter(department=3)
    phone = PhoneContact.objects.all()

    return render(request, 'contacts/contacts.html', {"contacts1": contact1, "contacts2": contact2,
                                                      "contacts3": contact3, "phone": phone})


def job(request):
    return render(request, 'job/job.html')


class OrderCreateView(View):
    @staticmethod
    def post(request, *args, **kwargs):
        form = MailForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            last_sender = Mail1.objects.first()
            file_url = last_sender.file.url
            message = f'ФИО: {last_sender.first_name} {last_sender.name} {last_sender.last_name}\n' \
                      f'Почта: {last_sender.email}\nТелефон: {last_sender.phone}\nАдрес: {last_sender.address}\n' \
                      f'Текст обращения: {last_sender.text}\nФайл: {urljoin(request.build_absolute_uri(), file_url)}'

            send_mail(
                f'Физ лицо: {last_sender.first_name} {last_sender.name} {last_sender.last_name}',
                message,
                'mazzzek@bk.ru',
                ['m.ysakov.jcc@gmail.com'],
                fail_silently=False,
            )

            messages.add_message(request, messages.SUCCESS, 'Обращение отправлено!')
            return HttpResponseRedirect(redirect_to=reverse_lazy('v2'))
        messages.add_message(request, messages.ERROR, 'Ошибка отправки данных.')


class OrderCreateView2(View):
    @staticmethod
    def post(request, *args, **kwargs):
        form = MailForm2(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            last_sender = Mail2.objects.first()
            file_url = last_sender.file.url

            message = f'Организация: {last_sender.organ}\nИНН: {last_sender.inn}\nДолжность: {last_sender.position}\n' \
                      f'ФИО: {last_sender.first_name} {last_sender.name} {last_sender.last_name}\n' \
                      f'Почта: {last_sender.email}\nТелефон: {last_sender.phone}\nАдрес: {last_sender.address}\n' \
                      f'Текст обращения: {last_sender.text}\nФайл: {urljoin(request.build_absolute_uri(), file_url)}'

            send_mail(
                f'Юр лицо: {last_sender.organ} {last_sender.inn} {last_sender.position}',
                message,
                'mazzzek@bk.ru',
                ['m.ysakov.jcc@gmail.com'],
                fail_silently=False,
            )
            messages.add_message(request, messages.SUCCESS, 'Обращение отправлено!')
            return HttpResponseRedirect(redirect_to=reverse_lazy('v3'))
        messages.add_message(request, messages.ERROR, 'Ошибка отправки данных.')
