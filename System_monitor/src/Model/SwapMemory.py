# Author    : Harshith S R
# Date      : 22/08/2018

class Swap:

    def __init__(self):
        self.total = 0
        self.used = 0
        self.free = 0

    @property
    def get_total(self):
        return self.total

    @get_total.setter
    def set_total(self, total):
        self.total = total

    @property
    def get_used(self):
        return self.used

    @get_used.setter
    def set_used(self, used):
        self.used = used

    @property
    def get_free(self):
        return self.free

    @get_free.setter
    def set_free(self, free):
        self.free = free
