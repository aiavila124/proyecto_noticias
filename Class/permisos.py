from Class.database import Database as DB
from Models.DB_Models.role_permissions_model import RolePermissions
from Models.DB_Models.functions_model import Function
import Helpers.constantes as c

class Permisos:
    def __init__(self):
        self.session = DB().session
        self.permisos = self.session.query(RolePermissions)

    def get_permisos(self, profile_id, path):
        
        function_id = self.get_id_function(path)
        
        query = self.session.query(RolePermissions).filter(
            RolePermissions.functions_id == function_id,
            RolePermissions.profiles_id == profile_id,
            RolePermissions.active == c.ACTIVE
        ).first()

        self.session.close()

        if not query:
            raise Warning(c.NOT_PERMMITED)
        

    def get_id_function(self, path):
        query = self.session.query(Function).filter(
            Function.path == path
        ).first()
        self.session.close()
        
        if not query:
            raise Warning(c.FUNCTION_NOT_FOUND)

        return query.id
    
    def validate_permission(self, path):
        query = self.session.query(Function).filter(
            Function.id == self.get_id_function(path),
            Function.active == c.ACTIVE
        ).first()

        self.session.close()

        return query.need_permission == c.ACTIVE
    