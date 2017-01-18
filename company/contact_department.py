from ..cw_model import CWModel


class ContactDepartment(CWModel):
    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.name = None  # *(String(30))
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
