from ..cw_controller import CWController
# Class for /schedule/entries
from schedule import schedule_entry


class ScheduleEntriesAPI(CWController):
    def __init__(self):
        self.module_url = 'schedule'
        self.module = 'entries'
        self._class = schedule_entry.ScheduleEntry
        super().__init__()  # instance gets passed to parent object

    def get_schedule_entries(self):
        return super()._get()

    def create_schedule_entry(self, a_entry):
        return super()._create(a_entry)

    def get_schedule_entries_count(self):
        return super()._get_count()

    def get_schedule_entry_by_id(self, entry_id):
        return super()._get_by_id(entry_id)

    def delete_schedule_entry_by_id(self, entry_id):
        super()._delete_by_id(entry_id)

    def replace_schedule_entry(self, entry_id):
        pass

    def update_schedule_entry(self, entry_id, key, value):
        return super()._update(entry_id, key, value)

    def merge_schedule_entry(self, a_entry, target_entry_id):
        # return super()._merge(a_schedule_entry, target_schedule_entry_id)
        pass
