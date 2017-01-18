import restapi
# Class for /company/contacts
import connectpyse
from connectpyse.company import contact


class ContactsAPI(restapi.Client):

    module_url = 'company'

    def __init__(self):
        super(ContactsAPI, self).__init__('{}/{}'.format(connectpyse.API_URL, ContactsAPI.module_url))

    def get_contacts(self, user_params={}):
        json_results = self.contacts.get(user_headers=connectpyse.basic_auth, user_params=user_params)
        for json in json_results:
            yield contact.Contact(json)

    def create_contact(self):
        pass

    def get_contacts_count(self):
        json_results = self.contacts.get(the_id='count', user_headers=connectpyse.basic_auth)
        count = json_results['count']
        return count

    def get_contact_by_id(self, contact_id):
        a_contact = contact.Contact(self.contacts.get(the_id=contact_id, user_headers=connectpyse.basic_auth))
        return a_contact

    def delete_contact_by_id(self, contact_id):
        pass

    def replace_contact(self, contact_id):
        pass

    def update_contact(self, contact_id, item, value):
        # build PatchOperation dict
        patch_operation = [{
            'op': 'replace',
            'path': item,
            'value': value
        }]
        # call Patch method on API
        json_results = self.contacts.patch(the_id=contact_id, user_data=patch_operation, user_headers=connectpyse.basic_auth)
        # return status code
        return json_results

    def merge_contact(self, contact_id):
        pass

    def validate_portal_credentials(self, a_contact):
        for comm_items in a_contact.communicationItems:
            if comm_items['defaultFlag'] and comm_items['communicationType'] == 'Email':
                email = comm_items['value']
                break
        dict_post = {'email': email, 'password': a_contact.portalPassword}
        json_results = self.contacts.post(user_data=dict_post, user_headers=connectpyse.basic_auth)
        status_code = json_results.status_code
        return status_code

