from sqlalchemy import func, String, Integer, Column, Date, TIMESTAMP
from Class.database import Database as DB
from Helpers.constantes import ACTIVE, INACTIVE

class RolePermissions(DB.base_class):
    __tablename__ = 'role_permissions'

    id = Column(Integer, primary_key=True)
    profiles_id = Column(Integer)
    functions_id = Column(Integer)
    active = Column(Integer, default = ACTIVE)
    registration_date = Column(TIMESTAMP, default= func.current_timestamp())

    def __init__(self, data: dict):
        self.profiles_id = data["profiles_id"]
        self.functions_id = data["functions_id"]


    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}