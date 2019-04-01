class UDP:

    def __init__(self):

        self.protocol = ""
        self.recv_q = 0
        self.send_q = 0
        self.local_address = ""
        self.foreign_address = ""
        self.state = ""
        self.program_name = ""

    @property
    def get_protocol(self):
        return self.protocol

    @get_protocol.setter
    def set_protocol(self, protocol):
        self.protocol = protocol

    @property
    def get_recv_q(self):
        return self.recv_q

    @get_recv_q.setter
    def set_recv_q(self, recv):
        self.recv_q = recv

    @property
    def get_send_q(self):
        return self.send_q

    @get_send_q.setter
    def set_send_q(self, send):
        self.send_q = send

    @property
    def get_local_address(self):
        return self.local_address

    @get_local_address.setter
    def set_local_address(self, address):
        self.local_address = address

    @property
    def get_foreign_address(self):
        return self.foreign_address

    @get_local_address.setter
    def set_foreign_address(self, address):
        self.foreign_address = address

    @property
    def get_state(self):
        return self.state

    @get_state.setter
    def set_state(self, state):
        self.state = state

    @property
    def get_program_name(self):
        return self.program_name

    @get_program_name.setter
    def set_program_name(self, name):
        self.program_name = name