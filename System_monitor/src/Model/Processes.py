# Author    : Harshith S R
# Date      : 22/08/2018

class Process:

    def __init__(self):
        self.pids = []

    @property
    def get_pid_list(self):
        return self.pids

    @get_pid_list.setter
    def set_pid_list(self, pid_list):
        self.pids = pid_list
