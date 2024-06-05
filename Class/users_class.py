import jwt
import os
from datetime import datetime
from Models.DB_Models.users_model import Users
from sqlalchemy import or_
from Class.database import Database as DB
import Helpers.constantes as c
from Class.fields_validator import UserValidator
from Helpers.basic_helper import (
    data_validation, hash_password, get_token
)
from Helpers.send_mail import send_mail
from Models.process_sql import ProcessSql
from Models.DB_Models.functions_model import Function

class UsersClass:
    def __init__(self, token = ""):
        self.session = DB().session
        self.users = self.session.query(Users)
        self.process = ProcessSql()
        self.token = token
        # self.user_id = self.get_user().id

    def create_user(self, data):
        # Validar si el usuario ya existe
        query = self.users.filter(
            or_(
                Users.username == data["username"],
                Users.email == data["email"]
            ),
            Users.active == c.ACTIVE
            ).first()
        
        if query:
            raise Warning(c.VALIDATE_USER)
        
        # Validación de datos
        data_validation(UserValidator(), data)

        data["password"] = hash_password(data["password"])

        user = Users(data)
        self.session.add(user)
        self.session.commit()

        # Enviar correo de confirmación
        html = self.process.get_html(c.CREATE_USER_CONFIRMATION)
        
        send_mail(user.email, 
                      html["asunto"],
                      html["html"].format(
                          full_name = f"{user.first_name} {user.last_name}",
                          username = user.username,
                          ruta_premium = "http://localhost:3000/get_filter_users",
                          ruta_main_page = "http://localhost:3000/get_filter_users"
                      ))

        self.session.close()
        
        return user
    
    def get_filter_users(self, data):

        query = self.users

        page = data["current_page"]
        per_page = data["per_page"]
        
        # incluye el primero y no el ultimo
        query = query.slice(per_page*(page-1),page * per_page).all()
        # query = query.limit(per_page).offset(per_page*(page-1)).all()

        as_dict = [user.as_dict() for user in query]

        self.session.close()

        return as_dict
    
    def get_token(self, data):

        # Validar si el usuario existe
        query = self.users.filter(
            or_(
                Users.username == data["username"],
                Users.email == data["username"]
            ),
            Users.active == c.ACTIVE,
            Users.password == hash_password(data["password"])
            ).first()
        
        self.session.close()
        
        if not query:
            raise Warning(c.INCORRECT_CREDENTIALS)
        
        
        return get_token(data)

    def get_user(self):

        username = self.validate_user()
        user = self.users.filter(
            or_(
                Users.username == username,
                Users.email == username
            )
        ).first()


        self.session.close()

        return user
    
    def validate_user(self):

        key = os.getenv('SECRET_KEY')
        
        try:     
            payload = jwt.decode(self.token, key, algorithms = ["HS256"])
            return payload["username"]

        except jwt.ExpiredSignatureError:
            raise Warning(c.TOKEN_EXPIRED)
        
        except jwt.exceptions.DecodeError:
            raise Warning(c.INCORRECT_CREDENTIALS)
        
        except jwt.InvalidTokenError:
            raise Warning(c.INCORRECT_CREDENTIALS)
    
        
        
       


        
        