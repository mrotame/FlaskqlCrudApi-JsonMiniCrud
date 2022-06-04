class ColumnView():
    requestData = None
    company = None
    nfse = None

    def __init__(self,nfse,company,requestData):
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
        
        res_condition = {
            'cod_verif': self.requestData.get('cod_verif'),
            'id_company':company.id
        }
        nfse_res = self.nfse.readMany(res_condition) 
        
        final_result = []

        for item in nfse_res:
            final_result.append({
                "dt_emissao": item.dt_emissao,
                "num_nfse": item.num_nfse,
                "cod_verif": item.cod_verif,
                "cnpj_prest": item.cnpj_prest 
            })

        if (nfse_res is None or len(final_result)==0):
            return None

        return {
            'result':final_result
        }