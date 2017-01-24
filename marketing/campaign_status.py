from ..cw_model import CWModel


class CampaignStatus(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.name = None  # *(String(100))
        self.defaultFlag = None  # (Boolean)
        self.inactiveFlag = None  # (Boolean)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
