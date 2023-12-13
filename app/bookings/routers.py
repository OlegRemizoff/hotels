from fastapi import APIRouter, FastAPI

from .dao import BookingDAO
from .schemas import SBooking


app = FastAPI()
router = APIRouter(
    prefix="/bookings",
    tags=["Бронирование"],
)


@router.get("")
async def get_bookings() -> list[SBooking]:
    return await BookingDAO.find_all()


@router.get("/{id}")
async def get_one_booking(id: int) -> SBooking:
    return await BookingDAO.find_by_id(id)

