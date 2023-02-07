from rest_framework import serializers
from .models import Dish, Ingredient


class IngredientSerializer(serializers.ModelSerializer):
    """
    Сериалайзер Ингредиента.

    """

    class Meta:
        model = Ingredient
        fields = (
            "id",
            "name",
        )


class DishSerializer(serializers.ModelSerializer):
    """
    Сериалайзер Блюда.

    """

    ingredients = IngredientSerializer(many=True)

    class Meta:
        model = Dish
        fields = (
            "id",
            "name",
            "price",
            "ingredients",
        )
