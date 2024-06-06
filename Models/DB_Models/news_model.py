from sqlalchemy import func, String, Integer, Column, Date, TIMESTAMP
from Class.database import Database as DB
import Helpers.constantes as c

class News(DB.base_class):
    __tablename__ = 'news'

    id = Column(Integer, primary_key=True)
    title = Column(String(100))
    content = Column(String(10000))
    users_id = Column(Integer)
    category_id = Column(Integer)
    featured_image = Column(String(500))
    status_id = Column(Integer, default = 1)
    summary = Column(String(200))
    view_count = Column(Integer, default = 0)
    comments_enabled = Column(Integer, default = c.ACTIVE)
    last_update = Column(TIMESTAMP, default= func.current_timestamp())
    active = Column(Integer, default = c.ACTIVE)
    registration_date = Column(TIMESTAMP, default= func.current_timestamp())

    def __init__(self, data: dict):
        self.title = data["title"]
        self.content = data["content"]
        self.users_id = data["users_id"]
        self.category_id = data["category_id"]
        self.featured_image = data["featured_image"]
        self.status_id = data["status_id"]
        self.summary = data["summary"]
