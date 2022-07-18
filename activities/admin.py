from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from .models import *


admin.site.register(Question)
admin.site.register(Gallery)
admin.site.register(Link)
admin.site.register(StatisticNumber)


@admin.register(StatisticCategory)
class HistoryAdmin(TranslationAdmin):
    pass


@admin.register(Statistic)
class HistoryAdmin(TranslationAdmin):
    pass

