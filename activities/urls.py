from django.urls import path


from .views import *

urlpatterns = [
    path('activities/', activities_view, name='activities'),
    path('gallery/', gallery, name='gallery'),
    path('link/', link_view, name='link'),
    path('statistic/', statistic, name='statistic'),

]
