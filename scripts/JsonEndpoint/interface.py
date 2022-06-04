
from scripts.JsonEndpoint.jsonAlter import JsonAlter
from scripts.JsonEndpoint.jsonSecurity import JsonSecurity
from scripts.JsonEndpoint.jsonView import JsonView

class Interface():
    def jsonSecurity(self):
        return JsonSecurity()

    def jsonView(self,nfse,company,requestData):
        return JsonView(nfse,company,requestData)

    def jsonAlter(self,nfse,company,requestData):
        return JsonAlter(nfse,company,requestData)