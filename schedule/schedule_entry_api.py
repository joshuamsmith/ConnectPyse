from cw_controller import CWController
# Class for /system/members
from schedule import schedule_entry


class ScheduleEntryAPI(CWController):
    def __init__(self):
        self.module_url = 'schedule'
        self.module = 'entries'
        self._class = schedule_entry.ScheduleEntry
        super().__init__()  # instance gets passed to parent object

    def get_scheduleEntries(self):
        return super()._get()

    def create_schedulEntry(self, a_type):
        return super()._create(a_type)

    def get_scheduleEntries_count(self):
        return super()._get_count()

    def get_scheduleEntry_by_id(self, type_id):
        return super()._get_by_id(type_id)

    def delete_scheduleEntry_by_id(self, type_id):
        super()._delete_by_id(type_id)

    def replace_schedueEntry(self, type_id):
        pass

    def update_scheduleEntry(self, type_id, key, value):
        return super()._update(type_id, key, value)

    def merge_scheduleEntry(self, a_type, target_type_id):
        # return super()._merge(a_type, target_type_id)
        pass
