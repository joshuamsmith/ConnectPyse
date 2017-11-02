from ..cw_controller import CWController
# Class for /time/entries
from . import time_entry


class TimeEntriesAPI(CWController):
    def __init__(self):
        self.module_url = 'time'
        self.module = 'entries'
        self._class = time_entry.TimeEntry
        super().__init__()  # instance gets passed to parent object

    def get_time_entries(self):
        return super()._get()

    def create_time_entry(self, a_time_entry):
        return super()._create(a_time_entry)

    def get_time_entries_count(self):
        return super()._get_count()

    def get_time_entry_by_id(self, time_entry_id):
        return super()._get_by_id(time_entry_id)

    def delete_time_entry_by_id(self, time_entry_id):
        super()._delete_by_id(time_entry_id)

    def replace_time_entry(self, time_entry_id):
        pass

    def update_time_entry(self, time_entry_id, key, value):
        return super()._update(time_entry_id, key, value)