from Class.database import Database as DB
from Models.DB_Models.plantilla_html import PlantillaHtml

class ProcessSql:
    def __init__(self):
        self.session = DB().session

    def get_html(self, id):
        query = self.session.query(PlantillaHtml)\
            .filter(PlantillaHtml.id == id).first()
        data = query.as_dict()

        self.session.close()
        return data