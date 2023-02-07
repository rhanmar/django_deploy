from django.contrib import admin
from .models import Dish, Ingredient


@admin.register(Dish)
class DishAdmin(admin.ModelAdmin):
    """
    Блюдо.

    """

    list_display = (
        "id",
        "name",
        "price",
    )


@admin.register(Ingredient)
class IngredientAdmin(admin.ModelAdmin):
    """
    Ингредиент.
    """

    list_display = (
        "id",
        "name",
    )
