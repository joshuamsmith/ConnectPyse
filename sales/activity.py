from cw_model import CWModel


class Activity(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.name = None  # *(String(100))
        self.type = None  # (ActivityTypeReference)
        self.company = None  # (CompanyReference)
        self.contact = None  # (ContactReference)
        self.phoneNumber = None  # (String(30))
        self.email = None  # (String(250))
        self.status = None  # (ActivityStatusReference)
        self.opportunity = None  # (OpportunityReference)
        self.ticket = None  # (TicketReference)
        self.agreement = None  # (AgreementReference)
        self.campaign = None  # (CampaignReference)
        self.notes = None  # (String)
        self.dateStart = None  # (String)
        self.dateEnd = None  # (String)
        self.assignedBy = None  # (MemberReference)
        self.assignTo = None  # *(MemberReference)
        self.scheduleStatus = None  # (ScheduleStatusReference)
        self.reminder = None  # (ReminderReference)
        self.where = None  # (ServiceLocationReference)
        self.notifyFlag = None  # (Boolean)
        self.mobileGuid = None  # (Guid)
        self._info = None  # (Metadata)
        self.customFields = None  # (CustomFieldValue[])

        # initialize object with json dict
        super().__init__(json_dict)
