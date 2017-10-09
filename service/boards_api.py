from ..cw_controller import CWController
# Class for /service/boards
from . import board


class BoardsAPI(CWController):
    def __init__(self):
        self.module_url = 'service'
        self.module = 'boards'
        self._class = board.Board
        super().__init__()  # instance gets passed to parent object

    def get_boards(self):
        return super()._get()

    def create_board(self, a_entry):
        return super()._create(a_entry)

    def get_boards_count(self):
        return super()._get_count()

    def get_board_by_id(self, entry_id):
        return super()._get_by_id(entry_id)

    def delete_board_by_id(self, entry_id):
        super()._delete_by_id(entry_id)

    def replace_board(self, entry_id):
        pass

    def update_board(self, entry_id, key, value):
        return super()._update(entry_id, key, value)

    def merge_board(self, a_entry, target_entry_id):
        # return super()._merge(a_board, target_board_id)
        pass
