from ..cw_model import CWModel


class Report(CWModel):

    def __init__(self, json_dict=None):
        self.column_definitions = None  # (JObject[])
        self.row_values = None  # (JObject[])

        # initialize object with json dict
        super().__init__(json_dict)
