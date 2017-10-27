from ..cw_controller import CWController
# Class for /procurement/shipmentmethods
from . import shipment_method


class ShipmentMethodsAPI(CWController):
    def __init__(self):
        self.module_url = 'procurement'
        self.module = 'shipmentmethods'
        self._class = shipment_method.ShipmentMethod
        super().__init__()  # instance gets passed to parent object

    def get_shipment_methods(self):
        return super()._get()

    def create_shipment_method(self, a_shipment_method):
        return super()._create(a_shipment_method)

    def get_shipment_methods_count(self):
        return super()._get_count()

    def get_shipment_method_by_id(self, shipment_method_id):
        return super()._get_by_id(shipment_method_id)

    def delete_shipment_method_by_id(self, shipment_method_id):
        super()._delete_by_id(shipment_method_id)

    def replace_shipment_method(self, shipment_method_id):
        pass

    def update_shipment_method(self, shipment_method_id, key, value):
        return super()._update(shipment_method_id, key, value)