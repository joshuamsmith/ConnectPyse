import restapi
# Class for /service/tickets/{id}/notes
import connectpyse
from connectpyse.service import ticket_note


class TicketNotesAPI(restapi.Client):

    module_url = 'service/tickets/'

    def __init__(self, ticket_id):
        super(TicketNotesAPI, self).__init__('{}/{}/{}'.format(connectpyse.API_URL, TicketNotesAPI.module_url, ticket_id))

    def get_ticket_notes(self, user_params={}):
        json_results = self.notes.get(user_headers=connectpyse.basic_auth, user_params=user_params)
        for json in json_results:
            yield ticket_note.TicketNote(json)

    def create_ticket_note(self, a_note):
        dict_post = {'internalAnalysisFlag': a_note.internalAnalysisFlag, 'text': a_note.text,
                     'customerUpdatedFlag': a_note.customerUpdatedFlag}
        json_results = self.notes.post(user_data=dict_post, user_headers=connectpyse.basic_auth)
        # status_code = json_results.status_code
        return json_results

    def get_ticket_notes_count(self):
        json_results = self.notes.get(the_id='count', user_headers=connectpyse.basic_auth)
        count = json_results['count']
        return count

    def get_ticket_note_by_id(self, ticket_note_id):
        a_ticket_note = ticket_note.TicketNote(self.notes.get(the_id=ticket_note_id, user_headers=connectpyse.basic_auth))
        return a_ticket_note

    def delete_ticket_note_by_id(self, ticket_note_id):
        pass

    def replace_ticket_note(self, ticket_note_id):
        pass

    def update_ticket_note(self, ticket_note_id):
        pass

    def merge_ticket_note(self, ticket_note_id):
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
