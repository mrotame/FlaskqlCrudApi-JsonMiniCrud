from cerberus import Validator
from flask import json, Response
from sql.Sqldb import session
import datetime

class Model():
    __response = None
    __requestIsValid = False
    __request = None
    __schema = None
    __userLoginRequired = None
    __dbSession = session
    userSessionExpirationAfterDays = 7
    __datatype = None

    def __init__(self, request,schema, userLoginRequired=False, datatype='json'):
        self.__request = request
        self.__schema = schema
        self.__userLoginRequired = userLoginRequired
        self.__datatype = datatype
        self.validateRequest()

    def respond(self, *args, **kargs):
        validation = self.validateRequest()
        if (validation is not None):
            return validation
        return self.main(*args, **kargs)

    # Override main with the request logic
    def main():
        return "Main must be overrided"

    # ----- Functions -----

    def updateSessionExpireDate(self, user):
        user.expire_date = datetime.datetime.now()+datetime.timedelta(days=self.userSessionExpirationAfterDays)
        self.__dbSession.commit()

    # ----- Validations -----

    def validateRequest(self):
        print("\n Validating \n")
        isValid = self.validateSchema() 

        validations = {
            "requestIsValid":{
                'status':isValid['result'],
                'expected':True,
                'return':{"message":"Invalid requesting json",'errors':isValid['errors']},
                'httpCode':400
                },
            "validateLogin":{
                'status':self.validateLogin(),
                'expected':self.__userLoginRequired,
                'return':{"message":"session invalid or expired."},
                'httpCode':401
                }
            }
        for item in validations:
            if (validations[item]['status'] != validations[item]['expected']): 
                self.setResponse(validations[item]['return'],validations[item]['httpCode'])
                return self.getResponse()
        return None
        
    
    def validateSchema(self):
        result = Validator()
        if self.__datatype == 'json':
            return {'result':result.validate(self.__request.json,self.__schema),'errors':result.errors}
        if self.__datatype == 'url':
            return {'result':True}#result.validate(self.__request.data,self.__schema),'errors':result.errors}
        
        
    def validateLogin(self):
        return True

    # ----- Getters and Setters -----

    def getRequest(self):
        return self.__request

    def setRequestIsValid(self):
        self.__requestIsValid = self.validateRequest()
        return True

    def getRequestIsValid(self):
        return self.__requestIsValid()

    def setResponse(self, data, status):
        self.__response = Response(
            response=json.dumps(data),
            status=status,
            mimetype='application/json'
        )
        return True

    def getResponse(self):
        return self.__response

    def getSchema(self):
        return self.__schema

    def getUserLoginRequired(self):
        return self.__userLoginRequired

    def getDbSession(self):
        return self.__dbSession

    def setDbSession(self, dbSession):
        self.__dbSession = dbSession
        return True
    
        