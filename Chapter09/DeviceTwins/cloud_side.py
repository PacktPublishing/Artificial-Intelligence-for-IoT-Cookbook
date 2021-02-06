import sys
from time import sleep
from azure.iot.hub import IoTHubRegistryManager
from azure.iot.hub.models import Twin, TwinProperties, QuerySpecification, QueryResult

iothub_registry_manager = IoTHubRegistryManager("Service Connection String")

twin = iothub_registry_manager.get_twin("Device_id")
twin_patch = Twin( properties= TwinProperties(desired={'Vision_Model_Version' : 1.2}))
twin = iothub_registry_manager.update_twin(DEVICE_ID, twin_patch, twin.etag)


query_spec = QuerySpecification(query="SELECT * FROM devices WHERE properties.reported.Vision_Model_Version <> 1.2")
query_result = iothub_registry_manager.query_iot_hub(query_spec, None, 100)
print("Devices that did not update: {}".format(', '.join([twin.device_id for twin in query_result.items])))

print()

query_spec = QuerySpecification(query="SELECT * FROM devices WHERE tags.location.plant = 'Redmond43' AND properties.reported.connectivity = 'cellular'")
query_result = iothub_registry_manager.query_iot_hub(query_spec, None, 100)
print("Devices in Redmond43 plant using cellular network: {}".format(', '.join([twin.device_id for twin in query_result.items])))
