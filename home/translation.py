from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(AboutText)
class AboutTextTranslation(TranslationOptions):
    fields = ('text', )


@register(About)
class AboutTranslation(TranslationOptions):
    fields = ('title', 'text')


@register(AboutTask)
class AboutTaskTranslation(TranslationOptions):
    fields = ('title',)


@register(TaskText)
class AboutTextTranslation(TranslationOptions):
    fields = ('text',)


@register(Power)
class PowerTranslation(TranslationOptions):
    fields = ('title',)


@register(PowerText)
class PowerTextTranslation(TranslationOptions):
    fields = ('text',)


@register(GosOrgan)
class GosOrganTranslation(TranslationOptions):
    fields = ('name',)


