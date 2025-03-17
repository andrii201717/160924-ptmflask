from pydantic import BaseModel, EmailStr

class Address(BaseModel):
    city: str
    street: str
    house_number: int

class User(BaseModel):
    name:str
    age:int
    email: EmailStr
    address:Address

user_data = """
{
    "name": "Vlad",
    "age": "2_128",
    "email": "john.doee@xample.a",
    "address": {
        "city": "New York",
        "street": "St. Time Square",
        "house_number": 2
    }
}
"""

user = User.model_validate_json(user_data)

print(user)




class User(BaseModel):
    first_name: str
    last_name: str
    age: int


class Admin(User):
    salary_rating: float


class Moderator(User):
    phone: str


json_data = [
    """{"name": "Andre","age": 21,"email": "a.21@gmail.com"}""",
    """{"name": "Andre","age": 22,"email": "a.22@gmail.com"}""",
    """{"name": "Andre","age": 23,"email": "a.23@gmail.com"}""",
    """{"name": "Andre","age": 24,"email": "a.24@test.com"}""",
    """{"name": "Andre","age": 25,"email": "a.25@gmail.com"}""",
    """{"name": "Andre","age": 25,"email": "a.25@test.com"}"""
]

for us in json_data:
    try:
        user = User.model_validate_json(us)
        print(user)
    except ValidationError as err:
        print(err)



print("WE ARE IN THE SYSTEM!!!")