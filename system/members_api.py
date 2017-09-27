from ..cw_controller import CWController
# Class for /system/members
from system import member


class MembersAPI(CWController):
    def __init__(self):
        self.module_url = 'system'
        self.module = 'members'
        self._class = member.Member
        super().__init__()  # instance gets passed to parent object

    def get_members(self):
        return super()._get()

    def create_member(self, a_type):
        return super()._create(a_type)

    def get_members_count(self):
        return super()._get_count()

    def get_member_by_id(self, type_id):
        return super()._get_by_id(type_id)

    def delete_member_by_id(self, type_id):
        super()._delete_by_id(type_id)

    def replace_member(self, type_id):
        pass

    def update_member(self, type_id, key, value):
        return super()._update(type_id, key, value)

    def merge_member(self, a_type, target_type_id):
        # return super()._merge(a_type, target_type_id)
        pass
