from ..cw_model import CWModel


class TaxCodeXRef(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.description = None  # *(String(50))
        self.defaultFlag = None  # (Boolean)
        self.levelOne = None  # (Enum)
        self.levelTwo = None  # (Enum)
        self.levelThree = None  # (Enum)
        self.levelFour = None  # (Enum)
        self.levelFive = None  # (Enum)
        self.taxCode = None  # (TaxCodeReference)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
