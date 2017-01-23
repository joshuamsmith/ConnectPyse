from ..cw_model import CWModel


class AgreementAddition(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.product = None  # *(IvItemReference)
        self.quantity = None  # (Number)
        self.lessIncluded = None  # (Number)
        self.unitPrice = None  # (Number)
        self.unitCost = None  # (Number)
        self.billCustomer = None  # *(Enum)
        self.effectiveDate = None  # (String)
        self.cancelledDate = None  # (String)
        self.taxableFlag = None  # (Boolean)
        self.serialNumber = None  # (String(50))
        self.invoiceDescription = None  # (String(6000))
        self.purchaseItemFlag = None  # (Boolean)
        self.specialOrderFlag = None  # (Boolean)
        self.agreementId = None  # (Integer)
        self.description = None  # (String)
        self.billedQuantity = None  # (Number)
        self.uom = None  # (String)
        self.extPrice = None  # (Number)
        self.extCost = None  # (Number)
        self.sequenceNumber = None  # (Number)
        self.margin = None  # (Number)
        self.prorateCost = None  # (Number)
        self.proratePrice = None  # (Number)
        self.extendedProrateCost = None  # (Number)
        self.extendedProratePrice = None  # (Number)
        self.prorateCurrentPeriodFlag = None  # (Boolean)
        self._info = None  # (Metadata)
        
        # initialize object with json dict
        super().__init__(json_dict)
