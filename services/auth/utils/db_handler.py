from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker
from sqlalchemy.future import select
from dotenv import load_dotenv
import os 
from datetime import datetime, timedelta
from models import Base, User

class DatabaseHandler:
    def __init__(self):
        # create the .env path manually
        envpath = os.path.join(os.path.dirname(__file__),'.env')
        load_dotenv(dotenv_path=envpath)


        self.db_name = os.getenv('DB_NAME')
        self.db_user = os.getenv('DB_USER')
        self.db_password = os.getenv('DB_PASSWORD')
        self.db_port = os.getenv('DB_PORT')

        self.DB_CONNECTION_STRING = f"postgresql://{self.db_user}:{self.db_password}@localhost:{self.db_port}/{self.db_name}"
        self.engine = create_async_engine(self.DB_CONNECTION_STRING, echo=True)
        self.SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=self.engine, class_=AsyncSession)

    async def start_session(self):
        async with self.SessionLocal() as session:
            yield session
    
    async def close_session(self):
        self.engine.dispose()


    # User Lookup Functions
    async def get_user_by_phone(self, session, phone) -> User | None:
        result = await session.execute(select(User).where(User.phone == phone))
        return result.fetchone()
    
    async def get_user_by_email(self, session, email) -> User | None:
        result = await session.execute(select(User).where(User.email == email))
        return result.fetchone()
    
    async def get_user_by_id(self, session, id) -> User | None:
        result = await session.execute(select(User).where(User.id == id))
        return result.fetchone()
    
    # ------------------    User Creation Functions    -----------------------

    # inserts an empty user object and returns the user.
    async def create_user_in_otp_flow(self, session, phone) -> User:
        user = User(phone=phone, auth_phone=True)
        session.add(user)
        await session.commit()
        return user

    # inserts a user object and returns the user. for eg. in the case of google auth.
    async def create_user(self, session, user: User) -> User:
        session.add(user)
        await session.commit()
        return user
    
    # ------------------    User Update Functions    -----------------------

    # once otp is validated, updates the user object and returns the user.
    async def update_user(self, session, user: User) -> User:
        existing_user = await self.get_user_by_id(session, user.id)
        if existing_user:
            existing_user.first_name = user.first_name
            existing_user.middle_name = user.middle_name
            existing_user.last_name = user.last_name
            existing_user.email = user.email
            existing_user.profile_image_uri = user.profile_image_uri
            await session.commit()
            return existing_user
        return None
    
    # ------------------    User Deletion Functions    -----------------------

    # deletes the user object and returns the user.
    async def delete_user(self, session, user: User) -> User:
        session.delete(user)
        await session.commit()
        return user
    
