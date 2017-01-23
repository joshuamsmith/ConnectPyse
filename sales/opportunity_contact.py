from ..cw_model import CWModel


class OpportunityContact(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.contact = None  # *(ContactReference)
        self.company = None  # (CompanyReference)
        self.role = None  # (OpportunitySalesRoleReference)
        self.notes = None  # (String)
        self.referralFlag = None  # (Boolean)
        self.opportunityId = None  # (Integer)
        self.phoneNumber = None  # (String)
        self.emailAddress = None  # (String)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
