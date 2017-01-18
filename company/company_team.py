from ..cw_model import CWModel


class CompanyTeam(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.company = None  # (CompanyReference)
        self.teamRole = None  # *(TeamRoleReference)
        self.locationId = None  # (Integer)
        self.businessUnitId = None  # (Integer)
        self.contact = None  # (ContactReference)
        self.member = None  # (MemberReference)
        self.accountManagerFlag = None  # (Boolean)
        self.techFlag = None  # (Boolean)
        self.salesFlag = None  # (Boolean)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
