from Models.DB_Models.news_model import News
from Class.database import Database as DB
from Class.users_class import UsersClass
from Class.fields_validator import NewsValidator
from Helpers.basic_helper import data_validation


class NewsClass:

    def __init__(self, token = ""):
        self.session = DB().session
        if token:
            self.user = UsersClass(token).get_user()
    
    def create_news(self, data):

        data_validation(NewsValidator(),data)


        data["users_id"] = self.user.id


        new = News(data)
        self.session.add(new)
        self.session.commit()

        self.session.close()