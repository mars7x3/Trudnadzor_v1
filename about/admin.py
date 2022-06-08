from django.contrib import admin
from .models import *
from modeltranslation.admin import TranslationAdmin


class EduAdmin(admin.TabularInline):
    model = Education


class ExpAdmin(admin.TabularInline):
    model = Exp


@admin.register(Management)
class ManagementAdmin(TranslationAdmin):
    inlines = [EduAdmin, ExpAdmin]


@admin.register(Structure)
class StructureAdmin(TranslationAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(TranslationAdmin):
    pass


