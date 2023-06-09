from django.contrib import admin
from food.models import Food


class FoodAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "publisher_name", "is_deleted"]

admin.site.register(Food,FoodAdmin)




