from ..cw_model import CWModel


class AuditTrail(CWModel):

    def __init__(self, json_dict=None):
        self.text = None  # (String)
        self.enteredDate = None  # (String)
        self.enteredBy = None  # (String)
        self.auditType = None  # (String)
        self.auditSubType = None  # (String)
        self.auditSource = None  # (String)

        # initialize object with json dict
        super().__init__(json_dict)
