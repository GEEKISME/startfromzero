from pydantic import ValidationError
from datetime import datetime
from typing import List
from pydantic import BaseModel
class User(BaseModel):
    id:int
    name='jack guo'
    signup_timestamp:datetime=None
    friends:List[int]=[]

try:
    User(signup_timestamp='not datetime',friends=[1,2,3,'not number'])
except ValidationError as e:
    print(e.json())