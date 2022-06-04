
class JsonAlter():
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
            'json_nota':{
                'name_field':self.requestData['name_field'],
                'value_old':self.requestData['value_old'],
                'value_new':self.requestData['value_new']
            }
        }

        update = self.nfse.updateOne_fromJson(dataToQuery)

        if (not update):
            return False
        
        return True