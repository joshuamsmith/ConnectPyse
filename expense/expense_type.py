from ..cw_model import CWModel


class ExpenseType(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.name = None  # *(String(30))
        self.amountCaption = None  # *(String)
        self.reimbursementRate = None  # (Number)
        self.billExpenses = None  # *(Enum)
        self.invoiceMarkupOption = None  # *(Enum)
        self.invoiceMarkupAmount = None  # (Number)
        self.advancedAmountFlag = None  # (Boolean)
        self.mileageFlag = None  # (Boolean)
        self.quantityFlag = None  # (Boolean)
        self.inactiveFlag = None  # (Boolean)
        self.maxAmount = None  # (Number)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
