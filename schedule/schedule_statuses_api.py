from ..cw_controller import CWController
# Class for /schedule/statuses
from connectpyse.schedule import schedule_status


class ScheduleStatusesAPI(CWController):
    def __init__(self):
        self.module_url = 'schedule'
        self.module = 'statuses'
        self._class = schedule_status.ScheduleStatus
        super().__init__()  # instance gets passed to parent object

    def get_schedule_statuses(self):
        return super()._get()

    def create_schedule_status(self, a_status):
        return super()._create(a_status)

    def get_schedule_statuses_count(self):
        return super()._get_count()

    def get_schedule_status_by_id(self, status_id):
        return super()._get_by_id(status_id)

    def delete_schedule_status_by_id(self, status_id):
        super()._delete_by_id(status_id)

    def replace_schedule_status(self, status_id):
        pass

    def update_schedule_status(self, status_id, key, value):
        return super()._update(status_id, key, value)

    def merge_schedule_status(self, a_status, target_status_id):
        # return super()._merge(a_schedule_status, target_schedule_status_id)
        pass
