from ..cw_model import CWModel


class ShipmentMethod(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.name = None  # *(String(50))
        self.defaultFlag = None  # (Boolean)
        self.trackingUrl = None  # (String(200))
        self.shippingType = None  # (Enum)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
