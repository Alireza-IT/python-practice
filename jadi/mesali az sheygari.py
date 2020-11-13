
class Device:
    count = 0

    def __init__(self, ip, mac, name):
        self.ip = ip
        self.mac = mac
        self.name = name
        Device.count += 1
        # init the device & ping the device and store in result
        result = "ping the device"
        if result:
            self.status = 'active'
        else:
            self.status = "unknows"

    def get_status(self):
        # return result based on ping results for self.ip
        pass


class TV(Device):

    def turn_on(self):
        # connect to self ip and turn on
        pass

    def turn_off(self):
        # connect to self ip and turn off
        pass


class Thermo(Device):
    def get_degree(self):
        # connect to self.ip and read degree and return result
        pass


class SmartTV(TV):
    def turn_on(self):
        # turn on the smart tv from self.ip
        pass
