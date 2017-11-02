from ..cw_model import CWModel


class ChargeCode(CWModel):

    def __init__(self, json_dict=None):
        # With: id(Integer)
        # Search: ^(\s*)(\*?)([_a-z0-9]*)\s?(\(.*$)
        # Replace: $1self.$3 = None  # $2$4
        # To get: self.id = None  # (Integer)
        self.id = None  # (Integer)
        self.name = None  # *(String(50))
        self.company = None  # *(CompanyReference)
        self.location = None  # (SystemLocationReference)
        self.department = None  # (SystemDepartmentReference)
        self.billTime = None  # (Enum)
        self.expenseEntryFlag = None  # (Boolean)
        self.allowAllExpenseTypeFlag = None  # (Boolean)
        self.timeEntryFlag = None  # (Boolean)
        self.workType = None  # *(WorkTypeReference)
        self.workRole = None  # (WorkRoleReference)
        self.integrationXref = None  # (String(50))
        self.expenseTypeIds = None  # (Integer[])
        self._info = None  # (Metadata)
        
        # initialize object with json dict
        super().__init__(json_dict)
