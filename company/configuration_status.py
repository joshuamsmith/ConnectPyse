
class ConfigurationStatus(object):

    def __init__(self, json_dict=None):
        self.id = None  # (Integer)
        self.description = None  # *(String(50))
        self.closedFlag = None  # (Boolean)
        self.defaultFlag = None  # (Boolean)
        self._info = None  # (Metadata)

        # initialize object with json dict
        self.__dict__.update(json_dict)

    def __repr__(self):
        string = None
        string = ''.join('{}: {}\n'.format('Name',self.__dict__['name']))
        return string
