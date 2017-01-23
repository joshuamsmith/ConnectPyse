from ..cw_model import CWModel


class ProjectNote(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.projectId = None  # (Integer)
        self.text = None  # *(String)
        self.type = None  # (NoteTypeReference)
        self.flagged = None  # (Boolean)
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
