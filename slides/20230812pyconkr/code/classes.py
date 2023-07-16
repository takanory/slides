from dataclasses import dataclass


@dataclass
class Order:  # Order(beer="IPA"), Order("Ale", "nuts")...
    beer: str = ""
    food: str = ""


def order_with_class(order: Order) -> str:
    match (order):
        case Order(beer="", food=""):
            return "Please order something."
        case Order(beer=beer, food=""):
            return f"I drink {beer}."
        case Order(beer="", food=food):
            return f"I eat {food}."
        case Order(beer=beer, food=food):
            return f"I drink {beer} with {food}."
        case _:
            return "Not an order."

print(order_with_class(Order()))
'Please order something.'
print(order_with_class(Order(beer="Ale")))
'I drink Ale.'
print(order_with_class(Order(food="fries")))
'I eat fries.'
print(order_with_class(Order("Ale", "fries")))
'I drink Ale with fries.'
print(order_with_class("IPA"))
'Not an order.'
