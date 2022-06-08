from django.urls import path


from .views import *

urlpatterns = [
    path('news/', news_view, name='news'),
    path('news/<int:news_id>/', NewsDetailView.as_view(), name='news'),

]
