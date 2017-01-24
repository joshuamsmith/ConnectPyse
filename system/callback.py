from ..cw_model import CWModel


class Callback(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.description = None  # (String(100))
        self.url = None  # *(String)
        self.objectId = None  # *(Integer)
        self.type = None  # *(String)
        self.level = None  # *(String)
        self.memberId = None  # (Integer)
        self.inactiveFlag = None  # (Boolean)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
