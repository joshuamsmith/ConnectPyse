from ..cw_model import CWModel


class Product(CWModel):

    def __init__(self, json_dict=None):
        self.identifier = None  # (Enum)
        self.password = None  # (String)
        self.installedFlag = None  # (Boolean)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
