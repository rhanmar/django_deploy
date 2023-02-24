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
    ingredients_count = serializers.IntegerField()

    class Meta:
        model = Dish
        fields = (
            "id",
            "name",
            "price",
            "ingredients_count",
            "ingredients",
        )
