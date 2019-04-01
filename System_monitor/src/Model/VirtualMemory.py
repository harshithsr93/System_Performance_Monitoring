# Author    : Harshith S R
# Date      : 22/08/2018

class Virtual:

    def __init__(self):
        self.total = 0
        self.used = 0
        self.available = 0
        self.free = 0
        self.active = 0
        self.inactive = 0
        self.buffers = 0
        self.cached = 0
        self.slab = 0

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
    def get_available(self):
        return self.available

    @get_available.setter
    def set_available(self, available):
        self.available =available

    @property
    def get_free(self):
        return self.free

    @get_free.setter
    def set_free(self, free):
        self.free = free

    @property
    def get_active(self):
        return self.active

    @get_active.setter
    def set_active(self, active):
        self.active = active

    @property
    def get_inactive(self):
        return self.inactive

    @get_inactive.setter
    def set_inactive(self, inactive):
        self.inactive = inactive

    @property
    def get_buffer(self):
        return self.buffers

    @get_buffer.setter
    def set_buffer(self, buffer):
        self.buffers = buffer

    @property
    def get_cached(self):
        return self.cached

    @get_cached.setter
    def set_cached(self, cached):
        self.cached = cached

    @property
    def get_slab(self):
        return self.slab

    @get_slab.setter
    def set_slab(self, slab):
        self.slab = slab
