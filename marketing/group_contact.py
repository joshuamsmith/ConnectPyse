from ..cw_model import CWModel


class GroupContact(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # *(Integer)
        self.groupId = None  # (Integer)
        self.note = None  # (String(50))
        self.unsubscribeFlag = None  # (Boolean)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
