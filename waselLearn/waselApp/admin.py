from django.contrib import admin
from .models import Sugestion, Session, dayTimeSlot

# Register your models here.
admin.site.register(Sugestion)
admin.site.register(Session)
admin.site.register(dayTimeSlot)