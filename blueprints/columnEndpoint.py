from flask import Blueprint, request
from scripts.ColumnEndpoint.ColumnEndpoint import ColumnEndpoint


column_endpoint = Blueprint('column_endpoint',__name__)

@column_endpoint.route('/nfse/<name>',methods=['GET','POST','PUT','DELETE'])
def Column(name):
    return ColumnEndpoint(request, name).main()
