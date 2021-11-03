from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import *


# Apply summernote to all TextField in model.
class SomeModelAdmin(SummernoteModelAdmin):  # instead of ModelAdmin
    summernote_fields = '__all__'
    list_display = ['name', 'author', 'price', 'get_average_rate', 'category', 'place', 'check_availability', ]
    list_filter = ['category', 'place', 'created_at']


class PropertyBookAdmin(admin.ModelAdmin):
    list_display = ['property', 'booked']


admin.site.register(Property, SomeModelAdmin)
admin.site.register(Place)
admin.site.register(Category)
admin.site.register(PropertyBook, PropertyBookAdmin)
admin.site.register(PropertyImages)
admin.site.register(PropertyReview)
