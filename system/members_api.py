import restapi
# Class for /system/members
import connectpyse
from connectpyse.system import member


class MembersAPI(restapi.Client):

    module_url = 'system'

    def __init__(self):
        super(MembersAPI, self).__init__('{}/{}'.format(connectpyse.API_URL, MembersAPI.module_url))

    def get_members(self, user_params={}):
        json_results = self.members.get(user_headers=connectpyse.basic_auth, user_params=user_params)
        for json in json_results:
            yield member.Member(json)

    def create_member(self):
        pass

    def get_members_count(self):
        json_results = self.members.get(the_id='count', user_headers=connectpyse.basic_auth)
        count = json_results['count']
        return count

    def get_member_by_id(self, member_id):
        a_member = member.Member(self.members.get(the_id=member_id, user_headers=connectpyse.basic_auth))
        return a_member

    def delete_member_by_id(self, member_id):
        pass

    def replace_member(self, member_id):
        pass

    def update_member(self, member_id):
        pass

    def merge_member(self, member_id):
        pass

# get
# create
# count
# search
# betbyid
# delete
# replace
# update
# activities
# count
# timeentries
# count
# scheduleentries
# count
# documents
# count
# products
# count
# configurations
# createconfigurations
# count
# betbyid
# delete
