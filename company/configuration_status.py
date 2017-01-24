from ..cw_model import CWModel


class ConfigurationStatus(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.description = None  # *(String(50))
        self.closedFlag = None  # (Boolean)
        self.defaultFlag = None  # (Boolean)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
