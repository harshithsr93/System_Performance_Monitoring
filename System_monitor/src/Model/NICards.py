# Author    : Harshith S R
# Date      : 22/08/2018

class Cards:

    def __init__(self):

        self.inet = ""
        self.net_mask = ""
        self.inet6 = ""

    @property
    def get_inet(self):
        return self.inet

    @get_inet.setter
    def set_address(self, inet):
        self.inet = inet

    @property
    def get_net_mask(self):
        return self.net_mask

    @get_net_mask.setter
    def set_net_mask(self, net_mask):
        self.net_mask = net_mask

    @property
    def get_inet6(self):
        return self.inet6

    @get_inet6.setter
    def set_inet6(self, inet6):
        self.inet6 = inet6