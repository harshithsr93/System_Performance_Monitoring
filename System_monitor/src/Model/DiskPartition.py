class Partition:

    def __init__(self):

        self.name = ""
        self.rm = 0
        self.size = ""
        self.type = ""
        self.mount_point = ""

    @property
    def get_name(self):
        return self.name

    @get_name.setter
    def set_name(self, name):
        self.name = name

    @property
    def get_rm(self):
        return self.rm

    @get_rm.setter
    def set_rm(self, rm):
        self.rm = rm

    @property
    def get_size(self):
        return self.size

    @get_size.setter
    def set_size(self, size):
        self.size = size

    @property
    def get_mount_point(self):
        return self.mount_point

    @get_mount_point.setter
    def set_mount_point(self, point):
        self.mount_point = point

    @property
    def get_type(self):
        return self.type

    @get_type.setter
    def set_type(self, dtype):
        self.type = dtype
