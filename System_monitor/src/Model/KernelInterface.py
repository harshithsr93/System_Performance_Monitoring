class Kernel:

    def __init__(self):

        self.interface = []

    @property
    def get_kernel_interface(self):
        return self.interface

    @get_kernel_interface.setter
    def set_kernel_interface(self, interface):
        self.interface = interface