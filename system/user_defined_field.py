from ..cw_model import CWModel


class UserDefinedField(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.podId = None  # *(Integer)
        self.caption = None  # *(String(25))
        self.sequenceNumber = None  # *(Integer)
        self.helpText = None  # (String(1000))
        self.fieldTypeIdentifier = None  # *(Enum)
        self.numberDecimals = None  # (Integer)
        self.entryTypeIdentifier = None  # (Enum)
        self.requiredFlag = None  # (Boolean)
        self.displayOnScreenFlag = None  # (Boolean)
        self.readOnlyFlag = None  # (Boolean)
        self.listViewFlag = None  # (Boolean)
        self.buttonUrl = None  # (String(1000))
        self.options = None  # (UserDefinedFieldOption[])
        self.businessUnitIds = None  # (Integer[])
        self.locationIds = None  # (Integer[])
        self.addAllBusinessUnits = None  # (Boolean)
        self.removeAllBusinessUnits = None  # (Boolean)
        self.addAllLocations = None  # (Boolean)
        self.removeAllLocations = None  # (Boolean)
        self.dateCreated = None  # (String)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
