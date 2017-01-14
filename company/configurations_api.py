import restapi

from company import configuration


class ConfigurationsAPI(restapi.Client):

    module_url = 'company'

    def __init__(self, base_url):
        super(ConfigurationsAPI, self).__init__('{}/{}'.format(base_url, ConfigurationsAPI.module_url))

    def get_configurations(self, user_headers, user_params=None):
        json_results = self.configurations.get(user_headers=user_headers, user_params=user_params)
        for json in json_results:
            yield configuration.Configuration(json)

    def create_configuration(self, user_headers, a_config):
        dict_post = {'name': a_config.name, 'company': a_config.company, 'type': a_config.type}
        json_results = self.configurations.post(user_data=dict_post, user_headers=user_headers)
  #      status_code = json_results.status_code
        return json_results

    def get_configurations_count(self, user_headers):
        json_results = self.configurations.get(the_id='count', user_headers=user_headers)
        count = json_results['count']
        return count

    def get_configuration_by_id(self, configuration_id, user_headers):
        a_configuration = configuration.Configuration(self.configurations.get(the_id=configuration_id, user_headers=user_headers))
        return a_configuration

    def delete_configuration_by_id(self, configuration_id   ):
        pass

    def replace_configuration(self, configuration_id):
        pass

    def update_configuration(self, configuration_id):
        pass

    def merge_configuration(self, configuration_id):
        pass
