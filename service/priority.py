from ..cw_model import CWModel


class Priority(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.name = None  # *(String(50))
        self.color = None  # *(String(50))
        self.sortOrder = None  # (Integer)
        self.defaultFlag = None  # (Boolean)
        self.imageLink = None  # (String)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
