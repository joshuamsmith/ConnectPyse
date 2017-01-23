from ..cw_model import CWModel


class ScheduleStatus(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.name = None  # *(String(30))
        self.defaultFlag = None  # (Boolean)
        self.showAsTentativeFlag = None  # (Boolean)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
