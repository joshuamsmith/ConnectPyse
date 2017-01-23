from ..cw_model import CWModel


class CatalogItem(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.identifier = None  # *(String(30))
        self.description = None  # *(String(50))
        self.inactiveFlag = None  # (Boolean)
        self.subcategory = None  # *(ProductSubCategoryReference)
        self.type = None  # *(ProductTypeReference)
        self.productClass = None  # *(Enum)
        self.serializedFlag = None  # (Boolean)
        self.serializedCostFlag = None  # (Boolean)
        self.phaseProductFlag = None  # (Boolean)
        self.unitOfMeasure = None  # (UnitOfMeasureReference)
        self.minStockLevel = None  # (Integer)
        self.price = None  # (Number)
        self.cost = None  # (Number)
        self.priceAttribute = None  # (Enum)
        self.taxableFlag = None  # (Boolean)
        self.customerDescription = None  # *(String(6000))
        self.manufacturer = None  # (ManufacturerReference)
        self.manufacturerPartNumber = None  # (String(50))
        self.vendor = None  # (CompanyReference)
        self.vendorSku = None  # (String(50))
        self.notes = None  # (String)
        self.integrationXRef = None  # (String(50))
        self.dateEntered = None  # (String)
        self.category = None  # (ProductCategoryReference)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
