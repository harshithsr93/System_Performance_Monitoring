# Author    : Harshith S R
# Date      : 22/08/2018

class Memory:

    def __init__(self):
        self.virtual = None
        self.swap = None

    @property
    def get_virtual(self):
        return self.virtual

    @get_virtual.setter
    def set_virtual(self, virtual):
        self.virtual = virtual

    @property
    def get_swap(self):
        return self.swap

    @get_swap.setter
    def set_swap(self, swap):
        self.swap = swap
