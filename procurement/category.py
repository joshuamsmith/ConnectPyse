from ..cw_model import CWModel


class Category(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.name = None  # *(String(50))
        self.inactiveFlag = None  # (Boolean)
        self.priceLevelXref = None  # (String(10))
        self.integrationXref = None  # (String(100))
        self.locationIds = None  # (Integer[])
        self.addAllLocations = None  # (Boolean)
        self.removeAllLocations = None  # (Boolean)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
