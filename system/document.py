from ..cw_model import CWModel


class Document(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.title = None  # (String)
        self.fileName = None  # (String)
        self.serverFileName = None  # (String)
        self.owner = None  # (String)
        self.linkFlag = None  # (Boolean)
        self.imageFlag = None  # (Boolean)
        self.publicFlag = None  # (Boolean)
        self.readOnlyFlag = None  # (Boolean)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
