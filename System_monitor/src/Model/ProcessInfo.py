# Author    : Harshith S R
# Date      : 22/08/2018

class Information:

    def __init__(self):

        self.user = ""
        self.pid = 0
        self.cpu_percentage = 0
        self.memory_percentage = 0
        self.time = ""
        self.command = ""

    @property
    def get_user(self):
        return self.user

    @get_user.setter
    def set_user(self, user):
        self.user = user

    @property
    def get_pid(self):
        return self.pid

    @get_pid.setter
    def set_pid(self, pid):
        self.pid = pid

    @property
    def get_cpu_percentage(self):
        return self.cpu_percentage

    @get_cpu_percentage.setter
    def set_cpu_percentage(self, percentage):
        self.cpu_percentage = percentage

    @property
    def get_memory_percentage(self):
        return self.memory_percentage

    @get_memory_percentage.setter
    def set_memory_percentage(self, percentage):
        self.memory_percentage = percentage

    @property
    def get_time(self):
        return self.time

    @get_time.setter
    def set_time(self, time):
        self.time = time

    @property
    def get_command(self):
        return self.command

    @get_command.setter
    def set_command(self, command):
        self.command = command

    def to_string(self):

        return '%s %s %s %s %s %s' % (self.user, self.pid, self.command,
                                      self.memory_percentage, self.cpu_percentage,
                                      self.time)
