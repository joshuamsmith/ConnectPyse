from ..cw_model import CWModel


class MenuEntry(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.menuLocation = None  # *(MenuLocationReference)
        self.caption = None  # *(String(50))
        self.link = None  # *(String(2000))
        self.newWindowFlag = None  # *(Boolean)
        self.locationIds = None  # (Integer[])
        self.origin = None  # (String(2000))
        self.addAllLocations = None  # (Boolean)
        self.removeAllLocations = None  # (Boolean)
        self.smallMenuIconId = None  # (Integer)
        self.largeMenuIconId = None  # (Integer)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
