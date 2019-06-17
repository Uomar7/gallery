from django.contrib import admin
from .models import Image,category,Location

class ImageAdmin(admin.ModelAdmin):
    filter_horizontal = ('category',)


admin.site.register(Image, ImageAdmin)
admin.site.register(category)
admin.site.register(Location)
