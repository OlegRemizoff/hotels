from fastapi import APIRouter, FastAPI, Depends
from datetime import date
from sqlalchemy import select, delete, insert, func, and_, or_
from app.users.models import Users
from app.users.dependencies import get_current_user
from app.exceptions import RoomCannotBeBooked

from .dao import BookingDAO
from .schemas import SBooking



app = FastAPI()
router = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"],
)


# @router.get("")
# async def get_bookings() -> list[SBooking]:
#     return await BookingDAO.find_all()


@router.get("/{id}")
async def get_one_booking(id: int) -> SBooking:
    return await BookingDAO.find_by_id(id)



@router.get("")
async def get_bookings(user: Users = Depends(get_current_user)) -> list[SBooking]:
    print(user, type(user), user.email)
    return await BookingDAO.find_all(user_id=user.id)


@router.post("")
async def add_booking(
    room_id: int, date_from: date, date_to: date,
    user: Users = Depends(get_current_user)
    ):
    booking = await BookingDAO.add(user.id, room_id, date_from, date_to)
    if not booking:
        raise RoomCannotBeBooked