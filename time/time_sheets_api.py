from ..cw_controller import CWController
# Class for /time/entries
from . import time_sheet


class TimeSheetsAPI(CWController):
    def __init__(self, **kwargs):
        self.module_url = 'time'
        self.module = 'sheets'
        self._class = time_sheet.TimeSheet
        super().__init__(**kwargs)  # instance gets passed to parent object

    def get_time_sheets(self):
        return super()._get()

    def get_time_sheet_by_id(self, time_sheet_id):
        return super()._get_by_id(time_sheet_id)

    def submit_time_sheet_by_id(self, time_sheet_id):
        return super()._post_dict("{}/submit".format(str(time_sheet_id)), {"approvalType": "tier1update"})

    def reverse_time_sheet_by_id(self, time_sheet_id):
        return super()._post_dict("{}/reverse".format(str(time_sheet_id)))

    def reject_time_sheet_by_id(self, time_sheet_id):
        return super()._post_dict("{}/reject".format(str(time_sheet_id)), {"approvalType": "tier1update"})

    def approve_time_sheet_by_id(self, time_sheet_id):
        return super()._post_dict("{}/approve".format(str(time_sheet_id)), {"approvalType": "tier1update"})