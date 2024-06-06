from sqlalchemy import func, String, Integer, Column, Date, TIMESTAMP
from Class.database import Database as DB
from Helpers.constantes import ACTIVE

class Function(DB.base_class):
    __tablename__ = 'functions'

    id = Column(Integer, primary_key=True)
    function_name = Column(String(100))
    path = Column(String(100))
    need_permission = Column(Integer, default = ACTIVE)
    active = Column(Integer, default = ACTIVE)
    registration_date = Column(TIMESTAMP, default= func.current_timestamp())

    def __init__(self, data: dict):
        self.function_name = data["function_name"]
        self.path = data["path"]
        self.need_permission = data["need_permission"]

    def as_dict(self):
        data = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        data["registration_date"] = self.registration_date.isoformat()
        return data
