from ..cw_model import CWModel


class OpportunityStatus(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.name = None  # *(String(30))
        self.wonFlag = None  # (Boolean)
        self.lostFlag = None  # (Boolean)
        self.closedFlag = None  # (Boolean)
        self.inactiveFlag = None  # (Boolean)
        self.defaultFlag = None  # (Boolean)
        self._info = None  # (Metadata)
        self.enteredBy = None  # (String)
        self.dateEntered = None  # (String)

        # initialize object with json dict
        super().__init__(json_dict)
