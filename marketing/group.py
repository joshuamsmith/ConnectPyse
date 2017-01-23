from ..cw_model import CWModel


class Group(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.name = None  # *(String)
        self.publicDescription = None  # (String(255))
        self.publicFlag = None  # (Boolean)
        self.inactiveFlag = None  # (Boolean)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
