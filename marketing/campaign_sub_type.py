from ..cw_model import CWModel


class CampaignSubType(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.typeId = None  # (Integer)
        self.name = None  # *(String(100))
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
