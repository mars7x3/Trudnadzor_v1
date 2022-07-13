from urllib.parse import urljoin

from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
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
    category1 = CategoryContact.objects.get(id=1)
    category2 = CategoryContact.objects.get(id=2)
    category3 = CategoryContact.objects.get(id=3)


    phone = PhoneContact.objects.all()

    return render(request, 'contacts/contacts.html', {"contacts1": contact1, "contacts2": contact2,
                                                      "contacts3": contact3, "phone": phone,
                                                      'category1': category1, 'category2': category2,
                                                      'category3': category3})


def job(request):
    return render(request, 'job/job.html')


class OrderCreateView(View):
    @staticmethod
    def post(request, *args, **kwargs):
        form = MailForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            last_sender = Mail1.objects.first()
            try:
                file_url = last_sender.file.url
                message = f'Вид обращения: {last_sender.type_of_mail}\n' \
                          f'ФИО: {last_sender.first_name} {last_sender.name} {last_sender.last_name}\n' \
                          f'ПИН: {last_sender.pin}\n'  \
                          f'Почта: {last_sender.email}\nТелефон: {last_sender.phone}\nАдрес: {last_sender.address}\n' \
                          f'Текст обращения: {last_sender.text}\n' \
                          f'Файл: {urljoin(request.build_absolute_uri(), file_url)}'
                send_mail(
                    f'Физ лицо: {last_sender.first_name} {last_sender.name} {last_sender.last_name}',
                    message,
                    'mazzzek@bk.ru',
                    ['trud14@bk.ru'],
                    fail_silently=False,
                )

                messages.add_message(request, messages.SUCCESS, 'Обращение отправлено!')
                return HttpResponseRedirect(redirect_to=reverse_lazy('v2'))
            except:
                message = f'Вид обращения: {last_sender.type_of_mail}\n' \
                          f'ФИО: {last_sender.first_name} {last_sender.name} {last_sender.last_name}\n' \
                          f'ПИН: {last_sender.pin}\n' \
                          f'Почта: {last_sender.email}\nТелефон: {last_sender.phone}\nАдрес: {last_sender.address}\n' \
                          f'Текст обращения: {last_sender.text}\n'

                send_mail(
                    f'Физ лицо: {last_sender.first_name} {last_sender.name} {last_sender.last_name}',
                    message,
                    'mazzzek@bk.ru',
                    ['trud14@bk.ru'],
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
            try:
                file_url = last_sender.file.url

                message = f'Вид обращения: {last_sender.type_of_mail}\n' \
                          f'Организация: {last_sender.organ}\nИНН: {last_sender.inn}\n' \
                          f'Должность: {last_sender.position}\n' \
                          f'ФИО: {last_sender.first_name} {last_sender.name} {last_sender.last_name}\n' \
                          f'Почта: {last_sender.email}\nТелефон: {last_sender.phone}\nАдрес: {last_sender.address}\n' \
                          f'Текст обращения: {last_sender.text}\n' \
                          f'Файл: {urljoin(request.build_absolute_uri(), file_url)}'

                send_mail(
                    f'Юр лицо: {last_sender.organ} {last_sender.inn} {last_sender.position}',
                    message,
                    'mazzzek@bk.ru',
                    ['trud14@bk.ru'],
                    fail_silently=False,
                )
                messages.add_message(request, messages.SUCCESS, 'Обращение отправлено!')
                return HttpResponseRedirect(redirect_to=reverse_lazy('v3'))
            except:

                message = f'Вид обращения: {last_sender.type_of_mail}\n' \
                          f'Организация: {last_sender.organ}\nИНН: {last_sender.inn}\n' \
                          f'Должность: {last_sender.position}\n' \
                          f'ФИО: {last_sender.first_name} {last_sender.name} {last_sender.last_name}\n' \
                          f'Почта: {last_sender.email}\nТелефон: {last_sender.phone}\nАдрес: {last_sender.address}\n' \
                          f'Текст обращения: {last_sender.text}\n'

                send_mail(
                    f'Юр лицо: {last_sender.organ} {last_sender.inn} {last_sender.position}',
                    message,
                    'mazzzek@bk.ru',
                    ['trud14@bk.ru'],
                    fail_silently=False,
                )
                messages.add_message(request, messages.SUCCESS, 'Обращение отправлено!')
                return HttpResponseRedirect(redirect_to=reverse_lazy('v3'))

        messages.add_message(request, messages.ERROR, 'Ошибка отправки данных.')
