from ..cw_model import CWModel


class CampaignFormSubmitted(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.campaignId = None  # (Integer)
        self.contactId = None  # *(Integer)
        self.dateSubmitted = None  # (String)
        self.url = None  # *(String(2083))
        self.queryString = None  # (String)
        self.pageType = None  # (String)
        self.pageSubType = None  # (String)
        self.topic = None  # (String)
        self.version = None  # (String)
        self.status = None  # (String)

        # initialize object with json dict
        super().__init__(json_dict)
