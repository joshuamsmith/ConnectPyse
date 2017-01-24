from ..cw_model import CWModel


class AccountingBatch(CWModel):

    def __init__(self, json_dict=None):
        self.thruDate = None  # (String)
        self.transactionsClosedDate = None  # (String)
        self.locationId = None  # (Integer)
        self.summarizeInvoices = None  # (Integer)
        self.includedInvoiceIds = None  # (Integer[])
        self.includedExpenseIds = None  # (Integer[])
        self.includedProductIds = None  # (Integer[])
        self.excludedInvoiceIds = None  # (Integer[])
        self.excludedExpenseIds = None  # (Integer[])
        self.excludedProductIds = None  # (Integer[])
        self.id = None  # (Integer)
        self.batchIdentifier = None  # *(String(50))
        self.exportInvoicesFlag = None  # (Boolean)
        self.exportExpensesFlag = None  # (Boolean)
        self.exportProductsFlag = None  # (Boolean)
        self.closedFlag = None  # (Boolean)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
