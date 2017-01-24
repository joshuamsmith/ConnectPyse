from ..cw_model import CWModel


class ActivityStopwatch(CWModel):

    def __init__(self, json_dict=None):
        self._info = None  # (Metadata)
        self.activityId = None  # *(Integer)
        self.activityMobileGuid = None  # (Guid)
        self.agreement = None  # (AgreementReference)
        self.billableOption = None  # (Enum)
        self.businessUnitId = None  # (Integer)
        self.dateEntered = None  # (String)
        self.endTime = None  # (String)
        self.id = None  # (Integer)
        self.internalNotes = None  # (String)
        self.locationId = None  # (Integer)
        self.member = None  # *(MemberReference)
        self.mobileGuid = None  # (Guid)
        self.notes = None  # (String(4000))
        self.startTime = None  # (String)
        self.status = None  # *(Enum)
        self.totalPauseTime = None  # (Integer)
        self.workRole = None  # (WorkRoleReference)
        self.workType = None  # (WorkTypeReference)

        # initialize object with json dict
        super().__init__(json_dict)
