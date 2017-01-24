from ..cw_model import CWModel


class SurveyResult(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.ticketId = None  # *(Integer)
        self.emailAddress = None  # (String)
        self.footerResponse = None  # (String)
        self.contactMeFlag = None  # (Boolean)
        self.contact = None  # (ContactReference)
        self.results = None  # (SurveyResultDetail[])
        self.totalPoints = None  # (Integer)
        self.company = None  # (CompanyReference)
        self.surveyId = None  # (Integer)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
