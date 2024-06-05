import traceback
from Class.response import Response
from Class.users_class import UsersClass
from Class.permisos import Permisos

def http(func):
    def wrapper(*args, **kwargs):
        
        try:
            event = args[0]
            
            if Permisos().validate_permission(event["rawPath"]):
                token = event["headers"]["authorization"].split(" ")[1]
                UsersClass(token).validate_user()
                user = UsersClass(token).get_user()
                Permisos().get_permisos(user.profiles_id, event["rawPath"])
                
            response = func(*args, **kwargs)
            
        except Warning as w:
            print(str(w))
            print(type(w).__name__)
            print(traceback.extract_tb(w.__traceback__))
            response = Response("BAD_REQUEST", str(w))

        except KeyError as k:
            print(str(k))
            print(type(k).__name__)
            print(traceback.extract_tb(k.__traceback__))
            response = Response("BAD_REQUEST", str(k))

        except Exception as e:
            print(str(e))
            print(type(e).__name__)
            print(traceback.extract_tb(e.__traceback__))
            response = Response("INTERNAL_ERROR")  

        finally:
            return response.create_response()

    return wrapper