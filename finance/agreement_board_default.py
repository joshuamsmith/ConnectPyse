from ..cw_model import CWModel


class AgreementBoardDefault(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.board = None  # *(BoardReference)
        self.serviceType = None  # (ServiceTypeReference)
        self.defaultFlag = None  # (Boolean)
        self.agreementId = None  # (Integer)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
