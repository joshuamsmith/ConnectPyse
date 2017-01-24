from ..cw_model import CWModel


class Board(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.name = None  # *(String(50))
        self.locationId = None  # *(Integer)
        self.businessUnitId = None  # *(Integer)
        self.inactive = None  # (Boolean)
        self.signOffTemplate = None  # (ServiceSignoffReference)
        self.sendToContact = None  # (Boolean)
        self.contactTemplateId = None  # (Integer)
        self.sendToResource = None  # (Boolean)
        self.resourceTemplateId = None  # (Integer)
        self.projectFlag = None  # (Boolean)
        self.showDependenciesFlag = None  # (Boolean)
        self.showEstimatesFlag = None  # (Boolean)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
