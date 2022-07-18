from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(StatisticCategory)
class StatisticCategoryTranslation(TranslationOptions):
    fields = ('title', )


@register(Statistic)
class StatisticTranslation(TranslationOptions):
    fields = ('title', 'score1', 'score2')
