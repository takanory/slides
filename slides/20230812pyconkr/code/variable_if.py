def order_beer_and_food(order: tuple) -> str:
    if len(order) == 2:
        beer, food = order
        if beer == "" and food == "":
            return "I'm full."
        elif beer != "" and food == "":
            return f"I drink {beer}."
        elif beer == "" and food != "":
            return f"I eat {food}."
        else:
            return f"I drink {beer} with {food}."
    else:
        return "one beer and one food only."
