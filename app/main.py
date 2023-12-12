from fastapi import FastAPI, Query, Depends
from typing import Optional
from datetime import date
from pydantic import BaseModel


app = FastAPI(debug=True)

class SBooking(BaseModel):
    rom_id: int
    date_from: date
    date_to: date

class SHotels(BaseModel):
    address: str
    name: str
    stars: int
    has_spa: bool



class HotelSearchArgs:
    def __init__(
        self, 
    location: str,
    date_from: date,
    date_to: date,
    has_spa: Optional[bool] = None,
    stars: Optional[int] = Query(None, ge=1, le=5),    
    ):
        self.location = location
        self.date_from = date_from
        self.date_to = date_to
        self.has_spa = has_spa
        self.start = stars


# @app.get('/hotels', response_model=list[SHotels])
@app.get('/hotels')
def get_hotels(): 
    search_args: HotelSearchArgs = Depends()
    return search_args








@app.post('/bookings')
def add_book(booking: SBooking):
    pass
