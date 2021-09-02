from django.contrib import admin

from .models import Landlord

class LandlordAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email')
    list_display_links = ('id','name')
    list_filter = ('name',)
    search_fields = ('name', 'email')
    list_per_page = 25

admin.site.register(Landlord, LandlordAdmin)

