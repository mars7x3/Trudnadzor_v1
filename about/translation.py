from modeltranslation.translator import register, TranslationOptions
from .models import *


@register(Management)
class ManagementTranslation(TranslationOptions):
    fields = ('position', 'date', 'city', 'family', )


@register(Education)
class EduTranslation(TranslationOptions):
    fields = ('education', )


@register(Exp)
class ExpTranslation(TranslationOptions):
    fields = ('exp', )


@register(Category)
class CategoryTranslation(TranslationOptions):
    fields = ('title', )


@register(Structure)
class StructureTranslation(TranslationOptions):
    fields = ('name', )
