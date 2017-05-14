from django.contrib import admin

# Register your models here.
from .models import Instrument, Price, Index, Universe

admin.site.register(Instrument)
admin.site.register(Price)
admin.site.register(Index)
admin.site.register(Universe)
