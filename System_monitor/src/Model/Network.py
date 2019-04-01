# Author    : Harshith S R
# Date      : 22/08/2018

class Network:

    def __init__(self):

        self.active_internet_connection= None
        self.kernel_interface = None

    @property
    def get_active_internet_connection(self):
        return self.active_internet_connection

    @get_active_internet_connection.setter
    def set_active_internet_connection(self, aic):
        self.active_internet_connection = aic

    @property
    def get_kernel_interfaces(self):
        return self.kernel_interface

    @get_kernel_interfaces.setter
    def set_kernel_interface(self, interface):
        self.kernel_interface = interface

