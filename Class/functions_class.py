from Models.DB_Models.functions_model import Function
from Models.DB_Models.role_permissions_model import RolePermissions
from Models.DB_Models.profiles_model import ProfileModel
from Class.database import Database as DB
from Helpers.basic_helper import data_validation
from Models.process_sql import ProcessSql
import Helpers.constantes as c

class FunctionClass:

    def __init__(self):
        self.session = DB().session
        self.processSql = ProcessSql()

    def create_function(self, data):
        # Validate if function already exits
        function_ = self.processSql.validate_function(data)
        warning_message = c.MESSAGE_IF_EXITS.format(
            "function",
            data["function_name"]
        )

        model_id = self.processSql.create_record(
            function_,
            Function,
            warning_message,
            data
        )
        
        response = {
            "Function_id": model_id
        }
        self.session.close()

        return response
    
    def get_functions(self, id_):
        response = self.processSql.get_records_by_id(
            Function,
            id_
        )
        return response
        
    
    def create_profile(self, data):
        profiles = self.processSql.validate_profile(data)
        warning_message = c.MESSAGE_IF_EXITS.format(
                "profile",
                data["profiles"],
            )
        
        model_id = self.processSql.create_record(
            profiles,
            ProfileModel,
            warning_message,
            data
        )

        response = {
            "Profile_id": model_id
        }

        return response
    
    def get_profile(self, id_):
        response = self.processSql.get_records_by_id(
            ProfileModel,
            id_
        )
        return response


    def create_role_permission(self,data):
        # Validate if relationship exists
        relationship = self.processSql.validate_role_permission(data)
        warning_message = c.MESSAGE_IF_EXITS.format(
                "relationship",
                [data["profiles_id"],  data["functions_id"]],
            )
        
        self.processSql.create_record(
            relationship,
            RolePermissions,
            warning_message,
            data
        )

    def get_role_permission(self, id_):
        response = self.processSql.get_records_by_id(
            RolePermissions,
            id_
        )
        return response

        


        

