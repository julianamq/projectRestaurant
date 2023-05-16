from src.models.ingredient import Ingredient, Restriction  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    ingredient_cheese = Ingredient("queijo gorgonzola")
    assert ingredient_cheese.name == "queijo gorgonzola"
    assert ingredient_cheese.restrictions == {
        Restriction.LACTOSE,
        Restriction.ANIMAL_DERIVED,
    }

    ingredient_far = Ingredient("farinha")
    assert ingredient_far.name == "farinha"
    assert ingredient_far.restrictions == {Restriction.GLUTEN}

    ingredient_bacon = Ingredient("bacon")
    assert ingredient_bacon.name == "bacon"
    assert ingredient_bacon.restrictions == {
        Restriction.ANIMAL_MEAT,
        Restriction.ANIMAL_DERIVED,
    }

    ingredient_cheese = Ingredient("queijo gorgonzola")
    assert repr(ingredient_cheese) == "Ingredient('queijo gorgonzola')"
    assert hash(ingredient_cheese) == hash("queijo gorgonzola")
    assert ingredient_cheese == Ingredient("queijo gorgonzola")
    assert ingredient_cheese != Ingredient("farinha")

    ingredient_cheese1 = Ingredient("queijo gorgonzola")
    ingredient_cheese2 = Ingredient("queijo gorgonzola")
    ingredient_bacon = Ingredient("bacon")
    assert hash(ingredient_cheese1) == hash(ingredient_cheese2)
    assert hash(ingredient_cheese1) != hash(ingredient_bacon)

    ingredient_cheese = Ingredient("queijo gorgonzola")
    ingredient_far = Ingredient("farinha")
    ingredient_bacon = Ingredient("bacon")
    assert Restriction.LACTOSE in ingredient_cheese.restrictions
    assert Restriction.GLUTEN in ingredient_far.restrictions
    assert Restriction.ANIMAL_MEAT in ingredient_bacon.restrictions
    assert Restriction.ANIMAL_DERIVED in ingredient_bacon.restrictions
