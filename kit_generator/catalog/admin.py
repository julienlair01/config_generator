from django.contrib import admin
from catalog.models import Manufacturer, ChargeboxModel, Customer


admin.site.register(Manufacturer)
admin.site.register(ChargeboxModel)
admin.site.register(Customer)