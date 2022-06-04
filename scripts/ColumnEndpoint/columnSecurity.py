class ColumnSecurity():
    def __init__(self):
        pass
    
    def main(self, name, methodList, method, validator,requestData):
        if (not self.valideUrl(name, methodList)) :
            return ({'message':"invlaid url"},400)

        if (not self.validateHttpMethod(name, method, methodList)) :
            return ({'message':'Method not allowed'},405)

        validation_result = self.validateSchema(validator,self.getSchema(method),requestData)
        if (validation_result['result'] != True) :
            return (
                {'message':'Invalid request, check input parameters',
                'errors':validation_result['errors']
                },
                400
            )
        
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
                'POST':{
                    'company_cnpj':{'type':'string','required':True} ,
                    'dt_emissao':{'type':'string','required':True},
                    'num_nfse':{'type':'string','required':True},
                    'cod_verif':{'type':'string','required':True},
                    'cnpj_prest':{'type':'string','required':True},
                    'xml_nota':{'type':'string','required':True},
                    'json_nota':{'type':'dict','required':True}
                },
                'PUT': {
                    'company_cnpj':{'type':'string','required':True},
                    'cod_verif_old':{'type':'string','required':True},
                    'cod_verif_new':{'type':'string','required':True},
                    'xml_new':{'type':'string','required':True},
                    'json_new':{'type':'dict','required':True}
                },
                'GET':{
                    'company_cnpj':{'type':'string','required':True},
                    'cod_verif':{'type':'string','required':True}
                },
                'DELETE': {
                    'company_cnpj':{'type':'string','required':True},
                    'cod_verif':{'type':'string','required':True},
                    'areYouSure':{'type':'boolean','required':True}
                }
            }
        return schemaList[method]