import restapi
# Class for /company/companies
import connectpyse


class CWController(restapi.Client):

    def __init__(self):
        self.module_url = ''
        super().__init__('{}/{}'.format(connectpyse.API_URL, self.module_url))

    def get_companies(self, user_params={}):
        json_results = self.companies.get(user_headers=connectpyse.basic_auth, user_params=user_params)
        for json in json_results:
            yield company.Company(json)

    def create_company(self):
        pass

    def get_companies_count(self):
        json_results = self.companies.get(the_id='count', user_headers=connectpyse.basic_auth)
        count = json_results['count']
        return count

    def get_company_by_id(self, company_id):
        a_company = company.Company(self.companies.get(the_id=company_id, user_headers=connectpyse.basic_auth))
        return a_company

    def delete_company_by_id(self, company_id   ):
        pass

    def replace_company(self, company_id):
        pass

    def update_company(self, company_id):
        pass

    def merge_company(self, company_id):
        pass
