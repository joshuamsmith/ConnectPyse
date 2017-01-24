from ..cw_model import CWModel


class Link(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.name = None  # *(String(50))
        self.tableReferenceId = None  # *(Integer)
        self.url = None  # (String(1000))
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
