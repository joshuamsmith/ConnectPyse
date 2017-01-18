class TicketNote(object):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.ticketId = None  # (Integer)
        self.text = None  # (String)
        self.detailDescriptionFlag = None  # (Boolean)
        self.internalAnalysisFlag = None  # (Boolean)
        self.resolutionFlag = None  # (Boolean)
        self.member = None  # (MemberReference)
        self.contact = None  # (ContactReference)
        self.customerUpdatedFlag = None  # (Boolean)
        self.processNotifications = None  # (Boolean)
        self.dateCreated = None  # (String)
        self.createdBy = None  # (String)
        self.internalFlag = None  # (Boolean)
        self.externalFlag = None  # (Boolean)
        self._info = None  # (Metadata)

        # initialize object with json dict
        self.__dict__.update(json_dict)

    def __repr__(self):
        string = ''
        for k, v in self.__dict__.items():
            string = ''.join([string, '{}: {}\n'.format(k, v)])
        return string