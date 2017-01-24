from ..cw_model import CWModel


class ScheduleReminderTime(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.time = None  # (Integer)
        self.description = None  # (String(10))
        self.defaultFlag = None  # (Boolean)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
