class ActiveConnection:

    def __init__(self):

        self.tcp_connection = []
        self.udp_connection = []

    @property
    def get_tcp_connection(self):
        return self.tcp_connection

    @get_tcp_connection.setter
    def set_tcp_connection(self, connection):
        self.tcp_connection = connection

    @property
    def get_udp_connection(self):
        return self.udp_connection

    @get_udp_connection.setter
    def set_udp_connection(self, connection):
        self.udp_connection = connection
