
class CWModel(object):
    def __init__(self, json_dict=None):
        if json_dict is not None:
            self.__dict__.update(json_dict)

    def __repr__(self):
        string = ''
        for k, v in self.__dict__.items():
            string = ''.join([string, '{}: {}\n'.format(k, v)])
        return string
