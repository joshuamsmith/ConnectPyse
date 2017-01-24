from ..cw_model import CWModel


class TicketStopwatch(CWModel):

    def __init__(self, json_dict=None):
        self._info = None  # (Metadata)
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
        self.serviceStatus = None  # (ServiceStatusReference)
        self.startTime = None  # (String)
        self.status = None  # *(Enum)
        self.ticket = None  # *(TicketReference)
        self.ticketMobileGuid = None  # (Guid)
        self.totalPauseTime = None  # (Integer)
        self.workRole = None  # (WorkRoleReference)
        self.workType = None  # (WorkTypeReference)
        self.showNotesInDiscussionFlag = None  # (Boolean)
        self.showNotesInInternalFlag = None  # (Boolean)
        self.showNotesInResolutionFlag = None  # (Boolean)
        self.emailNotesToContactFlag = None  # (Boolean)
        self.emailNotesToResourcesFlag = None  # (Boolean)

        # initialize object with json dict
        super().__init__(json_dict)
