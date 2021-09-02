from django.contrib import admin

from .models import Property

class PropertyAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published', 'rent', 'list_date','landlord')
    list_display_links = ('id','title')
    list_filter = ('landlord',)
    list_editable = ('is_published',)
    search_fields = ('title', 'address', 'city', 'zipcode', 'rent')
    list_per_page = 25
admin.site.register(Property, PropertyAdmin)

