from ..cw_model import CWModel


class TimeSheet(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.member = None  # (MemberReference)
        self.year = None  # (Integer)
        self.period = None  # (Integer)
        self.dateStart = None  # (String)
        self.dateEnd = None  # (String)
        self.status = None  # (StatusReference)
        self.hours = None  # *(Integer)
        self.deadline = None  # (String)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)

    def get_timesheets(self):
        return super()._get()
