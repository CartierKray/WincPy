import models
import peewee
from typing import List

__winc_id__ = "286787689e9849969c326ee41d8c53c4"
__human_name__ = "Peewee ORM"


def cheapest_dish() -> models.Dish:
    """You want ot get food on a budget

    Query the database to retrieve the cheapest dish available
    """
    cheapest_dish = models.Dish.select().order_by(models.Dish.price_in_cents).first()
    return cheapest_dish


def vegetarian_dishes() -> List[models.Dish]:
    """You'd like to know what vegetarian dishes are available

    Query the database to return a list of dishes that contain only
    vegetarian ingredients.
    """
    vegetarian_dishes = []
    for dish in models.Dish.select(): 
        if all(ingredient.is_vegetarian for ingredient in dish.ingredients):
                vegetarian_dishes.append(dish)
    return vegetarian_dishes


def best_average_rating() -> models.Restaurant:
    """You want to know what restaurant is best.

    Query the database to retrieve the restaurant that has the highest
    average rating.
    """
    query = (
        models.Restaurant
        .select(models.Restaurant, peewee.fn.AVG(models.Rating.rating).alias("avg_rating"))
        .join(models.Rating)
        .group_by(models.Restaurant)
        .order_by(peewee.fn.AVG(models.Rating.rating).desc())
        .first()
    )
    return query




def add_rating_to_restaurant() -> None:
    """After visiting a restaurant, you want to leave a rating

    Select the first restaurant in the dataset and add a rating
    """
    first_restaurant = models.Restaurant.select().first()
    models.Rating.create(restaurant=first_restaurant, rating=5, comment="Enjoyable Dish")


def dinner_date_possible() -> List[models.Restaurant]:
    """You have asked someone out on a dinner date, but where to go?

    You want to eat at around 19:00 and your date is vegan.
    Query a list of restaurants that account for these constraints.
    """
    restaurants_met_requirements = []
    restaurants = models.Restaurant.select().where(models.Restaurant.opening_time.hour <= 19).where(models.Restaurant.closing_time.hour >= 19)
    for restaurant in restaurants:
        if any((all(ingredient.is_vegan for ingredient in dish.ingredients)) for dish in restaurant.dish_set.select()):     # dish_set is default name for backref to model.Dish
            restaurants_met_requirements.append(restaurant)
    return restaurants_met_requirements


def add_dish_to_menu() -> models.Dish:
    """You have created a new dish for your restaurant and want to add it to the menu

    The dish you create must at the very least contain 'cheese'.
    You do not know which ingredients are in the database, but you must not
    create ingredients that already exist in the database. You may create
    new ingredients however.
    Return your newly created dish
    """
    new_dish_name = "The Daily Special"
    restaurant_id = models.Restaurant.get_by_id(1)
    new_dish_price = 10000
    ingredients_new_dish = ["cheese", "pasta", "salmon", "onions"]


 # check if ingredients are in db
    cheese, created = models.Ingredient.get_or_create(name=ingredients_new_dish[0],
                                             defaults={
                                             'is_vegetarian': True,
                                             'is_vegan': False,
                                             'is_glutenfree': True,
                                             },)

    pasta, created = models.Ingredient.get_or_create(name=ingredients_new_dish[1],
                                             defaults={
                                             'is_vegetarian': True,
                                             'is_vegan': True,
                                             'is_glutenfree': False,
                                             },)

    salmon, created = models.Ingredient.get_or_create(name=ingredients_new_dish[2],
                                             defaults={
                                             'is_vegetarian': False,
                                             'is_vegan': False,
                                             'is_glutenfree': True,
                                             },)

    onions, created = models.Ingredient.get_or_create(name=ingredients_new_dish[3],
                                             defaults={
                                             'is_vegetarian': True,
                                             'is_vegan': True,
                                             'is_glutenfree': True,
                                             },)

    new_dish = models.Dish.create(name=new_dish_name,
                                  served_at=restaurant_id,
                                  price_in_cents=new_dish_price,
                                  )
    new_dish.ingredients.add([cheese, pasta, salmon, onions])   # ingredients is basicly its own table due to manytomanyfield
    
    return new_dish


if __name__ == "__main__":
    # print(cheapest_dish())
    # print(vegetarian_dishes())
    print(best_average_rating())
    # print(dinner_date_possible())
    # print(add_dish_to_menu())