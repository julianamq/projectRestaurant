from src.models.dish import Dish  # noqa: F401, E261, E501
import pytest
from src.models.ingredient import Ingredient, Restriction


# Req 2
def test_dish():
    dish_lasanha = Dish("lasanha", 70.00)
    assert dish_lasanha.name == "lasanha"
    assert dish_lasanha.price == 70.00

    dish_lasanha = Dish("lasanha", 70.00)
    assert repr(dish_lasanha) == "Dish('lasanha', R$70.00)"
    dish_lasanha = Dish("lasanha", 70.00)
    dish_massa = Dish("lasanha", 70.00)
    dish_bacon = Dish("bacon", 55.00)
    assert dish_lasanha == dish_massa
    assert dish_lasanha != dish_bacon

    dish_lasanha = Dish("lasanha", 70.00)
    dish_massa = Dish("lasanha", 70.00)
    dish_bacon = Dish("bacon", 55.00)
    assert hash(dish_lasanha) == hash(dish_massa)
    assert hash(dish_lasanha) != hash(dish_bacon)

    dish_lasanha = Dish("lasanha", 70.00)
    ingredient_presunto = Ingredient("presunto")
    ingredient_frango = Ingredient("frango")
    dish_lasanha.add_ingredient_dependency(ingredient_presunto, 2)
    dish_lasanha.add_ingredient_dependency(ingredient_frango, 1)
    expected_restrictions = {
        Restriction.ANIMAL_MEAT, Restriction.ANIMAL_DERIVED}
    assert dish_lasanha.get_restrictions() == expected_restrictions

    with pytest.raises(TypeError):
        Dish("lasanha", "70.00")

    with pytest.raises(ValueError):
        Dish("lasanha", 0)

    dish_lasanha = Dish("lasanha", 70.00)
    assert dish_lasanha.get_restrictions() == set()

    dish_lasanha = Dish("lasanha", 70.00)
    assert dish_lasanha.get_ingredients() == set()
