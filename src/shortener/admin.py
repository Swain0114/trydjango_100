from django.contrib import admin

# Register your models here.

from .models import shortener

admin.site.register(shortener)