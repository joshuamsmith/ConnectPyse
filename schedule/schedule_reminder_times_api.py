from ..cw_controller import CWController
# Class for /schedule/reminderTimes
from connectpyse.schedule import schedule_reminder_time

''' not available until 2017.3 '''
class ScheduleReminderTimesAPI(CWController):
    def __init__(self):
        self.module_url = 'schedule'
        self.module = 'reminderTimes'
        self._class = schedule_reminder_time.ScheduleReminderTime
        super().__init__()  # instance gets passed to parent object

    def get_schedule_reminder_times(self):
        return super()._get()

    def create_schedule_reminder_time(self, a_reminder_time):
        return super()._create(a_reminder_time)

    def get_schedule_reminder_times_count(self):
        return super()._get_count()

    def get_schedule_reminder_time_by_id(self, reminder_time_id):
        return super()._get_by_id(reminder_time_id)

    def delete_schedule_reminder_time_by_id(self, reminder_time_id):
        super()._delete_by_id(reminder_time_id)

    def replace_schedule_reminder_time(self, reminder_time_id):
        pass

    def update_schedule_reminder_time(self, reminder_time_id, key, value):
        return super()._update(reminder_time_id, key, value)

    def merge_schedule_reminder_time(self, a_reminder_time, target_reminder_time_id):
        # return super()._merge(a_schedule_reminder_time, target_schedule_reminder_time_id)
        pass
