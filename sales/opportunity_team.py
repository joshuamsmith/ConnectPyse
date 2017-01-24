from ..cw_model import CWModel


class OpportunityTeam(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.type = None  # *(Enum)
        self.member = None  # (MemberReference)
        self.salesTeam = None  # (SalesTeamReference)
        self.commissionPercent = None  # (Integer)
        self.referralFlag = None  # (Boolean)
        self.opportunityId = None  # (Integer)
        self.responsibleFlag = None  # (Boolean)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
