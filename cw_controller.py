import restapi
# Class for /company/companies
import connectpyse


class CWController(restapi.Client):
    def __init__(self):
        # self.module_url comes from child
        # self.module comes from child
        self.conditions = ''
        self.orderBy = ''
        self.childconditions = ''
        self.customfieldconditions = ''
        self.page = ''
        self.pageSize = ''
        super().__init__('{}/{}'.format(connectpyse.API_URL, self.module_url))

    def _get(self, child, user_params={}):
        json_results = getattr(self, self.module).get(user_headers=connectpyse.basic_auth, user_params=user_params)
        for json in json_results:
            yield child(json)

    def _create(self, child, the_item):  # TODO: Test
        # Ideally take the_item and submit that as the user_data
        dict_post = {'name': the_item.name, 'company': the_item.company, 'type': the_item.type}
        an_instance = child(getattr(self, self.module).post(user_data=dict_post, user_headers=connectpyse.basic_auth))
        return an_instance

    def _get_count(self):
        json_results = getattr(self, self.module).get(the_id='count', user_headers=connectpyse.basic_auth)
        count = json_results['count']
        return count

    def _get_by_id(self, child, item_id):
        an_instance = child(getattr(self, self.module).get(the_id=item_id, user_headers=connectpyse.basic_auth))
        return an_instance

    def _delete_by_id(self, item_id):
        return getattr(self, self.module).delete(the_id=item_id, user_headers=connectpyse.basic_auth)

    def _replace(self, company_id):
        # copy code from _create once tested, use PUT verb
        pass

    def _update(self, child, item_id, key, value):
        # build PatchOperation dict
        patch_operation = [{
            'op': 'replace',
            'path': key,
            'value': value
        }]
        # call Patch method on API
        an_instance = child(getattr(self, self.module).patch(the_id=item_id, user_data=patch_operation,
                                                             user_headers=connectpyse.basic_auth))
        return an_instance

    def _merge(self, item_id, target_id):
        company_merge = [{
            'toCompanyId': target_id
        }]
        success_response = getattr(self, self.module).post(the_id=item_id, user_data=company_merge,
                                                           user_headers=connectpyse.basic_auth)
        return success_response
