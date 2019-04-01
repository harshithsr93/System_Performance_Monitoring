# Author    : Harshith S R
# Date      : 22/08/2018

class Disk:

    def __init__(self):

        self.partition = None

    @property
    def get_partition(self):
        return self.partition

    @get_partition.setter
    def set_partition(self, partition):
        self.partition = partition