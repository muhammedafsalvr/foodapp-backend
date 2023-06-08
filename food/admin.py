from django.contrib import admin
from food.models import Food


class FoodAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "publisher_name"]

admin.site.register(Food,FoodAdmin)




