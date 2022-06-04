from blueprints.modelBlueprint import ModelBlueprint
from controller import companyController, nfseController
from scripts.JsonEndpoint.interface import Interface

class JsonEndpoint(ModelBlueprint):
    company = None
    nfse = None
    schema = None
    requestData = None

    def __init__(self,request,name):
        super().__init__(request,name)
        self.company = companyController.CompanyController()
        self.nfse = nfseController.NfseController()
        self.schema = self.getSchema(self.method)
        self.requestData = self.getRes(self.method)

    def main(self):
        methodList = self.getMethodList()
        validation = Interface().jsonSecurity().main(self.name, methodList,self.method,self.validate,self.requestData)
        
        if(validation != True):
            return validation

        res = methodList[self.name]['function']()
        return self.respond(res[0],res[1])

    def get(self):
        return Interface().jsonView(self.nfse,self.company,self.requestData).main()
    
    def put(self):
        return Interface().jsonAlter(self.nfse,self.company,self.requestData).main()

    def getSchema(self,method):
        return Interface().jsonSecurity().getSchema(method)

    def getRes(self,method):
        resList = {
            'GET':'url',
            'PUT':'json',
        }
        return self.getResLocation(resList[method])

    def getMethodList(self):
        return {
            'find':{'function':self.get,'methods':['GET']},
            'alter':{'function':self.put,'methods':['PUT']},
        }