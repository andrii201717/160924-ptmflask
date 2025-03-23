from pydantic import BaseModel, EmailStr, Field, ValidationError, field_validator, ValidationInfo
import json

class Address(BaseModel):
    city: str = Field(..., min_length=2, description="строка, минимум 2 символа.")
    street: str = Field(..., min_length=3, description="строка, минимум 3 символа.")
    house_number: int = Field(..., gt=0, description="число, должно быть положительным.")

class User(BaseModel):
    name: str = Field(..., min_length=2, pattern=r'^[a-zA-Z ]+$',
                      description="строка, должна быть только из букв, минимум 2 символа.")
    age: int = Field(..., ge=0, le=120, description="число, должно быть между 0 и 120")
    email: EmailStr
    is_employed: bool
    address: Address

    @field_validator("age")
    @classmethod
    def check_employment_status(cls, age: int, info: ValidationInfo) -> int:
        is_employed = info.data.get("is_employed")
        if is_employed and (age < 18 or age > 65):
            raise ValueError("Is_employed = true, возраст должен быть от 18 до 65 лет.")
        return age

def validate_and_serialize(json_str: str) -> str:
    try:
        user = User.model_validate(json.loads(json_str))
        return user.model_dump_json(indent=4)
    except ValidationError as e:
        return json.dumps({"errors": e.errors()}, indent=4)




json_users = """[
    {
        "name": "Иван Смирнов",
        "age": 45,
        "email": "ivan.smirnov@gmail.com",
        "is_employed": true,
        "address": {
            "city": "Одесса",
            "street": "Александровский проспект",
            "house_number": 12
        }
    },
    {
        "name": "Елена Иванова",
        "age": 99,
        "email": "elena.ivanova@gmail.com",
        "is_employed": false,
        "address": {
            "city": "Николаев",
            "street": "проспект Мира",
            "house_number": 34
        }
    },
    {
        "name": "Сергей Петров",
        "age": 50,
        "email": "sergey.petrov@gmail.com",
        "is_employed": true,
        "address": {
            "city": "Новосибирск",
            "street": "Ленина",
            "house_number": 56
        }
    },
    {
        "name": "Марина Курц",
        "age": 99,
        "email": "marina.kurz@gmail.com",
        "is_employed": false,
        "address": {
            "city": "Екатеринбург",
            "street": "Малышева",
            "house_number": 78
        }
    },
    {
        "name": "А С",
        "age": 55,
        "email": "alexander.sokolov@gmail.com",
        "is_employed": true,
        "address": {
            "city": "Владивосток",
            "street": "Океанский проспект",
            "house_number": 90
        }
    }
]"""

users = json.loads(json_users)


for i, user in enumerate(users, 1):
    result = validate_and_serialize(json.dumps(user))
    print(f"\n🔹 Проверка пользователя {i}: {user['name']}\nРезультат: {result}")