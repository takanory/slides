from pathlib import Path

from pydantic import ValidationError

from example_model import Person

json_string = Path('person.json').read_text()
person = Person.model_validate_json(json_string)
print(person)
#> name='John Doe' age=30 email='john@example.com'

json_string = Path("person_wrong.json").read_text()
try:
    person = Person.model_validate_json(json_string)
except ValidationError as err:
    print(err)
