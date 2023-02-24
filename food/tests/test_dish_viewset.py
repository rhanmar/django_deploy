import pytest
from .factories import DishFactory, IngredientFactory
from rest_framework import status
from django.urls import reverse


@pytest.mark.django_db
@pytest.mark.dishes
def test_list(api_client, django_assert_num_queries):
    ingredient1 = IngredientFactory()
    ingredient2 = IngredientFactory()
    ingredient3 = IngredientFactory()
    ingredient4 = IngredientFactory()
    dish1 = DishFactory(ingredients=[ingredient1, ingredient2])
    dish2 = DishFactory(ingredients=[ingredient2, ingredient3, ingredient4])

    url = reverse("dishes-list")

    with django_assert_num_queries(2):
        response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    res_json = response.json()
    assert len(res_json) == 2
    for dish_json in res_json:
        assert "id" in dish_json
        assert "name" in dish_json
        assert "price" in dish_json
        assert "ingredients" in dish_json
        ingredients_json = dish_json["ingredients"]
        match dish_json["id"]:
            case dish1.id:
                assert len(ingredients_json) == 2
            case dish2.id:
                assert len(ingredients_json) == 3
        for ingredient_json in ingredients_json:
            assert "id" in ingredient_json
            assert "name" in ingredient_json


@pytest.mark.django_db
@pytest.mark.dishes
def test_detail(api_client, django_assert_num_queries):
    ingredients = [IngredientFactory() for _ in range(10)]
    dish = DishFactory(ingredients=ingredients)

    url = reverse("dishes-detail", kwargs={"pk": dish.id})

    with django_assert_num_queries(2):
        response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    dish_json = response.json()
    assert dish_json["id"] == dish.id
    assert dish_json["name"] == dish.name
    assert dish_json["price"] == dish.price
    assert "ingredients" in dish_json
    ingredients_json = dish_json["ingredients"]
    assert len(ingredients_json) == len(ingredients)
    for ingredient_json in ingredients_json:
        assert "id" in ingredient_json
        assert "name" in ingredient_json


@pytest.mark.django_db
@pytest.mark.dishes
def test_ingredients_count(api_client, django_assert_num_queries):
    ingredient1 = IngredientFactory()
    ingredient2 = IngredientFactory()
    dish1 = DishFactory(ingredients=[ingredient1, ingredient2])
    dish2 = DishFactory()

    url = reverse("dishes-list")

    with django_assert_num_queries(2):
        response = api_client.get(url)
    assert response.status_code == status.HTTP_200_OK
    res_json = response.json()
    assert len(res_json) == 2
    for dish_json in res_json:
        match dish_json["id"]:
            case dish1.id:
                assert dish_json["ingredients_count"] == 2
            case dish2.id:
                assert dish_json["ingredients_count"] == 0
