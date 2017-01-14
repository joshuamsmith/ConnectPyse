import restapi
# Class for /ticket/tickets
import connectpyse
from connectpyse.service import ticket


class TicketsAPI(restapi.Client):

    module_url = 'service'

    def __init__(self):
        super(TicketsAPI, self).__init__('{}/{}'.format(connectpyse.API_URL, TicketsAPI.module_url))

    def get_tickets(self, user_params={}):
        json_results = self.tickets.get(user_headers=connectpyse.basic_auth, user_params=user_params)
        for json in json_results:
            yield ticket.Ticket(json)

    def create_ticket(self):
        pass

    def get_tickets_count(self):
        json_results = self.tickets.get(the_id='count', user_headers=connectpyse.basic_auth)
        count = json_results['count']
        return count

    def get_ticket_by_id(self, ticket_id):
        a_ticket = ticket.Ticket(self.tickets.get(the_id=ticket_id, user_headers=connectpyse.basic_auth))
        return a_ticket

    def delete_ticket_by_id(self, ticket_id):
        pass

    def replace_ticket(self, ticket_id):
        pass

    def update_ticket(self, ticket_id):
        pass

    def merge_ticket(self, ticket_id):
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
