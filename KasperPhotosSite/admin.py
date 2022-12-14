from django.contrib import admin
from .models import Photo, Appointment, Blog


# Register your models here.
admin.site.register(Photo)
admin.site.register(Appointment)
admin.site.register(Blog)