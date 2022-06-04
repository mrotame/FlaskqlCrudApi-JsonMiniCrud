from sqlalchemy.dialects.postgresql import JSON
from sqlalchemy import String

class JsonView():
    requestData = None
    company = None
    nfse = None

    def __init__(self, nfse , company, requestData):
        self.requestData = requestData
        self.company = company
        self.nfse = nfse

    def main(self):
        res = self.getFromDb()
        if (res is None):
            return({'message':'Registry not found'},400)
        res['message'] = 'success'
        return (res,200)
    
    def getFromDb(self):
        company_condition = {
            'cnpj': self.requestData.get('company_cnpj'),
        }
        
        company = self.company.readOne(company_condition)
        if (company is None):
            return None
        print('\n\n', self.requestData.get('name_field'),'\n\n')
        res_condition = {
            
            'id_company':company.id,
            'json_nota': {
                'name_field':self.requestData.get('name_field'),
                'value':self.requestData.get('value')
            }
        }
        nfse_res = self.nfse.readMany_fromJson(res_condition)

        final_result = []
        for item in nfse_res:
            final_result.append({
                'num_nfse':item.json_nota['numeroNfe'],
                'cod_verif':item.json_nota['codVerificacao'],
                'cnpj_prest':item.json_nota['cnpjCpfPrestador']
            })
        if (nfse_res is None or len(final_result)==0):
            return None
        
        return {
            'Notas encontradas':final_result
        }