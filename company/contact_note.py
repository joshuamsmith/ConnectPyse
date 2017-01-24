from ..cw_model import CWModel


class ContactNote(CWModel):
    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.contactId = None  # (Integer)
        self.text = None  # *(String)
        self.type = None  # (NoteTypeReference)
        self.flagged = None  # (Boolean)
        self.enteredBy = None  # (String)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
