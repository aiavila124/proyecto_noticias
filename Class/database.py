from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import QueuePool
import os

class Database():
    base_class = declarative_base()

    def __init__(self):
        connection_string = self.__get_connection_strings()
        self.__engine = create_engine(connection_string, poolclass=QueuePool)
        self.__session_maker = sessionmaker(bind=self.__engine)
        self.session = self.__session_maker()

    def __get_connection_strings(self):

        string = "mysql+pymysql://{}:{}@{}/{}".format(
            os.getenv('DB_USER'),
            os.getenv('DB_PASSWORD'),
            os.getenv('DB_HOST'),
            os.getenv('DB_NAME'))
        return string
    
    

