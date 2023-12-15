from fastapi import APIRouter, HTTPException, Response, status
from .schemas import UserAuth
from .dao import UsersDAO
from .auth import get_password_hash, verify_password, authenticate_user, create_access_token

router = APIRouter(
    prefix="/auth",
    tags=["Auth & Пользователи"],
)



@router.post("/register")
async def register_user(user_data: UserAuth):
    existing_user = await UsersDAO.find_one_or_none(email=user_data.email)
    if existing_user:
        raise HTTPException(status_code=500)
    
    hashed_password = get_password_hash(user_data.password)
    await UsersDAO.add(email=user_data.email, hashed_password=hashed_password)


@router.post("/login")
async def login_user(response: Response, user_data: UserAuth):
    user = await authenticate_user(user_data.email, user_data.password)
    if not user:
        return HTTPException(status_code=status.HTTP_401_UNAUTHORIZED)
    access_token = create_access_token({"sub": user.id})
    response.set_cookie("bookings_access_token", access_token, httponly=True) # добавляем наш токен в куки браузера
    return {"access_token": access_token}
    