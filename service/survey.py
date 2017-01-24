from ..cw_model import CWModel


class Survey(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.name = None  # *(String(50))
        self.inactiveFlag = None  # (Boolean)
        self.headerIncludeLogoFlag = None  # (Boolean)
        self.headerText = None  # (String(4000))
        self.headerTextVisibleFlag = None  # (Boolean)
        self.footerText = None  # (String(500))
        self.footerTextVisibleFlag = None  # (Boolean)
        self.thankYouText = None  # (String(4000))
        self.notifyWho = None  # (GenericIdIdentifierReference)
        self.notifyWhoVisibleFlag = None  # (Boolean)
        self.notifyMember = None  # (MemberReference)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
