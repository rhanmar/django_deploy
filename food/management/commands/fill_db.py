from django.core.management.base import BaseCommand
from food.tests.factories import DishFactory, IngredientFactory


class Command(BaseCommand):
    help = "Заполнение БД тестовыми данными"

    def handle(self, *args, **kwargs):
        ingredient1 = IngredientFactory()
        ingredient2 = IngredientFactory()
        ingredient3 = IngredientFactory()
        ingredient4 = IngredientFactory()
        DishFactory(ingredients=[ingredient1, ingredient2])
        DishFactory(ingredients=[ingredient2, ingredient3, ingredient4])
        print("Окончание заполнения БД тестовыми данными")
