from pydantic import BaseModel
from datetime import date


# схема для валидации (то, что будет возвращать наш роутер)
class SBooking(BaseModel):
    room_id: int
    user_id: int
    date_from: date
    date_to: date
    price: int
    total_cost: int
    total_days: int

    class Config:
        orm_mod = True  