import json
import re
import hashlib
import jwt
import os
from marshmallow import ValidationError
from datetime import datetime, timedelta
from Helpers.constantes import FIELD_VALIDATION

def get_data(data):
    try:
        return json.loads(data)
    except:
        return data
    
def data_validation(model, data):
    try:
        model.load({**data})
        
    except ValidationError as err:
        key, value = list(err.messages.items())[0]

        raise Warning(FIELD_VALIDATION.format(key, value[0]))
    
def hash_password(password):
    password = password.encode('utf-8')
    hash_object = hashlib.sha256(password)
    password_hash = hash_object.hexdigest()

    return password_hash

def validate_password(password):
    patron = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]+$'
    # Comprobar si la contraseña cumple con el patrón
    if re.match(patron, password):
        return True
    else:
        raise Warning("Password format not valid")

def validate_no_spaces(text):
    if " " in text:
        raise Warning("Username must not contain spaces")
    else:
        return True
    
def expire_date(hour):
    date = datetime.now() + timedelta(hours=hour)

    return date

def get_token(data):
    payload = {**data, 'exp': datetime.now() + timedelta(days=1)}
    print("payload", datetime.now() + timedelta(hours=1))
    print("payload", payload)
    key = os.getenv('SECRET_KEY')
    token = jwt.encode(payload, key, algorithm = "HS256")

    return str(token).split("'")[1]

