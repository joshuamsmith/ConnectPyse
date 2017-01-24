from ..cw_model import CWModel


class Adjustment(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.identifier = None  # *(String(50))
        self.type = None  # *(AdjustmentTypeReference)
        self.reason = None  # (String(100))
        self.notes = None  # (String)
        self.closedFlag = None  # (Boolean)
        self.closedBy = None  # (String)
        self.closedDate = None  # (String)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
