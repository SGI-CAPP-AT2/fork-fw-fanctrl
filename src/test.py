"""
This test is added for quick check without installation of fw_fanctrl
"""
from fw_fanctrl.hardwareController.EctoolHardwareController import EctoolHardwareController

ectoolhwc = EctoolHardwareController(no_battery_sensor_mode=False)
print("The temprature is: ")
print(ectoolhwc.get_temperature())