from flask import Blueprint, request

from scripts.JsonEndpoint.jsonEndpoint import JsonEndpoint


json_endpoint = Blueprint('json_endpoint',__name__)

@json_endpoint.route('/json/<name>',methods=['GET','PUT'])
def Json(name):
    return JsonEndpoint(request, name).main()

