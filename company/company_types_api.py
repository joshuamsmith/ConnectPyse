from ..cw_controller import CWController
# Class for /company/companies/types
from connectpyse.company import company_type


class CompanyTypeAPI(CWController):
    def __init__(self):
        self.module_url = 'company'
        self.module = 'companies/types'
        self._class = company_type.CompanyType
        super().__init__()  # instance gets passed to parent object

    def get_company_types(self):
        return super()._get()

    def create_company_type(self, a_company_type):
        return super()._create(a_company_type)

    def get_company_types_count(self):
        return super()._get_count()

    def get_company_type_by_id(self, company_type_id):
        return super()._get_by_id(company_type_id)

    def delete_company_type_by_id(self, company_type_id):
        super()._delete_by_id(company_type_id)

    def replace_company_type(self, company_type_id):
        pass

    def update_company_type(self, company_type_id, key, value):
        return super()._update(company_type_id, key, value)

    def merge_company_type(self, a_company_type, target_company_type_id):
        # return super()._merge(a_company_type, target_company_type_id)
        pass
