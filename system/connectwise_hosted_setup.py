from ..cw_model import CWModel


class ConnectwiseHostedSetup(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.screenId = None  # *(Integer)
        self.description = None  # *(String(255))
        self.url = None  # *(String(1024))
        self.type = None  # *(Enum)
        self.origin = None  # (String(50))
        self.podHeight = None  # (Integer)
        self.toolbarButtonDialogHeight = None  # (Integer)
        self.toolbarButtonDialogWidth = None  # (Integer)
        self.toolbarButtonText = None  # *(String(50))
        self.toolbarButtonToolTip = None  # (String(50))
        self.toolbarButtonIconDocumentId = None  # (Integer)
        self.disabledFlag = None  # (Boolean)
        self.createdBy = None  # (String)
        self.dateCreated = None  # (String)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
