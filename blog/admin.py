from django.contrib import admin
from tof.admin import TofAdmin, TranslationTabularInline

from .models import *


class CategoryAdmin(TofAdmin):
    list_display = ['id', 'name']
    inlines = [TranslationTabularInline]


admin.site.register(Post)
admin.site.register(Category, CategoryAdmin)
