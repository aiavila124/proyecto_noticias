from sqlalchemy import func, String, Integer, Column, Date, TIMESTAMP, TEXT
from Class.database import Database as DB
from Helpers.constantes import ACTIVE, INACTIVE


class PlantillaHtml(DB.base_class):
    __tablename__ = 'plantillas_html'

    id = Column(Integer, primary_key=True)
    asunto = Column(String(100))
    html = Column(TEXT)
    active = Column(Integer, default = ACTIVE)
    registration_date = Column(TIMESTAMP, default= func.current_timestamp())

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}