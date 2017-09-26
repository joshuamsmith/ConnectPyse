from ..cw_controller import CWController
# Class for /system/callbacks
from connectpyse.system import callback


class CallbacksAPI(CWController):
    def __init__(self):
        self.module_url = 'system'
        self.module = 'callbacks'
        self._class = callback.Callback
        super().__init__()  # instance gets passed to parent object

    def get_callbacks(self):
        return super()._get()

    def create_callback(self, a_entry):
        return super()._create(a_entry)

    def get_callbacks_count(self):
        return super()._get_count()

    def get_callback_by_id(self, entry_id):
        return super()._get_by_id(entry_id)

    def delete_callback_by_id(self, entry_id):
        super()._delete_by_id(entry_id)

    def replace_callback(self, entry_id):
        pass

    def update_callback(self, entry_id, key, value):
        return super()._update(entry_id, key, value)

    def merge_callback(self, a_entry, target_entry_id):
        # return super()._merge(a_callback, target_callback_id)
        pass
