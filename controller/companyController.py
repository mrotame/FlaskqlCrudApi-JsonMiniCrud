from controller.modelController import ModelController
from sql.models.company import Company

class CompanyController(ModelController):
    def __init__(self):
        self.table = Company

