from django.contrib import admin

# Register your models here.
from .models import City, Country, Lead, Vendor, WalkIn, WebPage, Device, PageSection

admin.site.register(City)
admin.site.register(Country)
admin.site.register(Lead)
admin.site.register(Vendor)
admin.site.register(WalkIn)
admin.site.register(Device)
admin.site.register(WebPage)
admin.site.register(PageSection)