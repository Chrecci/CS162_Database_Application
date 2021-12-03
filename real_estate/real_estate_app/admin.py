from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Listing, Agent

# Register your models here.


@admin.register(Listing)
class ListingAdmin(admin.ModelAdmin):
    list_display = ('listing_id', 'address', 'price')
    list_filter = ('bathrooms', 'bedrooms')