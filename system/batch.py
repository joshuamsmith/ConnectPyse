from ..cw_model import CWModel


class Batch(CWModel):

    def __init__(self, json_dict=None):
        self.id = None  # (String)
        self.responses = None  # (EndpointResponse[])

        # initialize object with json dict
        super().__init__(json_dict)
