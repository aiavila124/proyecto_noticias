from sqlalchemy import func, String, Integer, Column, Date, TIMESTAMP, TEXT
from Class.database import Database as DB
from Helpers.constantes import ACTIVE


class ProfileModel(DB.base_class):
    __tablename__ = 'profiles'

    id = Column(Integer, primary_key=True)
    profiles = Column(String(45))
    active = Column(Integer, default = ACTIVE)
    registration_date = Column(TIMESTAMP, default= func.current_timestamp())

    def as_dict(self):
        dict_ = {c.name: getattr(self, c.name) for c in self.__table__.columns}
        dict_["registration_date"] = self.registration_date.isoformat()
        return dict_