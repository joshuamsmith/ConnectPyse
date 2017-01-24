from ..cw_model import CWModel


class OpportunityNote(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.opportunityId = None  # (Integer)
        self.type = None  # (NoteTypeReference)
        self.text = None  # *(String)
        self.flagged = None  # (Boolean)
        self.enteredBy = None  # (String)
        self.mobileGuid = None  # (Guid)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
