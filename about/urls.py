from django.urls import path


from .views import *

urlpatterns = [
    path('management/', management, name='management'),
    path('management/<int:management_id>/', ManagementDetailView.as_view(), name='management'),
    path('history/', history, name='history'),
    path('structure/', structure, name='structure'),

]
