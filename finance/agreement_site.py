from ..cw_model import CWModel


class AgreementSite(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.company = None  # *(CompanyReference)
        self.site = None  # (SiteReference)
        self.agreementId = None  # (Integer)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
