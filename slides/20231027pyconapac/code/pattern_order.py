def order_beer_and_food(order: tuple) -> str:
    match (order):
        case (beer, food):  # match here
            return f"I drink {beer} with {food}."
        case ("", ""):  # never reach
            return "Please order something."
        case (beer, ""):  # never reach
            return f"I drink {beer}."
        case ("", food):  # never reach
            return f"I eat {food}."
        case _:
            return "one beer and one food only."

order = ("", "nuts")
print(order_beer_and_food(order))  # -> I drink  with nuts.
