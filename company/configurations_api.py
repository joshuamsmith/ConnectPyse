from ..cw_controller import CWController
# Class for /company/configurations
from . import configuration


class ConfigurationsAPI(CWController):
    def __init__(self):
        self.module_url = 'company'
        self.module = 'configurations'
        self._class = configuration.Configuration
        super().__init__()  # instance gets passed to parent object

    def get_configurations(self):
        return super()._get()

    def create_configuration(self, a_configuration):
        return super()._create(a_configuration)

    def get_configurations_count(self):
        return super()._get_count()

    def get_configuration_by_id(self, configuration_id):
        return super()._get_by_id(configuration_id)

    def delete_configuration_by_id(self, configuration_id):
        super()._delete_by_id(configuration_id)

    def replace_configuration(self, configuration_id):
        pass

    def update_configuration(self, configuration_id, key, value):
        return super()._update(configuration_id, key, value)

