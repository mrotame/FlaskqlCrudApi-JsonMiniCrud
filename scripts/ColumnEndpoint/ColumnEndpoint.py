from controller import companyController, nfseController
from blueprints.modelBlueprint import ModelBlueprint
from scripts.ColumnEndpoint.interface import Interface

class ColumnEndpoint(ModelBlueprint):
    company = None
    nfse = None
    schema = None
    requestData = None

    def __init__(self,request, name):
        
        super().__init__(request,name)
        self.company = companyController.CompanyController()
        self.nfse = nfseController.NfseController()
        self.schema = self.getSchema(self.method)
        self.requestData = self.getRes(self.method)
        
    def main(self):
        methodList = self.getMethodList()

        validation = Interface().columnSecurity().main(self.name, methodList,self.method,self.validate,self.requestData)
        if(validation != True):
            return validation           

        res = methodList[self.name]['function']()
        return self.respond(res[0],res[1])

    def get(self):
        return Interface().columnView(self.nfse,self.company,self.requestData).main()

    def post(self):
        return Interface().columnAdd(self.nfse,self.company,self.requestData).main()
    
    def put(self):
        return Interface().columnAlter(self.nfse,self.company,self.requestData).main()

    def delete(self):
        return Interface().columnDelete(self.nfse,self.company,self.requestData).main()

    def getSchema(self,method):
        return Interface().columnSecurity().getSchema(method)

    def getRes(self,method):
        resList = {
            'GET':'url',
            'POST':'json',
            'PUT':'json',
            'DELETE':'json',
        }
        return self.getResLocation(resList[method])

    def getMethodList(self):
        return {
            'find':{'function':self.get,'methods':['GET']},
            'insert':{'function':self.post,'methods':['POST']},
            'alter':{'function':self.put,'methods':['PUT']},
            'delete':{'function':self.delete,'methods':['DELETE']}
        }