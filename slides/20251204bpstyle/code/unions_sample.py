from typing import Literal
from pydantic import BaseModel, Field

class Cat(BaseModel):
    pet_type: Literal['cat']
    meows: int

class Dog(BaseModel):
    pet_type: Literal['dog']
    barks: float

class Model(BaseModel):  # pet_typeで見分ける
    pet: Cat | Dog = Field(discriminator='pet_type')

print(Model(pet={'pet_type': 'dog', 'barks': 3.14}))
#> pet=Dog(pet_type='dog', barks=3.14)
