from ..cw_model import CWModel


class TicketNote(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.ticketId = None  # (Integer)
        self.text = None  # (String)
        self.detailDescriptionFlag = None  # (Boolean)
        self.internalAnalysisFlag = None  # (Boolean)
        self.resolutionFlag = None  # (Boolean)
        self.member = None  # (MemberReference)
        self.contact = None  # (ContactReference)
        self.customerUpdatedFlag = None  # (Boolean)
        self.processNotifications = None  # (Boolean)
        self.dateCreated = None  # (String)
        self.createdBy = None  # (String)
        self.internalFlag = None  # (Boolean)
        self.externalFlag = None  # (Boolean)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
