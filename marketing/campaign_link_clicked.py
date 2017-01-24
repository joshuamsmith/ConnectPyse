from ..cw_model import CWModel


class CampaignLinkClicked(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.campaignId = None  # (Integer)
        self.contactId = None  # *(Integer)
        self.dateClicked = None  # (String)
        self.url = None  # *(String(2083))
        self.queryString = None  # (String)

        # initialize object with json dict
        super().__init__(json_dict)
