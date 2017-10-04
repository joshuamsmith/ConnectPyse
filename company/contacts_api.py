from ..cw_controller import CWController
# Class for /company/contacts
from connectpyse.company import contact


class ContactsAPI(CWController):
    def __init__(self):
        self.module_url = 'company'
        self.module = 'contacts'
        self._class = contact.Contact
        super().__init__()  # instance gets passed to parent object

    def get_contacts(self):
        return super()._get()

    def create_contact(self, a_contact):
        return super()._create(a_contact)

    def get_contacts_count(self):
        return super()._get_count()

    def get_contact_by_id(self, contact_id):
        return super()._get_by_id(contact_id)

    def delete_contact_by_id(self, contact_id):
        super()._delete_by_id(contact_id)

    def replace_contact(self, contact_id):
        pass

    def update_contact(self, contact_id, key, value):
        return super()._update(contact_id, key, value)

    def merge_contact(self, a_contact, target_contact_id):
        # return super()._merge(a_contact, target_contact_id)
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

