from datetime import datetime

class ColumnAdd():
    nfse = None
    company = None
    request = None

    def __init__(self,nfse,company,requestData):
        self.nfse = nfse
        self.company = company
        self.requestData = requestData

    def main(self):
        to_date = lambda s: datetime.strptime(s, '%Y-%m-%d')
        if (not self.insertNewIntoDb()):
            return ({'message':'Company not found. Verify the inserted cnpj'},400)
        return ({'message':'Nfse created'},200)

    def insertNewIntoDb(self):
        toInsert = self.requestData
        company_res = self.company.readOne({'cnpj':self.requestData['company_cnpj']})
        toInsert.pop('company_cnpj')
        if (company_res is None):
            return False

        toInsert['id_company'] = company_res.id
        self.nfse.createOne(toInsert)  
        return True 