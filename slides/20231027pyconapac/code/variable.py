def order_beer_and_food(order: tuple) -> str:
    match (order):
        case ("", ""):
            return "Please order something."
        case (beer, ""):
            return f"I drink {beer}."
        case ("", food):
            return f"I eat {food}."
        case (beer, food):
            return f"I drink {beer} with {food}."
        case _:
            return "one beer and one food only."

order = ("", "")
print(order_beer_and_food(order))  # -> Please order something.

order = ("IPA", "")
print(order_beer_and_food(order))  # -> I drink IPA.

order = ("IPA", "nuts")
print(order_beer_and_food(order))  # -> I drink IPA with nuts.

order = ("IPA", "nuts", "spam")
print(order_beer_and_food(order))  # -> one beer and one food only.
