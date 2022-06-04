
class ColumnAlter():
    nfse = None
    company = None
    requestData = None

    def __init__(self,nfse,company,requestData):
        self.nfse = nfse
        self.company = company
        self.requestData = requestData

    def main(self):
        res = self.alterFromDb()

        if (not res):
            return ({'message':'Could not update. Registry not found'},400)

        return ({'message':'successfully changed'},200)

    def alterFromDb(self):
        id_company = self.company.readOne({'cnpj':self.requestData['company_cnpj']})
        
        if (id_company is None):
            return False

        dataToQuery = {
            'id_company':id_company.id,
            'cod_verif': self.requestData['cod_verif_old']
        }
        dataToUpdate = {
            'cod_verif': self.requestData['cod_verif_new'],
            'json_nota': self.requestData['json_new'],
            'xml_nota': self.requestData['xml_new']
        }
        update = self.nfse.updateOne(dataToQuery, dataToUpdate)

        if (not update):
            return False
        
        return True