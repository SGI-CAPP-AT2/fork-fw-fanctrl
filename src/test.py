from fw_fanctrl.hardwareController.EctoolHardwareController import EctoolHardwareController

ectoolhwc = EctoolHardwareController(no_battery_sensor_mode=False)
print("The temprature is: ")
print(ectoolhwc.get_temperature())