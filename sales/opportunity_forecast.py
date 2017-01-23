from ..cw_model import CWModel


class OpportunityForecast(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.name = None  # (String(50))
        self.revenue = None  # (Number)
        self.cost = None  # (Number)
        self.type = None  # *(Enum)
        self.status = None  # (OpportunityStatusReference)
        self.includedFlag = None  # (Boolean)
        self.recurring = None  # (ProductRecurring)
        self.percent = None  # (Number)
        self.margin = None  # (Number)
        self.opportunityId = None  # (Integer)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
