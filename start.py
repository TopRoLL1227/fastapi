from pydantic import BaseModel

class User(BaseModel):
    username: str
    email: str
    balance: float = 0


new_user = User(
    username='admin1', 
    email='mail@mail.ru', 
    balance='10000'
)

print(new_user.username)