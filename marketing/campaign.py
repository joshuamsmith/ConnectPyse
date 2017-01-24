from ..cw_model import CWModel


class Campaign(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.name = None  # *(String(50))
        self.type = None  # *(CampaignTypeReference)
        self.subType = None  # *(CampaignSubTypeReference)
        self.status = None  # (CampaignStatusReference)
        self.startDate = None  # *(String)
        self.endDate = None  # (String)
        self.locationId = None  # (Integer)
        self.member = None  # (MemberReference)
        self.inactive = None  # (Boolean)
        self.inactiveDaysAfterEnd = None  # (Integer)
        self.notes = None  # (String)
        self.defaultGroup = None  # (GroupReference)
        self.marketingManagerDefaultTrackId = None  # (Integer)
        self.opportunityDefaultTrackId = None  # (Integer)
        self.impressions = None  # (Integer)
        self.budgetRevenue = None  # (Number)
        self.budgetCost = None  # (Number)
        self.actualCost = None  # (Number)
        self.budgetGrossMargin = None  # (Number)
        self.budgetROI = None  # (Number)
        self.actualRevenue = None  # (Number)
        self.actualGrossMargin = None  # (Number)
        self.actualROI = None  # (Number)
        self.emailsSent = None  # (Integer)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
