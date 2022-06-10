from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView

from .models import *


def management(request):
    managements = Management.objects.all()
    context = {'managements': managements}
    return render(request, 'about/management.html', context)


class ManagementDetailView(DetailView):
    model = Management
    template_name = 'about/management-detail.html'
    context_object_name = 'management'
    pk_url_kwarg = 'management_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        context['exp'] = Exp.objects.all()
        context['edu'] = Education.objects.all()
        return context


def history(request):
    histories = History.objects.all()
    context = {'histories': histories}
    return render(request, 'about/history.html', context)


def structure(request):
    structures1 = Structure.objects.filter(category=9)
    structures2 = Structure.objects.filter(category=8)
    structures3 = Structure.objects.filter(category=7)
    category1 = get_object_or_404(Category, id=9)
    category2 = get_object_or_404(Category, id=8)
    category3 = get_object_or_404(Category, id=7)

    context = {"structures1": structures1, "structures2": structures2, "structures3": structures3,
               'category1': category1, 'category2': category2, 'category3': category3}
    return render(request, 'about/structure.html', context)

