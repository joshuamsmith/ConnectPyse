from ..cw_model import CWModel


class InvoicePayment(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.type = None  # (String)
        self.invoice = None  # (InvoiceReference)
        self.amount = None  # *(Number)
        self.paymentDate = None  # (String)
        self.appliedBy = None  # (String)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
