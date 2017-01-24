from ..cw_model import CWModel


class ConfigurationTypeQuestion(CWModel):
    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.configurationTypeId = None  # (Integer)
        self.fieldType = None  # *(Enum)
        self.entryType = None  # *(Enum)
        self.sequenceNumber = None  # (Number)
        self.question = None  # *(String(1000))
        self.numberOfDecimals = None  # (Integer)
        self.requiredFlag = None  # (Boolean)
        self.inactiveFlag = None  # (Boolean)
        self.possibleAnswers = None  # (Array)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
