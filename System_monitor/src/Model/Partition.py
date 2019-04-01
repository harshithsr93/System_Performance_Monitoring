class Partitions:

    def __init__(self):

        self.disk_partition = []
        self.file_system_partition = []

    @property
    def get_disk_partition(self):
        return self.disk_partition

    @get_disk_partition.setter
    def set_disk_partition(self, disk):
        self.disk_partition = disk

    @property
    def get_file_system_partition(self):
        return self.file_system_partition

    @get_file_system_partition.setter
    def set_file_system_partition(self, file):
        self.file_system_partition = file
