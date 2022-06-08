from django.conf.urls.i18n import i18n_patterns
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

]+ i18n_patterns(
    path('i18n/', include("django.conf.urls.i18n")),
    path('', include('home.urls')),
    path('', include('about.urls')),
    path('', include('news.urls')),
    path('', include('activities.urls')),
    path('', include('other.urls')),
    path('', include('labor_rights.urls')),
    prefix_default_language=False,

)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

