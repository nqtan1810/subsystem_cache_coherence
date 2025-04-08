# *******************************************************************************
# this class define a simple CPU with read and write operation
# *******************************************************************************

import os
from bi_directional_port import *
from transaction import *
from subsystem_parameter import *

class cache_word:
    def __init__(self, addr=0, data=0):
        self.addr = addr
        self.data = data

class processor:
    def __init__(self, name='', instr_mem_dir_path='testcase', read_data_dir_path='result',delay=0, lower_addr=CPU_0_LOWER_BOUND, upper_addr=CPU_0_UPPER_BOUND):
        self.name = name
        print(f"{self.name} is created!")

        # path for output file
        self.read_data_path = os.path.join(read_data_dir_path, f'read_data_{self.name[len(self.name)-1]}.mem')

        # read data queue
        self.read_data_q = []

        # base address
        self.lower_addr = lower_addr
        self.upper_addr = upper_addr

        # internal queues
        self.instr_mem = []
        # self.data_mem = [0] * (3*(2**10))

        # port to CACHE_L1_x
        self.s_port = bi_directional_port(self.name+'.s_port')

        # CPU Controller
        self.state = 'IDLE'
        self.next_state = 'IDLE'

        self.delay = delay
        self.delay_cnt = 0
        self.shutdown = 0
        self.init(instr_mem_dir_path)

    # init data memory and instruction memory
    def init(self, instr_mem_path='testcase'):
        current_path = os.path.dirname(os.path.abspath(__file__))
        index_str = self.name[len(self.name)-1]
        instr_file_path = os.path.join(current_path, f"{instr_mem_path}\\instr_mem_{index_str}.mem")
        instr_file = open(instr_file_path, "r")
        self.instr_mem = instr_file.readlines()
        instr_file.close()

        # convert hex string in instr_mem into int values
        for i in range(len(self.instr_mem)):
            self.instr_mem[i] = self.instr_mem[i].split()
            if(self.instr_mem[i][0] == 'read'):
                self.instr_mem[i][1] = int(self.instr_mem[i][1], 16)
            elif(self.instr_mem[i][0] == 'write'):
                self.instr_mem[i][1] = int(self.instr_mem[i][1], 16)
                self.instr_mem[i][2] = int(self.instr_mem[i][2], 16)

    def convert2local_addr(self, addr_in):
        if addr_in >= self.lower_addr and addr_in <= self.upper_addr:
            return addr_in - self.lower_addr
        elif addr_in >= SHARE_LOWER_BOUND and addr_in <= SHARE_UPPER_BOUND:
            return  addr_in - SHARE_LOWER_BOUND + (self.upper_addr - self.lower_addr)

    def send_slave(self, sys_c):
        if len(self.instr_mem) > 0:
            if self.state == 'SEND_REQ':                    # CPU is ready to Read/Write
                if self.s_port.s_ready == 1:
                    tmp_req = self.instr_mem[0]
                    req = transaction()
                    req.pack_trans(tmp_req)                 # convert instruction to transaction
                    req.id = sys_c.cycle
                    if req.wr_en:
                        req.wlast = 1
                        self.s_port.send_slave(req)
                        print(f"[Cycle {str(sys_c.cycle).rjust(CYCLE_PRINT_WIDTH, ' ')}]: {self.name.ljust(10, ' ')}: Sent Write Request to Slave: {req}")
                        self.next_state = 'WAIT_WRESP'
                        self.instr_mem.pop(0)
                    else:
                        self.s_port.send_slave(req)
                        self.next_state = 'WAIT_RRESP'
                        self.instr_mem.pop(0)
                        print(f"[Cycle {str(sys_c.cycle).rjust(CYCLE_PRINT_WIDTH, ' ')}]: {self.name.ljust(10, ' ')}: Sent Read Request to Slave: {req}")
            elif self.state == 'IDLE':
                if self.delay_cnt == self.delay:
                    self.next_state = 'SEND_REQ'            # expect to send request in next cycle
                    self.delay_cnt = 0
                else:
                    self.delay_cnt = self.delay_cnt + 1
                    self.next_state = 'IDLE'
            elif self.state == 'WAIT_RRESP' or self.state == 'WAIT_WRESP':
                self.next_state = self.state
        elif self.state == 'IDLE':                          # all CPU's instructions are sent and all response received
            self.next_state = 'IDLE'
            if not self.shutdown:
                print(f"[Cycle {str(sys_c.cycle).rjust(CYCLE_PRINT_WIDTH, ' ')}]: {self.name.ljust(10, ' ')}: Is ALL DONE!" )
                self.shutdown = 1

    def recv_slave(self, sys_c):
        if self.state == 'WAIT_RRESP' or self.state == 'WAIT_WRESP':
            if self.s_port.s_valid == 1:
                resp = self.s_port.recv_slave()
                # self.data_mem.append(resp)
                if resp.rlast:
                    read_data = cache_word(resp.addr, resp.data)
                    self.read_data_q.append(read_data)
                    print(f"[Cycle {str(sys_c.cycle).rjust(CYCLE_PRINT_WIDTH, ' ')}]: {self.name.ljust(10, ' ')}: Received a Read Response from Slave: {resp}")
                    self.next_state = 'IDLE'
                if resp.wdone:
                    print(f"[Cycle {str(sys_c.cycle).rjust(CYCLE_PRINT_WIDTH, ' ')}]: {self.name.ljust(10, ' ')}: Received a Write Response from Slave: {resp}")
                    self.next_state = 'IDLE'

    def save_read_data(self):
        with open(self.read_data_path, 'w') as file:
            for word in self.read_data_q:
                line = f"0x{word.addr:08x} 0x{word.data:08x}\n"
                file.write(line)


    def run(self, sys_c):
        self.send_slave(sys_c)
        self.recv_slave(sys_c)


    def update(self):
        # update state and next_state
        self.state = self.next_state
        self.next_state = self.state

        # update port
        self.s_port.update()
