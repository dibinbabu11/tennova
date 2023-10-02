from django.contrib import admin
from . models import Recipie

# Register your models here.
class RecipieAdmin(admin.ModelAdmin):
    list_display=['name','slug','prep_time','vegetarian']
    prepopulated_fields={"slug":("name",)}
admin.site.register(Recipie,RecipieAdmin)

