class Partition:

    def __init__(self):

        self.name = ""
        self.size = ""
        self.used = ""
        self.available = ""
        self.use_percentage = ""
        self.mount_on = ""

    @property
    def get_name(self):
        return self.name

    @get_name.setter
    def set_name(self, name):
        self.name = name

    @property
    def get_size(self):
        return self.size

    @get_size.setter
    def set_size(self, size):
        self.size = size

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
        self.available = available

    @property
    def get_use_percentage(self):
        return self.use_percentagee

    @get_use_percentage.setter
    def set_use_percentage(self, use):
        self.use_percentage = use

    @property
    def get_mount_on(self):
        return self.mount_on

    @get_mount_on.setter
    def set_mount_on(self, point):
        self.mount_on = point

