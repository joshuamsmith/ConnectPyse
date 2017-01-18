import restapi
# Class for /company/companies/{id}/managementSummaryReports
import connectpyse
from connectpyse.company import company_management_summary_report


class CompanyManagementSummaryReportsAPI(restapi.Client):

    module_url = 'company/companies/{}'

    def __init__(self, company_id):
        super(CompanyManagementSummaryReportsAPI, self).__init__(
            '{}/{}'.format(connectpyse.API_URL, CompanyManagementSummaryReportsAPI.module_url.format(company_id)))

    def get_company_management_summary_reports(self, user_params={}):
        json_results = self.managementSummaryReports.get(user_headers=connectpyse.basic_auth, user_params=user_params)
        for json in json_results:
            yield company_management_summary_report.CompanyManagementSummaryReport(json)

    def create_company_management_summary_report(self):
        pass

    def get_company_management_summary_reports_count(self):
        json_results = self.managementSummaryReports.get(the_id='count', user_headers=connectpyse.basic_auth)
        count = json_results['count']
        return count

    def get_company_management_summary_report_by_id(self, company_id):
        an_instance = company_management_summary_report.CompanyManagementSummaryReport(
            self.managementSummaryReports.get(the_id=company_id, user_headers=connectpyse.basic_auth))
        return an_instance

    def delete_company_management_summary_report_by_id(self, company_id):
        pass

    def replace_company_management_summary_report(self, company_id):
        pass

    def update_company_management_summary_report(self, company_id):
        pass

    def merge_company_management_summary_report(self, company_id):
        pass
