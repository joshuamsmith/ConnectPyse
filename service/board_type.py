from ..cw_model import CWModel


class BoardType(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.name = None  # *(String(50))
        self.category = None  # (Enum)
        self.defaultFlag = None  # (Boolean)
        self.inactive = None  # (Boolean)
        self.requestForChange = None  # (Boolean)
        self.boardId = None  # (Integer)
        self.locationId = None  # (Integer)
        self.businessUnitId = None  # (Integer)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
