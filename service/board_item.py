from ..cw_model import CWModel


class BoardItem(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.name = None  # *(String(50))
        self.inactive = None  # (Boolean)
        self.typeAssociations = None  # (TypeAssociations[])
        self.addAllSubTypes = None  # (Boolean)
        self.removeAllSubTypes = None  # (Boolean)
        self.typeId = None  # (Integer)
        self.boardId = None  # (Integer)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
