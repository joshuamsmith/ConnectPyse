from ..cw_model import CWModel


class AgreementWorkRoleExclusion(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.workRole = None  # *(WorkRoleReference)
        self.agreementId = None  # (Integer)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
