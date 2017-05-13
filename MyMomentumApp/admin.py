from django.contrib import admin

# Register your models here.
from .models import Instrument, Price

admin.site.register(Instrument)
admin.site.register(Price)