from ..cw_model import CWModel


class Currency(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.currencyIdentifier = None  # *(String(10))
        self.name = None  # (String(50))
        self.symbol = None  # (String(10))
        self.displayIdFlag = None  # (Boolean)
        self.displaySymbolFlag = None  # (Boolean)
        self.isoCode = None  # (String(3))
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
