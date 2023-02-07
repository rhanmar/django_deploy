from rest_framework.viewsets import ReadOnlyModelViewSet
from food.models import Dish
from food.serializers import DishSerializer


class DishViewSet(ReadOnlyModelViewSet):
    """
    Блюда.

    """

    queryset = Dish.objects.all().prefetch_related("ingredients")
    serializer_class = DishSerializer
