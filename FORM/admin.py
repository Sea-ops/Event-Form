from django.contrib import admin
from .models import List

# Register your models here.
class List_AD(admin.ModelAdmin):
    list_display = ('id', 'Name', 'Surname', 'Event', 'Date', 'Address')

admin.site.register(List, List_AD)
