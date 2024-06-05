from enum import Enum

REQUEST = {
    "OK": {
        "code": 200, 
        "message": "Operación exitosa."
    },
    "REGISTER": {
        "code": 201, 
        "message": "El registro ha sido exitoso."    
    },
    "UPDATE": {
        "code": 201, 
        "message": "La actualización ha sido exitosa."
    },
    "BAD_REQUEST": {
        "code": 400, 
        "message": "Ha ocurrido un error al procesar los datos."
    },
    "UNAUTHORIZED": {
        "code": 401, 
        "message": "Ha ocurrido un error de autenticación."
    },
    "FORBIDDEN": {
        "code": 403, 
        "message": "No tiene permisos para realizar esta operación."
    },
    "NOT_FOUND": {
        "code": 404, 
        "message": "No se ha encontrado el recurso solicitado."
    },
    "INTERNAL_ERROR": {
        "code": 500, 
        "message": "Ha ocurrido un error inesperado."
    }
}

# Active constants
ACTIVE = 1
INACTIVE = 0

# Message constants
VALIDATE_USER = "Ya existe una cuenta con el usuario proporcionado."
FIELD_VALIDATION = "Error in field {0}: {1}"
INCORRECT_CREDENTIALS = "Credenciales incorrectas."
NOT_PERMMITED = "No tiene permisos para realizar esta operación."
TOKEN_EXPIRED = "The incoming token has expired."
FUNCTION_NOT_FOUND = "Function not found"

# mails subjects
CREATE_USER_CONFIRMATION = 1