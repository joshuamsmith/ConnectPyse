from cw_model import CWModel


class ScheduleEntry(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.objectId = None  # (Integer)
        self.name = None  # (String(250))
        self.member = None  # *(MemberReference)
        self.where = None  # (ServiceLocationReference)
        self.dateStart = None  # (String)
        self.dateEnd = None  # (String)
        self.reminder = None  # (ReminderReference)
        self.status = None  # (ScheduleStatusReference)
        self.type = None  # *(ScheduleTypeReference)
        self.span = None  # (ScheduleSpanReference)
        self.doneFlag = None  # (Boolean)
        self.acknowledgedFlag = None  # (Boolean)
        self.ownerFlag = None  # (Boolean)
        self.allowScheduleConflictsFlag = None  # (Boolean)
        self.addMemberToProjectFlag = None  # (Boolean)
        self.projectRoleId = None  # (Integer)
        self.mobileGuid = None  # (Guid)
        self.closeDate = None  # (String)
        self.hours = None  # (Number)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
