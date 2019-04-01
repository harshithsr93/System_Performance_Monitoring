class Interface:

    def __init__(self):

        self.iface = ""
        self.ip_address = ""
        self.mtu = 0
        self.rx_ok = 0
        self.rx_err = 0
        self.rx_drp = 0
        self.rx_ovr = 0
        self.tx_ok = 0
        self.tx_err = 0
        self.tx_drp = 0
        self.tx_ovr = 0
        self.flag = ""

    @property
    def get_iface(self):
        return self.iface

    @get_iface.setter
    def set_iface(self, iface):
        self.iface = iface

    @property
    def get_ip_address(self):
        return self.ip_address

    @get_ip_address.setter
    def set_ip_address(self, ip):
        self.ip_address = ip

    @property
    def get_mtu(self):
        return self.mtu

    @get_mtu.setter
    def set_mtu(self, mtu):
        self.mtu = mtu

    @property
    def get_rx_ok(self):
        return self.rx_ok

    @get_rx_ok.setter
    def set_rx_ok(self, rx):
        self.rx_ok = rx

    @property
    def get_rx_err(self):
        return self.rx_err

    @get_rx_err.setter
    def set_rx_err(self, rx):
        self.rx_err = rx

    @property
    def get_rx_drp(self):
        return self.rx_drp

    @get_rx_drp.setter
    def set_rx_drp(self, rx):
        self.rx_drp = rx

    @property
    def get_rx_ovr(self):
        return self.rx_ovr

    @get_rx_ovr.setter
    def set_rx_ovr(self, rx):
        self.rx_ovr = rx

    @property
    def get_tx_ok(self):
        return self.rx_ok

    @get_tx_ok.setter
    def set_tx_ok(self, tx):
        self.tx_ok = tx

    @property
    def get_tx_err(self):
        return self.tx_err

    @get_tx_err.setter
    def set_tx_err(self, tx):
        self.tx_err = tx

    @property
    def get_tx_drp(self):
        return self.tx_drp

    @get_tx_drp.setter
    def set_tx_drp(self, tx):
        self.tx_drp = tx

    @property
    def get_tx_ovr(self):
        return self.tx_ovr

    @get_tx_ovr.setter
    def set_tx_ovr(self, tx):
        self.tx_ovr = tx

    @property
    def get_flag(self):
        return self.flag

    @get_flag.setter
    def set_flag(self, flag):
        self.flag = flag
