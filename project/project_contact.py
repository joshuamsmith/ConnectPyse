from ..cw_model import CWModel


class ProjectContact(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.projectId = None  # (Integer)
        self.contact = None  # *(ContactReference)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
