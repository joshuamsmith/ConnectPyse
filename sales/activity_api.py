from ..cw_controller import CWController
# Class for /sales/activity
from . import activity


class ActivityAPI(CWController):
    def __init__(self):
        self.module_url = 'sales'
        self.module = 'activities'
        self._class = activity.Activity
        super().__init__()  # instance gets passed to parent object

    def get_activities(self):
        return super()._get()

    def create_activity(self, a_type):
        return super()._create(a_type)

    def get_activities_count(self):
        return super()._get_count()

    def get_activity_by_id(self, type_id):
        return super()._get_by_id(type_id)

    def delete_activity_by_id(self, type_id):
        super()._delete_by_id(type_id)

    def replace_activity(self, type_id):
        pass

    def update_activity(self, type_id, key, value):
        return super()._update(type_id, key, value)

    def merge_activity(self, a_type, target_type_id):
        # return super()._merge(a_type, target_type_id)
        pass
