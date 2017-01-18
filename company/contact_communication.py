class ContactCommunication(object):
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

        if json_dict is not None:
            # initialize object with json dict
            self.__dict__.update(json_dict)

    def __repr__(self):
        string = ''
        for k, v in self.__dict__.items():
            string = ''.join([string, '{}: {}\n'.format(k, v)])
        return string
