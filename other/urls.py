from django.urls import path


from .views import *

urlpatterns = [
    path('mail/', mail, name='mail'),
    path('mail1/', mail1, name='v1'),
    path('mail2/', mail2, name='v2'),
    path('mail3/', mail3, name='v3'),
    path('mail2/create/', OrderCreateView.as_view(), name='v2_create'),
    path('mail3/create/', OrderCreateView2.as_view(), name='v3_create'),
    path('partners/', partners, name='partners'),
    path('contacts/', contacts, name='contacts'),
    path('job/', job, name='job'),

]
