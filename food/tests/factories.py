from food.models import Dish, Ingredient
import factory


class DishFactory(factory.django.DjangoModelFactory):
    """
    Фабрика Блюда.

    """

    name = factory.Faker("name")
    price = factory.Sequence(lambda x: x)

    @factory.post_generation
    def ingredients(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for ingredient in extracted:
                self.ingredients.add(ingredient)

    class Meta:
        model = Dish


class IngredientFactory(factory.django.DjangoModelFactory):
    """
    Фабрика Ингредиента.

    """

    name = factory.Faker("name")

    class Meta:
        model = Ingredient
