from django.contrib import admin
from installations.models import Chargebox, Evse, Install


admin.site.register(Install)
admin.site.register(Chargebox)
admin.site.register(Evse)
