from flask import Blueprint, request, Response, json
from cerberus import Validator

class ModelBlueprint():
    request = None
    method = None
    name = None
    __response = None

    def __init__(self, request, name):
        self.request = request
        self.name = name
        self.method = request.method

    def validate(self,schema,request=None):
        if(request is None):
            request=self.request.json
        result = Validator()
        return {'result':result.validate(request,schema),'errors':result.errors}

    def respond(self,data,status):
        self.setResponse(data,status)
        return self.getResponse()

    def setResponse(self, data, status):
        self.__response = Response(
            response=json.dumps(data),
            status=status,
            mimetype='application/json'
        )
        return True

    def getResponse(self):
        return self.__response

    def getResLocation(self,location):
        if (location == 'json'):
            res = self.request.json
        if (location == 'url'):
            res = self.request.args
    
        return res

    

    