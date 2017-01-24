from ..cw_model import CWModel


class TicketTask(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.ticketId = None  # (Integer)
        self.notes = None  # (String)
        self.closedFlag = None  # (Boolean)
        self.priority = None  # (Integer)
        self.schedule = None  # (ScheduleEntryReference)
        self.code = None  # (ServiceCodeReference)
        self.resolution = None  # (String)
        self.childScheduleAction = None  # (Enum)
        self.childTicketId = None  # (Integer)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
