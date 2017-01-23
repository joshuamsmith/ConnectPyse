from ..cw_model import CWModel


class AgreementAdjustment(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.amount = None  # (Number)
        self.description = None  # (String(1000))
        self.effectiveDate = None  # (String)
        self.agreementId = None  # (Integer)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
