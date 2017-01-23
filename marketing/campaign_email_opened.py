from ..cw_model import CWModel


class CampaignEmailOpened(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.campaignId = None  # (Integer)
        self.contactId = None  # *(Integer)
        self.dateOpened = None  # (String)

        # initialize object with json dict
        super().__init__(json_dict)
