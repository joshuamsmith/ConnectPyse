from ..cw_controller import CWController
# Class for /company/contacts/{id}/communications
from connectpyse.company import contact_communication


class ContactCommunicationsAPI(CWController):
    def __init__(self, contact_id):
        self.module_url = 'company'
        self.module = 'contacts/{}/communications'.format(contact_id)
        self._class = contact_communication.ContactCommunication
        super().__init__()  # instance gets passed to parent object

    def get_contact_communications(self):
        return super()._get()

    def create_contact_communication(self, a_contact_communication):
        return super()._create(a_contact_communication)

    def get_contact_communications_count(self):
        return super()._get_count()

    def get_contact_communication_by_id(self, item_id):
        return super()._get_by_id(item_id)

    def delete_contact_communication_by_id(self, item_id):
        super()._delete_by_id(item_id)

    def replace_contact_communication(self, item_id):
        pass

    def update_contact_communication(self, item_id, key, value):
        return super()._update(item_id, key, value)
