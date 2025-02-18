"""
This test is added for quick check without installation of fw_fanctrl
"""
from fw_fanctrl.hardwareController.EctoolHardwareController import EctoolHardwareController

ectoolhwc = EctoolHardwareController(no_battery_sensor_mode=False)
print("The temprature is: ")
print(ectoolhwc.get_temperature())
ectoolhwcws = EctoolHardwareController(no_battery_sensor_mode=True)
print("The temprature with no battery sensors is: ")
print(ectoolhwcws.get_temperature())