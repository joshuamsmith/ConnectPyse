from ..cw_model import CWModel


class Info(CWModel):

    def __init__(self, json_dict=None):
        self.version = None  # (String)
        self.isCloud = None  # (Boolean)
        self.serverTimeZone = None  # (String)

        # initialize object with json dict
        super().__init__(json_dict)
