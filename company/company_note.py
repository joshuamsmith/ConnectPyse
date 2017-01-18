
class CompanyNote(object):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.text = None  # *(String)
        self.type = None  # (NoteTypeReference)
        self.flagged = None  # (Boolean)
        self.enteredBy = None  # (String)
        self.company = None  # (CompanyReference)
        self._info = None  # (Metadata)

        # initialize object with json dict
        self.__dict__.update(json_dict)

    def __repr__(self):
        string = None
        string = ''.join('{}: {}\n'.format('Name',self.__dict__['name']))
        return string
