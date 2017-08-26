from django.contrib import admin

from apps.events.models import Location
from apps.events.models import Pizzazip

admin.site.register(Location)

@admin.register(Pizzazip)
class PizzazipAdmin(admin.ModelAdmin):
    raw_id_fields = ['location']
