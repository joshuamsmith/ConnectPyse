from ..cw_controller import CWController
# Class for /company/companies/{id}/managementSummaryReports
from ConnectPyse.company import company_management_summary_reports


class CompanyManagementSummaryReportsAPI(CWController):
    def __init__(self, company_id):
        self.module_url = 'company'
        self.module = 'companies/{}/managementSummaryReports'.format(company_id)
        self._class = company_management_summary_reports.CompanyManagementSummaryReport
        super().__init__()  # instance gets passed to parent object

    def get_managementSummaryReports(self):
        return super()._get()

    def create_managementSummaryReport(self, a_managementSummaryReport):
        return super()._create(a_managementSummaryReport)

    def get_managementSummaryReports_count(self):
        return super()._get_count()

    def get_managementSummaryReport_by_id(self, managementSummaryReport_id):
        return super()._get_by_id(managementSummaryReport_id)

    def delete_managementSummaryReport_by_id(self, managementSummaryReport_id):
        super()._delete_by_id(managementSummaryReport_id)

    def replace_managementSummaryReport(self, managementSummaryReport_id):
        pass

    def update_managementSummaryReport(self, managementSummaryReport_id, key, value):
        return super()._update(managementSummaryReport_id, key, value)
