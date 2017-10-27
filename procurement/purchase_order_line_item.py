from ..cw_model import CWModel


class PurchaseOrderLineItem(CWModel):

    def __init__(self, json_dict=None):
        # With: id(Integer)
        # Search: ^(\s*)(\*?)([_a-z0-9]*)\s?(\(.*$)
        # Replace: $1self.$3 = None  # $2$4
        # To get: self.id = None  # (Integer)
        self.id = None  # (Integer)
        self.backorderedFlag = None  # (Boolean)
        self.canceledBy = None  # (String)
        self.canceledFlag = None  # (Boolean)
        self.canceledReason = None  # (String(100))
        self.closedFlag = None  # (Boolean)
        self.dateCanceled = None  # (String)
        self.dateCanceledUtc = None  # (String)
        self.description = None  # *(String(6000))
        self.displayInternalNotesFlag = None  # (Boolean)
        self.expectedShipDate = None  # (String)
        self.internalNotes = None  # (String(1000))
        self.lineNumber = None  # *(Integer)
        self.packingSlip = None  # (String(30))
        self.product = None  # *(IvItemReference)
        self.purchaseOrderId = None  # (Integer)
        self.quantity = None  # *(Number)
        self.receivedQuantity = None  # (Integer)
        self.serialNumbers = None  # (String(100))
        self.shipDate = None  # (String)
        self.shipmentMethod = None  # (ShipmentMethodReference)
        self.tax = None  # (Number)
        self.trackingNumber = None  # (String(50))
        self.unitCost = None  # (Number)
        self.unitOfMeasure = None  # *(UnitOfMeasureReference)
        self.vendorOrderNumber = None  # (String(50))
        self.warehouse = None  # (WarehouseReference)
        self.warehouseBin = None  # (WarehouseBinReference)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
