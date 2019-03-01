from os import path
import json
import base64
import sys


sys.path.insert(0, path.dirname(path.abspath(__file__)))

api_file = 'my_api.json'
_api_file = path.join(path.dirname(path.abspath(__file__)), api_file)


with open(_api_file) as fin:
    cw_api_settings = json.load(fin)

API_URL = cw_api_settings['API_URL']
_cid = cw_api_settings['COMPANYID']
_pubk = cw_api_settings['PUBLICKEY']
_privk = cw_api_settings['PRIVATEKEY']
_authtoken = cw_api_settings['AUTHTOKEN']

if (_authtoken is not None) and (_authtoken != "xxxxx"):
    basic_auth = _authtoken

else:

    basic_auth = base64.b64encode("{}+{}:{}".format(_cid, _pubk, _privk).encode('utf-8'))
    basic_auth = {'Authorization': 'Basic {}'.format(str(basic_auth, 'utf-8'))}
