# Class for /ticket/tickets
from ConnectPyse.service import ticket


class TicketsAPI(CWController):
    def __init__(self):
        self.module_url = 'service'
        self.module = 'tickets'
        self._class = ticket.Ticket
        super().__init__()  # instance gets passed to parent object

    def get_ticket_statuses(self):
        return super()._get()

    def create_ticket_status(self, a_ticket_status):
        return super()._create(a_ticket_status)

    def get_ticket_statuses_count(self):
        return super()._get_count()

    def get_ticket_status_by_id(self, ticket_status_id):
        return super()._get_by_id(ticket_status_id)

    def delete_ticket_status_by_id(self, ticket_status_id):
        super()._delete_by_id(ticket_status_id)

    def replace_ticket_status(self, ticket_status_id):
        pass

    def update_ticket_status(self, ticket_id, key, value):
        return super()._update(ticket_id, key, value)

    def merge_ticket_status(self, a_ticket_status, target_ticket_status_id):
        # return super()._merge(a_ticket_status, target_ticket_status_id)
        pass

# get
# create
# count
# search
# getbyid
# delete
# replace
# update
# activities
# count
# timeentries
# count
# scheduleentries
# count
# documents
# count
# products
# count
# configurations
# createconfigurations
# count
# betbyid
# delete
