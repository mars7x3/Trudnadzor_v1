from django.shortcuts import render


def articles(request):
    return render(request, 'labor_rights/articles.html')