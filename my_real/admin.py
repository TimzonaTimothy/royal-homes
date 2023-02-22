from django.contrib import admin
from .models import *
# Register your models here.


class ListingAdmin(admin.ModelAdmin):
    list_display = ('id','property_type', 'title', 'is_published', 'price', 'list_date')
    list_display_links = ('id', 'title')
    search_fields = ('title', 'description', 'address', 'city', 'state', 'zipcode','price',)
    list_per_page = 25


admin.site.register(Listing, ListingAdmin)



class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'listing', 'email', 'contact_date')
    list_display_links = ('id', 'name') 
    search_fields = ('name', 'email', 'listing')
    list_per_page = 25

admin.site.register(Contact, ContactAdmin)