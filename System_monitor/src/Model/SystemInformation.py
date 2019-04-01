class Information:

    def __init__(self):

        self.host_name = ""
        self.ip_address = ""

    @property
    def get_host_name(self):
        return self.host_name

    @get_host_name.setter
    def set_host_name(self, name):
        self.host_name = name

    @property
    def get_ip_address(self):
        return self.ip_address

    @get_ip_address.setter
    def set_ip_address(self, address):
        self.ip_address = address
