from fastapi import APIRouter, FastAPI, Depends
from app.users.models import Users
from app.users.dependencies import get_current_user

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
async def get_bookings(user: Users = Depends(get_current_user)):
    print(user, type(user), user.email)
    return await BookingDAO.find_all(user_id=user.id)