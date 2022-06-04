from sql.models.nfse import Nfse
from controller.modelController import ModelController
from sqlalchemy import String

class NfseController(ModelController):
    def __init__(self):
        self.table = Nfse

    def readOne_fromJson(self, condition):
        print('\n\n',condition,'\n\n')
        return self.session.query(self.table).filter(
            self.table.id_company == condition['id_company'],
            self.table.json_nota[condition['json_nota']['name_field']].astext.cast(String) == \
                condition['json_nota']['value']
        ).first()

    def readMany_fromJson(self, conditions):
        print('\n\n',conditions,'\n\n')
        return self.session.query(self.table).filter(
            self.table.id_company == conditions['id_company'],
            self.table.json_nota[conditions['json_nota']['name_field']].astext.cast(String) == \
                conditions['json_nota']['value']
        )

    def updateOne_fromJson(self,toChange):
        row = self.readOne_fromJson({
            'id_company':toChange['id_company'],
            'json_nota': {
                'name_field':toChange['json_nota']['name_field'],
                'value':toChange['json_nota']['value_old']
            }
        })

        if (row is None):
            return False

        row.json_nota[toChange['json_nota']['name_field']] = toChange['json_nota']['value_new']
        self.session.commit()
        return True

        
