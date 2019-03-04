from connectpyse import restapi
# Class for /company/agreements
from connectpyse.finance import agreement


class AgreementsAPI(restapi.Client):

    module_url = 'finance'

    def __init__(self, base_url):
        super(AgreementsAPI, self).__init__('{}/{}'.format(base_url, AgreementsAPI.module_url))

    def get_agreements(self, user_headers, user_params=None):
        json_results = self.agreements.get(user_headers=user_headers, user_params=user_params)
        for json in json_results:
            yield agreement.Agreement(json)

    def create_agreement(self, a_agreement):
        pass

    def get_agreements_count(self, user_headers):
        json_results = self.agreements.get(the_id='count', user_headers=user_headers)
        count = json_results['count']
        return count

    def get_agreement_by_id(self, user_headers, agreement_id):
        a_agreement = agreement.Agreement(self.agreements.get(the_id=agreement_id, user_headers=user_headers))
        return a_agreement

    def delete_agreement_by_id(self, agreement_id   ):
        pass

    def replace_agreement(self, agreement_id):
        pass

    def update_agreement(self, agreement_id):
        pass

    def merge_agreement(self, agreement_id):
        pass

    def create_configuration_association(self, user_headers, agreement_id, config_id):
        # /agreements/{id}/configurations
        self.root_path = self.root_path + '/agreements/{}'.format(agreement_id)

        dict_post = {'id': config_id}
        json_results = self.configurations.post(user_data=dict_post, user_headers=user_headers)
        #      status_code = json_results.status_code
        return json_results

    def get_agreement_configurations(self):
        pass
