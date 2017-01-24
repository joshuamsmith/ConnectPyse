from ..cw_model import CWModel


class ExpenseEntry(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.company = None  # **(CompanyReference)
        self.chargeToId = None  # (Integer)
        self.chargeToType = None  # **(Enum)
        self.type = None  # *(ExpenseTypeReference)
        self.member = None  # (MemberReference)
        self.paymentMethod = None  # (PaymentMethodReference)
        self.classification = None  # (ClassificationReference)
        self.amount = None  # *(Number)
        self.billableOption = None  # *(Enum)
        self.date = None  # *(String)
        self.locationId = None  # (Integer)
        self.businessUnitId = None  # (Integer)
        self.notes = None  # (String)
        self.agreement = None  # (AgreementReference)
        self.invoiceAmount = None  # (Number)
        self.taxes = None  # (ExpenseTax[])
        self.invoice = None  # (InvoiceReference)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
