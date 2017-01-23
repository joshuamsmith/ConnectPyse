from ..cw_model import CWModel


class GroupCompany(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # *(Integer)
        self.groupId = None  # (Integer)
        self.defaultContactFlag = None  # (Boolean)
        self.allContactsFlag = None  # (Boolean)
        self.unsubscribeFlag = None  # (Boolean)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
