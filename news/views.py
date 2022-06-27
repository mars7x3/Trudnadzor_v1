from django.db.models import Q
from django.shortcuts import render
from django.views.generic import DetailView

from .models import News


def news_view(request):
    news = News.objects.all()
    context = {'news': news}
    return render(request, 'news/news.html', context)


class NewsDetailView(DetailView):
    model = News
    template_name = 'news/news-detail.html'
    context_object_name = 'news'
    pk_url_kwarg = 'news_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data()
        now_news = self.get_object()
        context['recommendation'] = News.objects.filter(~Q(id=now_news.id)).order_by('-date')[:6]
        return context

