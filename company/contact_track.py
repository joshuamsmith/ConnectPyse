from ..cw_model import CWModel


class ContactTrack(CWModel):
    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.trackId = None  # *(Integer)
        self.name = None  # (String)
        self.startDate = None  # (String)
        self.endDate = None  # (String)
        self.actionTaken = None  # (Integer)
        self.actionRemaining = None  # (Integer)
        self.startedBy = None  # (String)
        self.company = None  # (CompanyReference)
        self.contact = None  # (ContactReference)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
