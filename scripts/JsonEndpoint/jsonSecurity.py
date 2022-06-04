class JsonSecurity():
    def __init__(self):
        pass
    
    def main(self, name, methodList, method, validator,requestData):
        if (not self.valideUrl(name, methodList)) :
            return ({'message':"invlaid url"},400)

        if (not self.validateHttpMethod(name, method, methodList)) :
            return ({'message':'Method not allowed'},405)

        validation_result = self.validateSchema(validator,self.getSchema(method),requestData)
        if (not validation_result['result']) :
            return ({'message':'Invalid request, check input parameters','errors':validation_result['errors']},400)
        
        return True

    def valideUrl(self, name, methodList):
        # Validação da url
        if (name not in methodList):
            return False
        return True

    def validateHttpMethod(self,name ,method, methodList):
        # Validação do metodo HTTP
        if (method not in methodList[name]['methods']):
            return False
        return True

    def validateSchema(self, validator,schema,requestData):
        # Validação dos parametros da request
        validation_result = validator(schema,requestData)
        if (not validation_result['result']):
            return {'result':False,'errors':validation_result['errors']}
        return {'result':True}

    def getSchema(self,method):
        schemaList = {
            'GET':{
                    'company_cnpj':{'type':'string','required':True},
                    'value':{'type':'string','required':True},
                    'name_field':{'type':'string','required':True}
                },
            'PUT': {
                'company_cnpj':{'type':'string','required':True},
                'name_field':{'type':'string','required':True},
                'value_old':{'type':'string','required':True},
                'value_new': {'type':'string','required':True}
            }
                
        }
        return schemaList[method]