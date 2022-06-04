class ColumnDelete():
    nfse = None
    company = None
    requestData = None

    def __init__(self,nfse,company,requestData):
        self.nfse = nfse
        self.company = company
        self.requestData = requestData

    def main(self):
        if(not self.requestData['areYouSure']):
            return ({'You must be sure before deleting'},200)

        res = self.deleteFromDb()
        if(not res):
            return ({"message":"Registry not found"},400)
        return ({"message":"Registry deleted"},200)
    
    def deleteFromDb(self):
        toQuery = {
            'id_company':self.company.readOne({'cnpj':self.requestData['company_cnpj']}).id,
            'cod_verif':self.requestData['cod_verif'],
        }
        res = self.nfse.delete(toQuery)
        if(not res):
            return False

        return True 