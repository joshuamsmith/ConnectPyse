from ..cw_model import CWModel


class BoardStatus(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.name = None  # *(String(50))
        self.boardId = None  # (Integer)
        self.sortOrder = None  # (Integer)
        self.displayOnBoard = None  # (Boolean)
        self.inactive = None  # (Boolean)
        self.closedStatus = None  # (Boolean)
        self.timeEntryNotAllowed = None  # (Boolean)
        self.defaultFlag = None  # (Boolean)
        self.escalationStatus = None  # (Enum)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
