from ..cw_model import CWModel


class BoardExcludedMember(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.memberId = None  # *(Integer)
        self.boardId = None  # (Integer)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
