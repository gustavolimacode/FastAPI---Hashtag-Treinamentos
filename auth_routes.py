from fastapi import APIRouter, Depends, HTTPException
from models import User
from dependencies import get_session
from main import bcrypt_context
from schemas import UserSchema, LoginSchema

auth_router = APIRouter(prefix='/auth', tags=['auth'])

def create_token(user_id):
    token = f"dhkn321kn32o1{user_id}"
    return 

@auth_router.get('/')
async def home():
    return {'message': 'You accessed authenticate route', 'authentificated': False}


@auth_router.post('/create_account')
async def create_account(user_schema: UserSchema, session = Depends(get_session)):
    user = session.query(User).filter(User.email==user_schema.email).first()
    if user:
        # There is already a user with this email address
        raise HTTPException(status_code=400, detail="Email already registered")
    else:
        encrypted_psw = bcrypt_context.hash(user_schema.password)
        new_user = User(user_schema.name, user_schema.email, encrypted_psw, user_schema.status, user_schema.admin)
        session.add(new_user)
        session.commit()
        return {'message': 'User successfully registered'}
    

@auth_router.post('/login')
async def login(login_schema: LoginSchema, session = Depends(get_session)):
    user = session.query(User).filter(User.email==login_schema.email).first()
    if not user:
        raise HTTPException(status_code=400, detail="User not found")
    else:
        access_token = create_token(user.id)
        return {
            "access_token": access_token,
            "token_type": 'Bearer'
            }