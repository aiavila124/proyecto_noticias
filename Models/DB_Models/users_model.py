from sqlalchemy import func, String, Integer, Column, Date, TIMESTAMP
from Class.database import Database as DB
from Helpers.constantes import ACTIVE, INACTIVE


class Users(DB.base_class):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    username = Column(String(100))
    email = Column(String(100))
    password = Column(String(150))
    profiles_id = Column(Integer)
    first_name = Column(String(100))
    last_name = Column(String(100))
    biography = Column(String(500))
    phone = Column(String(10))
    gender_id = Column(Integer)
    city_id = Column(Integer)
    birth_date = Column(Date)
    profile_picture = Column(String(500))
    social_links = Column(String(500))
    last_login = Column(TIMESTAMP)
    is_premium = Column(Integer, default = INACTIVE)
    active = Column(Integer, default = ACTIVE)
    registration_date = Column(TIMESTAMP, default= func.current_timestamp())


    def __init__(self, data: dict):
        self.username = data["username"]
        self.email = data["email"]
        self.password = data["password"]
        self.profiles_id = data["profiles_id"]
        self.first_name = data["first_name"]
        self.last_name = data["last_name"]
        self.biography = data.get("biography")
        self.phone = data.get("phone")
        self.gender_id = data.get("gender_id")
        self.city_id = data.get("city_id")
        self.birth_date = data.get("birth_date")
        self.profile_picture = data.get("profile_picture")
        self.social_links = data.get("social_links")
        # self.last_login = data.get("last_login")


    def as_dict(self):
        dates_dict = {
            "birth_date": None,
            "last_login": None, 
            "registration_date": self.registration_date.isoformat()
        }

        return {c.name: getattr(self, c.name)
                if c.name not in dates_dict.keys()
                else dates_dict[c.name]
                for c in self.__table__.columns}
    

