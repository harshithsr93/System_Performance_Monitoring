# Author    : Harshith S R
# Date      : 22/08/2018

class Cpu:

    def __init__(self):

        self.architecture = ""
        self.op_modes = ""
        self.byte_order = ""
        self.cpu_s = 0
        self.on_line_cpu = ""
        self.threads_per_core = 0
        self.core_per_socket = 0
        self.sockets = 0
        self.numa_nodes = 0
        self.vendor_id = ""
        self.cpu_family = 0
        self.model = 0
        self.model_name = ""
        self.stepping = 0
        self.cpu_mhz = 0
        self.cpu_max_mhz = 0
        self.cpu_min_mhz = 0
        self.bogo_mips = 0
        self.hypervisor_vendor = ""
        self.virtualization_type = ""
        self.l1d_cache = ""
        self.l1i_cache = ""
        self.l2_cache = ""
        self.l3_cache = ""

    @property
    def get_architecture(self):
        return self.architecture

    @get_architecture.setter
    def set_architecture(self, architecture):
        self.architecture = architecture

    @property
    def get_op_modes(self):
        return self.op_modes

    @get_op_modes.setter
    def set_op_modes(self, op_modes):
        self.op_modes = op_modes

    @property
    def get_byte_order(self):
        return self.byte_order

    @get_byte_order.setter
    def set_byte_order(self, byte_order):
        self.byte_order = byte_order

    @property
    def get_cpu_s(self):
        return self.cpu_s

    @get_cpu_s.setter
    def set_cpu_s(self, cpu):
        self.cpu_s = cpu

    @property
    def get_online_cpu(self):
        return self.on_line_cpu

    @get_online_cpu.setter
    def set_online_cpu(self, cpu):
        self.on_line_cpu = cpu

    @property
    def get_threads_per_core(self):
        return self.threads_per_core

    @get_threads_per_core.setter
    def set_threads_per_core(self, threads):
        self.threads_per_core = threads

    @property
    def get_core_per_socket(self):
        return self.core_per_socket

    @get_core_per_socket.setter
    def set_core_per_socket(self, core):
        self.core_per_socket = core

    @property
    def get_sockets(self):
        return self.sockets
    
    @get_sockets.setter
    def set_sockets(self, sockets):
        self.sockets = sockets

    @property
    def get_numa_nodes(self):
        return self.numa_nodes

    @get_numa_nodes.setter
    def set_numa_nodes(self, node):
        self.numa_nodes = node

    @property
    def get_vendor_id(self):
        return  self.vendor_id
    
    @get_vendor_id.setter
    def set_vendor_id(self, id):
        self.vendor_id = id
    
    @property
    def get_cpu_family(self):
        return self.cpu_family

    @get_cpu_family.setter
    def set_cpu_family(self, family):
        self.cpu_family = family

    @property
    def get_model(self):
        return self.model

    @get_model.setter
    def set_model(self, model):
        self.model = model

    @property
    def get_model_name(self):
        return self.model_name

    @get_model_name.setter
    def set_model_name(self, model):
        self.model_name = model

    @property
    def get_stepping(self):
        return self.stepping

    @get_stepping.setter
    def set_stepping(self, stepping):
        self.stepping = stepping

    @property
    def get_cpu_mhz(self):
        return self.cpu_mhz

    @get_cpu_mhz.setter
    def set_cpu_mhz(self, cpu_mhz):
        self.cpu_mhz = cpu_mhz

    @property
    def get_cpu_max_mhz(self):
        return self.cpu_max_mhz

    @get_cpu_max_mhz.setter
    def set_cpu_max_mhz(self, mhz):
        self.cpu_max_mhz = mhz

    @property
    def get_cpu_min_mhz(self):
        return self.cpu_min_mhz

    @get_cpu_min_mhz.setter
    def set_cpu_min_mhz(self, mhz):
        self.cpu_min_mhz = mhz

    @property
    def get_bogo_mips(self):
        return self.bogo_mips

    @get_bogo_mips.setter
    def set_bogo_mips(self, bogo):
        self.bogo_mips = bogo

    @property
    def get_hypervisor_vendor(self):
        return self.hypervisor_vendor

    @get_hypervisor_vendor.setter
    def set_hypervisor_vendor(self, vendor):
        self.hypervisor_vendor = vendor

    @property
    def get_virualization_type(self):
        return self.virtualization_type

    @get_virualization_type.setter
    def set_virualization_type(self, type):
        self.virtualization_type = type

    @property
    def get_l1d_cache(self):
        return self.l1d_cache

    @get_l1d_cache.setter
    def set_l1d_cache(self, cache):
        self.l1d_cache = cache

    @property
    def get_l1i_cache(self):
        return self.l1i_cache

    @get_l1i_cache.setter
    def set_l1i_cache(self, cache):
        self.l1i_cache = cache

    @property
    def get_l2_cache(self):
        return self.l2_cache

    @get_l2_cache.setter
    def set_l2_cache(self, cache):
        self.l2_cache = cache

    @property
    def get_l3_cache(self):
        return self.l3_cache

    @get_l3_cache.setter
    def set_l3_cache(self, cache):
        self.l3_cache = cache