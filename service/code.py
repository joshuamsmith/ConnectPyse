from ..cw_model import CWModel


class Code(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.name = None  # *(String(50))
        self.description = None  # *(String)
        self.boardId = None  # (Integer)
        self.locationId = None  # (Integer)
        self.businessUnitId = None  # (Integer)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
