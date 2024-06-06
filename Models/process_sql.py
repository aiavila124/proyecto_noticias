from Class.database import Database as DB
import Helpers.constantes as c
from sqlalchemy import or_
from Models.DB_Models.plantilla_html import PlantillaHtml
from Models.DB_Models.role_permissions_model import RolePermissions
from Models.DB_Models.functions_model import Function
from Models.DB_Models.profiles_model import ProfileModel

class ProcessSql:
    def __init__(self):
        self.session = DB().session

    def create_record(self, model, model_, warning_message, data):
        if model and model.active == c.ACTIVE:
            raise Warning(warning_message)
            
        
        if model and model.active == c.INACTIVE:
            self.session.query(model_).\
            filter(
                model_.id == model.id
            ).update({
                "active": c.ACTIVE
            })
        
            self.session.commit()

        else:
            model = model_(data)
            self.session.add(model)
            self.session.commit()

        model_id = model.id

        self.session.close()

        return model_id

    def get_html(self, id):
        query = self.session.query(PlantillaHtml)\
            .filter(PlantillaHtml.id == id).first()
        data = query.as_dict()

        self.session.close()
        return data

    
    def validate_role_permission(self, data):
        query = self.session.query(RolePermissions).\
                filter(
                    RolePermissions.functions_id == data["functions_id"],
                    RolePermissions.profiles_id == data["profiles_id"]
                ).first()
        
        self.session.close()
        
        return query
    
    def activate_role_permission(self, permission_id):
        self.session.query(RolePermissions).\
            filter(
                RolePermissions.id == permission_id
            ).update({
                "active": c.ACTIVE
            })
        
        self.session.commit()

    def validate_function(self, data):
        query = self.session.query(Function).\
                filter(
                    or_(
                        Function.function_name.ilike(data["function_name"]),
                        Function.path.ilike(data["path"])
                    )
                ).first()
        
        self.session.close()

        return query
    
    def validate_profile(self, data):
        query = self.session.query(ProfileModel).\
                filter(
                    ProfileModel.profiles.ilike(data["profiles"])
                ).first()
        
        self.session.close()

        return query
    
    def get_records_by_id(self, model, id_):
        model_ = self.session.query(model).filter(
            model.active == c.ACTIVE
        )

        if id_:
            model_ = model_.filter_by(id = id_)


        model_ = model_.all()
        
        json_dict = [row.as_dict() for row in model_]

        self.session.close()

        return json_dict