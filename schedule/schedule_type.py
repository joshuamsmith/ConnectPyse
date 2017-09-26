from cw_model import CWModel


class ScheduleType(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.name = None  # *(String(50))
        self.identifier = None  # *(String(1))
        self.chargeCode = None  # (ChargeCodeReference)
        self.where = None  # (ServiceLocationReference)
        self.systemFlag = None  # (Boolean)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
