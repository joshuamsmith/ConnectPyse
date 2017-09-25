from ..cw_controller import CWController
# Class for /schedule/types
from connectpyse.schedule import schedule_type


class ScheduleTypesAPI(CWController):
    def __init__(self):
        self.module_url = 'schedule'
        self.module = 'types'
        self._class = schedule_type.ScheduleType
        super().__init__()  # instance gets passed to parent object

    def get_schedule_types(self):
        return super()._get()

    def create_schedule_type(self, a_type):
        return super()._create(a_type)

    def get_schedule_types_count(self):
        return super()._get_count()

    def get_schedule_type_by_id(self, type_id):
        return super()._get_by_id(type_id)

    def delete_schedule_type_by_id(self, type_id):
        super()._delete_by_id(type_id)

    def replace_schedule_type(self, type_id):
        pass

    def update_schedule_type(self, type_id, key, value):
        return super()._update(type_id, key, value)

    def merge_schedule_type(self, a_type, target_type_id):
        # return super()._merge(a_schedule_type, target_schedule_type_id)
        pass
