from ..cw_model import CWModel


class TimeEntry(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.company = None  # *(CompanyReference)
        self.chargeToId = None  # *(Integer)
        self.chargeToType = None  # *(Enum)
        self.member = None  # (MemberReference)
        self.locationId = None  # (Integer)
        self.businessUnitId = None  # (Integer)
        self.workType = None  # (WorkTypeReference)
        self.workRole = None  # (WorkRoleReference)
        self.agreement = None  # (AgreementReference)
        self.timeStart = None  # *(String)
        self.timeEnd = None  # (String)
        self.hoursDeduct = None  # (Number)
        self.actualHours = None  # (Number)
        self.billableOption = None  # (Enum)
        self.notes = None  # (String)
        self.internalNotes = None  # (String)
        self.addToDetailDescriptionFlag = None  # (Boolean)
        self.addToInternalAnalysisFlag = None  # (Boolean)
        self.addToResolutionFlag = None  # (Boolean)
        self.emailResourceFlag = None  # (Boolean)
        self.emailContactFlag = None  # (Boolean)
        self.emailCcFlag = None  # (Boolean)
        self.emailCc = None  # (String)
        self.hoursBilled = None  # (Number)
        self.enteredBy = None  # (String)
        self.dateEntered = None  # (String)
        self.invoice = None  # (InvoiceReference)
        self.hourlyRate = None  # (Number)
        self._info = None  # (Metadata)
        self.customFields = None  # (CustomFieldValue[])

        # initialize object with json dict
        super().__init__(json_dict)
