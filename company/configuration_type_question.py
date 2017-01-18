class ConfigurationTypeQuestion(object):
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
        self.__dict__.update(json_dict)

    def __repr__(self):
        string = None
        string = ''.join('{}: {}\n'.format('Name', self.__dict__['name']))
        return string
