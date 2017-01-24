from ..cw_model import CWModel


class ContactCommunication(CWModel):
    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.contactId = None  # (Integer)
        self.type = None  # *(CommunicationTypeReference)  {id (integer)(int32)), name (string)), _info}
        self.value = None  # *(String(250))
        self.extension = None  # (String(15))
        self.defaultFlag = None  # (Boolean)
        self.mobileGuid = None  # (Guid)
        self.communicationType = None  # (Enum)  ("Phone", "Fax", "Email")
        self._info = None  # (Metadata)

        # initialize object with json dict
        super().__init__(json_dict)
