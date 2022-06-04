from scripts.ColumnEndpoint.columnView import ColumnView
from scripts.ColumnEndpoint.columnAdd import ColumnAdd
from scripts.ColumnEndpoint.columnAlter import ColumnAlter
from scripts.ColumnEndpoint.columnDelete import ColumnDelete
from scripts.ColumnEndpoint.columnSecurity import ColumnSecurity

class Interface():
    def columnView(self,nfse,company,requestData):
        return ColumnView(nfse,company,requestData)

    def columnAdd(self,nfse,company,requestData):
        return ColumnAdd(nfse,company,requestData)

    def columnAlter(self,nfse,company,requestData):
        return ColumnAlter(nfse,company,requestData)

    def columnDelete(self,nfse,company,requestData):
        return ColumnDelete(nfse,company,requestData)

    def columnSecurity(self):
        return ColumnSecurity()
