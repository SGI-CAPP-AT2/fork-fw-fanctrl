"""
This test is added for quick check without installation of fw_fanctrl
"""
from fw_fanctrl.hardwareController.EctoolHardwareController import EctoolHardwareController
from lib_example.shgi_mod import get_temprature_py, get_temperature_by_sensors_py
# Test the cython wrapper

print(get_temperature_by_sensors_py(['c1', 'c2', 'c3']))
print(get_temprature_py())

# Test the EctoolHardwareController
ectoolhwc = EctoolHardwareController(no_battery_sensor_mode=False)
print("The temprature is: ")
print(ectoolhwc.get_temperature())
ectoolhwcws = EctoolHardwareController(no_battery_sensor_mode=True)
print("The temprature with no battery sensors is: ")
print(ectoolhwcws.get_temperature())