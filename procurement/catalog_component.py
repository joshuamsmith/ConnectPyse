from ..cw_model import CWModel


class CatalogComponent(CWModel):

    def __init__(self, json_dict=None):
        # With: id(Integer)
        # Search: ^(\s*)(\*?)([_a-z0-9]*)\s?(\(.*$)
        # Replace: $1self.$3 = None  # $2$4
        # To get: self.id = None  # (Integer)
        self.id = None  # (Integer)
        self.sequenceNumber = None  # (Integer)
        self.quantity = None  # *(Number)
        self.catalogItem = None  # *(CatalogItemReference)
        self.hidePriceFlag = None  # (Boolean)
        self.hideItemIdentifierFlag = None  # (Boolean)
        self.hideDescriptionFlag = None  # (Boolean)
        self.hideQuantityFlag = None  # (Boolean)
        self.hideExtendedPriceFlag = None  # (Boolean)
        self.parentCatalogItem = None  # (CatalogItemReference)
        self.price = None  # (Number)
        self.cost = None  # (Number)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
