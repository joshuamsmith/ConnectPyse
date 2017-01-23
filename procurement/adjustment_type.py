from ..cw_model import CWModel


class AdjustmentType(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.identifier = None  # *(String(50))
        self.name = None  # (String(100))
        self.auditTrailFlag = None  # (Boolean)
        self.dateCreated = None  # (String)
        self.createdBy = None  # (String)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
