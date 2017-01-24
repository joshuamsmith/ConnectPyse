from ..cw_model import CWModel


class AgreementWorkRole(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.workRole = None  # (WorkRoleReference)
        self.locationId = None  # (Integer)
        self.rateType = None  # *(Enum)
        self.rate = None  # (Number)
        self.limitTo = None  # (Number)
        self.effectiveDate = None  # (String)
        self.endingDate = None  # (String)
        self.agreementId = None  # (Integer)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
