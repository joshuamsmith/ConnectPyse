from ..cw_controller import CWController
# Class for /company/companies
from . import company


class CompaniesAPI(CWController):
    def __init__(self):
        self.module_url = 'company'
        self.module = 'companies'
        self._class = company.Company
        super().__init__()  # instance gets passed to parent object

    def get_companies(self):
        return super()._get()

    def create_company(self, a_company):
        return super()._create(a_company)

    def get_companies_count(self):
        return super()._get_count()

    def get_company_by_id(self, company_id):
        return super()._get_by_id(company_id)

    def delete_company_by_id(self, company_id):
        super()._delete_by_id(company_id)

    def replace_company(self, company_id):
        pass

    def update_company(self, company_id, key, value):
        return super()._update(company_id, key, value)

    def merge_company(self, a_company, target_company_id):
        # return super()._merge(a_company, target_company_id)
        pass
