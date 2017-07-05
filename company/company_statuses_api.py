from ..cw_controller import CWController
# Class for /company/companies/statuses
from connectpyse.company import company_status


class CompanyStatusAPI(CWController):
    def __init__(self):
        self.module_url = 'company'
        self.module = 'companies/statuses'
        self._class = company_status.CompanyStatus
        super().__init__()  # instance gets passed to parent object

    def get_company_statuses(self):
        return super()._get()

    def create_company_status(self, a_company_status):
        return super()._create(a_company_status)

    def get_company_statuses_count(self):
        return super()._get_count()

    def get_company_status_by_id(self, company_status_id):
        return super()._get_by_id(company_status_id)

    def delete_company_status_by_id(self, company_status_id):
        super()._delete_by_id(company_status_id)

    def replace_company_status(self, company_status_id):
        pass

    def update_company_status(self, company_id, key, value):
        return super()._update(company_id, key, value)

    def merge_company_status(self, a_company_status, target_company_status_id):
        # return super()._merge(a_company_status, target_company_status_id)
        pass
