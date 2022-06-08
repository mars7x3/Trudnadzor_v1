from django.contrib import admin
from .models import *


class AboutTextInline(admin.TabularInline):
    model = AboutText


class AboutImageInline(admin.TabularInline):
    model = AboutImage


class AboutVideoInline(admin.TabularInline):
    model = AboutVideo


class AboutTaskInline(admin.TabularInline):
    model = AboutTask


class TaskTextInline(admin.TabularInline):
    model = TaskText


class TaskImageInline(admin.TabularInline):
    model = TaskImage


class PowerInline(admin.TabularInline):
    model = Power


class PowerTextInline(admin.TabularInline):
    model = PowerText


class AboutAdmin(admin.ModelAdmin):
    inlines = [
        AboutTextInline, AboutImageInline, AboutVideoInline, AboutTaskInline, TaskTextInline, TaskImageInline,
        PowerInline, PowerTextInline
    ]


admin.site.register(About, AboutAdmin)
admin.site.register(GosOrgan)
