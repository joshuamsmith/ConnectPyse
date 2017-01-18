import restapi
# Class for /company/contacts/{id}/communications
import connectpyse
from connectpyse.company import contact_communication


class ContactCommunicationsAPI(restapi.Client):

    module_url = 'company/contacts/{}'

    def __init__(self, contact_id):
        super(ContactCommunicationsAPI, self).__init__(
            '{}/{}'.format(connectpyse.API_URL, ContactCommunicationsAPI.module_url.format(contact_id)))

    def get_contact_communications(self, user_params={}):
        json_results = self.communications.get(user_headers=connectpyse.basic_auth, user_params=user_params)
        for json in json_results:
            yield contact_communication.ContactCommunication(json)

    def create_contact_communication(self, a_object):
        try:
            clean_dict = {k: v for k, v in a_object.__dict__.items() if v}
        except Exception as e:
            print(repr(e))
            return False
        json_results = self.communications.post(user_headers=connectpyse.basic_auth, user_data=clean_dict)
        return json_results

    def get_contact_communications_count(self):
        json_results = self.communications.get(the_id='count', user_headers=connectpyse.basic_auth)
        count = json_results['count']
        return count

    def get_contact_communication_by_id(self, contact_communication_id):
        a_contact_communication = contact_communication.ContactCommunication(self.communications.get(the_id=contact_communication_id, user_headers=connectpyse.basic_auth))
        return a_contact_communication

    def delete_contact_communication_by_id(self, contact_communication_id):
        pass

    def replace_contact_communication(self, contact_communication_id):
        pass

    def update_contact_communication(self, contact_communication_id, item, value):
        # build PatchOperation array-dict
        patch_operation = [{
            'op': 'replace',
            'path': item,
            'value': value
        }]
        # call Patch method on API
        json_results = self.communications.patch(the_id=contact_communication_id, user_data=patch_operation, user_headers=connectpyse.basic_auth)
        # return status code
        return json_results

