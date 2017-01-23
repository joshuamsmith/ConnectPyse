from ..cw_model import CWModel


class AdjustmentDetail(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.catalogItem = None  # *(CatalogItemReference)
        self.description = None  # (String(50))
        self.quantityOnHand = None  # (Number)
        self.unitCost = None  # (Number)
        self.warehouse = None  # *(WarehouseReference)
        self.warehouseBin = None  # *(WarehouseBinReference)
        self.quantityAdjusted = None  # *(Integer)
        self.serialNumber = None  # (String(1000))
        self.adjustment = None  # (AdjustmentReference)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
