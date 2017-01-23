from ..cw_model import CWModel


class AgreementWorkType(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.workType = None  # (WorkTypeReference)
        self.locationId = None  # (Integer)
        self.rateType = None  # *(Enum)
        self.billTime = None  # *(Enum)
        self.rate = None  # (Number)
        self.hoursMax = None  # (Number)
        self.hoursMin = None  # (Number)
        self.roundBillHours = None  # (Number)
        self.overageRate = None  # (Number)
        self.overageRateType = None  # (Enum)
        self.agreementLimit = None  # (Number)
        self.site = None  # (SiteReference)
        self.effectiveDate = None  # (String)
        self.endingDate = None  # (String)
        self.agreementId = None  # (Integer)
        self.company = None  # (CompanyReference)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
