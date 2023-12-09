from django.contrib import admin

from .models import vendor,historical_data
# Register your models here.
admin.site.register(vendor)
admin.site.register(historical_data)