from django.contrib import admin

# Register your models here.

from .models import Event, Type, Comment

admin.site.register(Event)
admin.site.register(Type)
admin.site.register(Comment)