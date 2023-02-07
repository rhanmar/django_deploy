from django.db import models


class Ingredient(models.Model):
    """
    Ингредиент.

    """

    name = models.CharField(
        verbose_name="Название",
        max_length=124,
    )

    def __str__(self) -> str:
        return f"Ингредиент {self.name}"

    class Meta:
        verbose_name = "Ингредиент"
        verbose_name_plural = "Ингредиенты"


class Dish(models.Model):
    """
    Блюдо.

    """

    name = models.CharField(
        verbose_name="Название",
        max_length=124,
    )
    price = models.FloatField(
        verbose_name="Цена",
    )
    ingredients = models.ManyToManyField(
        Ingredient,
        verbose_name="Ингредиенты",
    )

    def __str__(self) -> str:
        return f"Блюдо {self.name} | {self.price} руб."

    class Meta:
        verbose_name = "Блюдо"
        verbose_name_plural = "Блюда"
