from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(CategoryContact)
class CategoryContactTranslation(TranslationOptions):
    fields = ('department', )


@register(Contact)
class CategoryContactTranslation(TranslationOptions):
    fields = ('title', 'address')


