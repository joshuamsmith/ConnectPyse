from ..cw_model import CWModel


class  BoardSubType(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.name = None  # *(String(50))
        self.inactive = None  # (Boolean)
        self.typeAssociationIds = None  # (Integer[])
        self.addAllTypes = None  # (Boolean)
        self.removeAllTypes = None  # (Boolean)
        self.boardId = None  # (Integer)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
