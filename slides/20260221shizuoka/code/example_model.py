from pydantic import BaseModel, EmailStr, PositiveInt

class Person(BaseModel):  # BaseModelを継承
    name: str
    age: PositiveInt  # 正の整数
    email: EmailStr  # メールアドレス
