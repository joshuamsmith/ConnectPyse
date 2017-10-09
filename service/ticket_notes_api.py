# Class for /service/tickets/{id}/notes
from .service import ticket_note


class TicketNotesAPI(CWController):
    def __init__(self, ticket_id):
        self.module_url = 'service'
        self.module = 'tickets/{}/notes'.format(ticket_id)
        self._class = ticket_note.TicketNote
        super().__init__()  # instance gets passed to parent object

    def get_ticket_notes(self):
        return super()._get()

    def create_ticket_note(self, a_ticket_note):
        return super()._create(a_ticket_note)

    def get_ticket_notes_count(self):
        return super()._get_count()

    def get_ticket_note_by_id(self, ticket_note_id):
        return super()._get_by_id(ticket_note_id)

    def delete_ticket_note_by_id(self, ticket_note_id):
        super()._delete_by_id(ticket_note_id)

    def replace_ticket_note(self, ticket_note_id):
        pass

    def update_ticket_note(self, ticket_id, key, value):
        return super()._update(ticket_id, key, value)

    def merge_ticket_note(self, a_ticket_note, target_ticket_note_id):
        # return super()._merge(a_ticket_note, target_ticket_note_id)
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
