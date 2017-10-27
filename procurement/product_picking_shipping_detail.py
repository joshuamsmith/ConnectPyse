from ..cw_model import CWModel


class ProductPickingShippingDetail(CWModel):

    def __init__(self, json_dict=None):
        # With: id(Integer)
        # Search: ^(\s*)(\*?)([_a-z0-9]*)\s?(\(.*$)
        # Replace: $1self.$3 = None  # $2$4
        # To get: self.id = None  # (Integer)
        self.id = None  # (Integer)
        self.pickedQuantity = None  # *(Integer)
        self.shippedQuantity = None  # *(Integer)
        self.warehouse = None  # *(WarehouseReference)
        self.warehouseBin = None  # *(WarehouseBinReference)
        self.shipmentMethod = None  # (ShipmentMethodReference)
        self.serialNumber = None  # (String)
        self.serialNumberIds = None  # (Integer[])
        self.trackingNumber = None  # (String)
        self.productItem = None  # (ProductItemReference)
        self.lineNumber = None  # (Integer)
        self.quantity = None  # (Integer)
        self._info = None  # (Metadata)
        
        # initialize object with json dict
        super().__init__(json_dict)
