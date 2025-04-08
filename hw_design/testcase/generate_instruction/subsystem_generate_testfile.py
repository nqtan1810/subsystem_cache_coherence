import os
import random

# Hàm xử lý từng testcase trong nhóm 1.1
def testcase_1(n_set=16):
    base_path="subsystem_testcase/testcase_1/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,random.randint(1,4))
    chosen_tag=random.choice(selected_tags); all_tags=selected_tags+[chosen_tag]
    with open(path_0,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0000FFFF)|0x00000000; f.write(f"read\t0x{addr:08x}\n")
        word_offset=random.randint(0,15)
        addr=(chosen_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        addr=(addr&0x0000FFFF)|0x00000000; f.write(f"read\t0x{addr:08x}")
    with open(path_1,'w') as f: pass
    with open(path_mem,'w') as f:
        for tag in set(all_tags):
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0000FFC0)|0x00000000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t" + '\t'.join(data) + '\n')
    print("Testcase 1 created")
def testcase_2(n_set=16):
    base_path="subsystem_testcase/testcase_2/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,random.randint(1,3))
    remaining_tags=list(set(available_tags)-set(selected_tags)); extra_tag=random.choice(remaining_tags)
    all_tags=selected_tags+[extra_tag]
    with open(path_0,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0000FFFF)|0x00000000; f.write(f"read\t0x{addr:08x}\n")
        word_offset=random.randint(0,15)
        addr=(extra_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        addr=(addr&0x0000FFFF)|0x00000000; f.write(f"read\t0x{addr:08x}")
    with open(path_1,'w') as f: pass
    with open(path_mem,'w') as f:
        for tag in all_tags:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0000FFC0)|0x00000000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t" + '\t'.join(data) + '\n')
    print("Testcase 2 created")
def testcase_3(n_set=16):
    base_path="subsystem_testcase/testcase_3/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,4)
    remaining_tags=list(set(available_tags)-set(selected_tags)); extra_tag=random.choice(remaining_tags)
    all_tags=selected_tags+[extra_tag]
    with open(path_0,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0000FFFF)|0x00000000; f.write(f"read\t0x{addr:08x}\n")
        word_offset=random.randint(0,15)
        addr=(extra_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        addr=(addr&0x0000FFFF)|0x00000000; f.write(f"read\t0x{addr:08x}")
    with open(path_1,'w') as f: pass
    with open(path_mem,'w') as f:
        for tag in all_tags:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0000FFC0)|0x00000000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t" + '\t'.join(data) + '\n')
    print("Testcase 3 created")
def testcase_4(n_set=16):
    base_path="subsystem_testcase/testcase_4/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,4)
    remaining_tags=list(set(available_tags)-set(selected_tags)); extra_tag=random.choice(remaining_tags)
    all_tags=selected_tags+[extra_tag]
    with open(path_0,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0000FFFF)|0x00000000
            data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{addr:08x}\t{data}\n")
        word_offset=random.randint(0,15)
        addr=(extra_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        addr=(addr&0x0000FFFF)|0x00000000; f.write(f"read\t0x{addr:08x}")
    with open(path_1,'w') as f: pass
    with open(path_mem,'w') as f:
        for tag in all_tags:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0000FFC0)|0x00000000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t" + '\t'.join(data) + '\n')
    print("Testcase 4 created")
def testcase_5(n_set=16):
    base_path="subsystem_testcase/testcase_5/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,random.randint(1,4))
    chosen_tag=random.choice(selected_tags); all_tags=selected_tags+[chosen_tag]
    with open(path_0,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0000FFFF)|0x00000000; f.write(f"read\t0x{addr:08x}\n")
        word_offset=random.randint(0,15)
        addr=(chosen_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        addr=(addr&0x0000FFFF)|0x00000000
        data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{addr:08x}\t{data}")
    with open(path_1,'w') as f: pass
    with open(path_mem,'w') as f:
        for tag in set(all_tags):
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0000FFC0)|0x00000000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t" + '\t'.join(data) + '\n')
    print("Testcase 5 created")
def testcase_6(n_set=16):
    base_path="subsystem_testcase/testcase_6/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,random.randint(1,3))
    remaining_tags=list(set(available_tags)-set(selected_tags)); write_tag=random.choice(remaining_tags)
    all_tags=selected_tags+[write_tag]
    with open(path_0,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0000FFFF)|0x00000000; f.write(f"read\t0x{addr:08x}\n")
        word_offset=random.randint(0,15)
        addr=(write_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        addr=(addr&0x0000FFFF)|0x00000000
        data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{addr:08x}\t{data}")
    with open(path_1,'w') as f: pass
    with open(path_mem,'w') as f:
        for tag in all_tags:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0000FFC0)|0x00000000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t" + '\t'.join(data) + '\n')
    print("Testcase 6 created")
def testcase_7(n_set=16):
    base_path="subsystem_testcase/testcase_7/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,4)
    remaining_tags=list(set(available_tags)-set(selected_tags)); write_tag=random.choice(remaining_tags)
    all_tags=selected_tags+[write_tag]
    with open(path_0,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0000FFFF)|0x00000000; f.write(f"read\t0x{addr:08x}\n")
        word_offset=random.randint(0,15)
        addr=(write_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        addr=(addr&0x0000FFFF)|0x00000000
        data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{addr:08x}\t{data}")
    with open(path_1,'w') as f: pass
    with open(path_mem,'w') as f:
        for tag in all_tags:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0000FFC0)|0x00000000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t" + '\t'.join(data) + '\n')
    print("Testcase 7 created")
def testcase_8(n_set=16):
    base_path="subsystem_testcase/testcase_8/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,4)
    remaining_tags=list(set(available_tags)-set(selected_tags)); extra_tag=random.choice(remaining_tags)
    all_tags=selected_tags+[extra_tag]
    with open(path_0,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0000FFFF)|0x00000000
            data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{addr:08x}\t{data}\n")
        word_offset=random.randint(0,15)
        addr=(extra_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        addr=(addr&0x0000FFFF)|0x00000000
        data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{addr:08x}\t{data}")
    with open(path_1,'w') as f: pass
    with open(path_mem,'w') as f:
        for tag in all_tags:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0000FFC0)|0x00000000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t" + '\t'.join(data) + '\n')
    print("Testcase 8 created")
def testcase_9(n_set=16):
    base_path="subsystem_testcase/testcase_9/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,random.randint(1,4))
    chosen_tag=random.choice(selected_tags); all_tags=selected_tags+[chosen_tag]
    with open(path_1,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0000FFFF)|0x00010000; f.write(f"read\t0x{addr:08x}\n")
        word_offset=random.randint(0,15)
        addr=(chosen_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        addr=(addr&0x0000FFFF)|0x00010000; f.write(f"read\t0x{addr:08x}")
    with open(path_0,'w') as f: pass
    with open(path_mem,'w') as f:
        for tag in set(all_tags):
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0000FFC0)|0x00010000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t" + '\t'.join(data) + '\n')
    print("Testcase 9 created")
def testcase_10(n_set=16):
    base_path="subsystem_testcase/testcase_10/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,random.randint(1,3))
    remaining_tags=list(set(available_tags)-set(selected_tags)); extra_tag=random.choice(remaining_tags)
    all_tags=selected_tags+[extra_tag]
    with open(path_1,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0000FFFF)|0x00010000; f.write(f"read\t0x{addr:08x}\n")
        word_offset=random.randint(0,15)
        addr=(extra_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        addr=(addr&0x0000FFFF)|0x00010000; f.write(f"read\t0x{addr:08x}")
    with open(path_0,'w') as f: pass
    with open(path_mem,'w') as f:
        for tag in all_tags:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0000FFC0)|0x00010000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t" + '\t'.join(data) + '\n')
    print("Testcase 10 created")
def testcase_11(n_set=16):
    base_path="subsystem_testcase/testcase_11/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,4)
    remaining_tags=list(set(available_tags)-set(selected_tags)); extra_tag=random.choice(remaining_tags)
    all_tags=selected_tags+[extra_tag]
    with open(path_1,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0000FFFF)|0x00010000; f.write(f"read\t0x{addr:08x}\n")
        word_offset=random.randint(0,15)
        addr=(extra_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        addr=(addr&0x0000FFFF)|0x00010000; f.write(f"read\t0x{addr:08x}")
    with open(path_0,'w') as f: pass
    with open(path_mem,'w') as f:
        for tag in all_tags:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0000FFC0)|0x00010000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t" + '\t'.join(data) + '\n')
    print("Testcase 11 created")
def testcase_12(n_set=16):
    base_path="subsystem_testcase/testcase_12/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,4)
    remaining_tags=list(set(available_tags)-set(selected_tags)); extra_tag=random.choice(remaining_tags)
    all_tags=selected_tags+[extra_tag]
    with open(path_1,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0000FFFF)|0x00010000
            data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{addr:08x}\t{data}\n")
        word_offset=random.randint(0,15)
        addr=(extra_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        addr=(addr&0x0000FFFF)|0x00010000; f.write(f"read\t0x{addr:08x}")
    with open(path_0,'w') as f: pass
    with open(path_mem,'w') as f:
        for tag in all_tags:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0000FFC0)|0x00010000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t" + '\t'.join(data) + '\n')
    print("Testcase 12 created")
def testcase_13(n_set=16):
    base_path="subsystem_testcase/testcase_13/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,random.randint(1,4))
    chosen_tag=random.choice(selected_tags); all_tags=selected_tags+[chosen_tag]
    with open(path_1,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0000FFFF)|0x00010000; f.write(f"read\t0x{addr:08x}\n")
        word_offset=random.randint(0,15)
        addr=(chosen_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        addr=(addr&0x0000FFFF)|0x00010000
        data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{addr:08x}\t{data}")
    with open(path_0,'w') as f: pass
    with open(path_mem,'w') as f:
        for tag in set(all_tags):
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0000FFC0)|0x00010000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t" + '\t'.join(data) + '\n')
    print("Testcase 13 created")
def testcase_14(n_set=16):
    base_path="subsystem_testcase/testcase_14/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,random.randint(1,3))
    remaining_tags=list(set(available_tags)-set(selected_tags)); write_tag=random.choice(remaining_tags)
    all_tags=selected_tags+[write_tag]
    with open(path_1,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0000FFFF)|0x00010000; f.write(f"read\t0x{addr:08x}\n")
        word_offset=random.randint(0,15)
        addr=(write_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        addr=(addr&0x0000FFFF)|0x00010000
        data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{addr:08x}\t{data}")
    with open(path_0,'w') as f: pass
    with open(path_mem,'w') as f:
        for tag in all_tags:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0000FFC0)|0x00010000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t" + '\t'.join(data) + '\n')
    print("Testcase 14 created")
def testcase_15(n_set=16):
    base_path="subsystem_testcase/testcase_15/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,4)
    remaining_tags=list(set(available_tags)-set(selected_tags)); write_tag=random.choice(remaining_tags)
    all_tags=selected_tags+[write_tag]
    with open(path_1,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0000FFFF)|0x00010000; f.write(f"read\t0x{addr:08x}\n")
        word_offset=random.randint(0,15)
        addr=(write_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        addr=(addr&0x0000FFFF)|0x00010000
        data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{addr:08x}\t{data}")
    with open(path_0,'w') as f: pass
    with open(path_mem,'w') as f:
        for tag in all_tags:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0000FFC0)|0x00010000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t" + '\t'.join(data) + '\n')
    print("Testcase 15 created")
def testcase_16(n_set=16):
    base_path="subsystem_testcase/testcase_16/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,4)
    remaining_tags=list(set(available_tags)-set(selected_tags)); extra_tag=random.choice(remaining_tags)
    all_tags=selected_tags+[extra_tag]
    with open(path_1,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0000FFFF)|0x00010000
            data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{addr:08x}\t{data}\n")
        word_offset=random.randint(0,15)
        addr=(extra_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        addr=(addr&0x0000FFFF)|0x00010000
        data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{addr:08x}\t{data}")
    with open(path_0,'w') as f: pass
    with open(path_mem,'w') as f:
        for tag in all_tags:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0000FFC0)|0x00010000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t" + '\t'.join(data) + '\n')
    print("Testcase 16 created")
def testcase_17(n_set=16):
    base_path="subsystem_testcase/testcase_17/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,random.randint(1,4))
    chosen_tag=random.choice(selected_tags); all_tags=selected_tags+[chosen_tag]
    with open(path_0,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0000FFFF)|0x00020000; f.write(f"read\t0x{addr:08x}\n")
        word_offset=random.randint(0,15)
        addr=(chosen_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        addr=(addr&0x0000FFFF)|0x00020000; f.write(f"read\t0x{addr:08x}")
    with open(path_1,'w') as f: pass
    with open(path_mem,'w') as f:
        for tag in set(all_tags):
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0000FFC0)|0x00020000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t" + '\t'.join(data) + '\n')
    print("Testcase 17 created")
def testcase_18(n_set=16):
    base_path="subsystem_testcase/testcase_18/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,random.randint(1,3))
    remaining_tags=list(set(available_tags)-set(selected_tags)); extra_tag=random.choice(remaining_tags)
    all_tags=selected_tags+[extra_tag]
    with open(path_0,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0000FFFF)|0x00020000; f.write(f"read\t0x{addr:08x}\n")
        word_offset=random.randint(0,15)
        addr=(extra_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        addr=(addr&0x0000FFFF)|0x00020000; f.write(f"read\t0x{addr:08x}")
    with open(path_1,'w') as f: pass
    with open(path_mem,'w') as f:
        for tag in all_tags:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0000FFC0)|0x00020000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t" + '\t'.join(data) + '\n')
    print("Testcase 18 created")
def testcase_19(n_set=16):
    base_path="subsystem_testcase/testcase_19/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,4)
    remaining_tags=list(set(available_tags)-set(selected_tags)); extra_tag=random.choice(remaining_tags)
    all_tags=selected_tags+[extra_tag]
    with open(path_0,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0000FFFF)|0x00020000; f.write(f"read\t0x{addr:08x}\n")
        word_offset=random.randint(0,15)
        addr=(extra_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        addr=(addr&0x0000FFFF)|0x00020000; f.write(f"read\t0x{addr:08x}")
    with open(path_1,'w') as f: pass
    with open(path_mem,'w') as f:
        for tag in all_tags:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0000FFC0)|0x00020000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t" + '\t'.join(data) + '\n')
    print("Testcase 19 created")
def testcase_20(n_set=16):
    base_path="subsystem_testcase/testcase_20/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,4)
    remaining_tags=list(set(available_tags)-set(selected_tags)); extra_tag=random.choice(remaining_tags)
    all_tags=selected_tags+[extra_tag]
    with open(path_0,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0000FFFF)|0x00020000
            data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{addr:08x}\t{data}\n")
        word_offset=random.randint(0,15)
        addr=(extra_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        addr=(addr&0x0000FFFF)|0x00020000; f.write(f"read\t0x{addr:08x}")
    with open(path_1,'w') as f: pass
    with open(path_mem,'w') as f:
        for tag in all_tags:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0000FFC0)|0x00020000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t" + '\t'.join(data) + '\n')
    print("Testcase 20 created")
def testcase_21(n_set=16):
    base_path="subsystem_testcase/testcase_21/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,random.randint(1,3))
    remaining_tags=list(set(available_tags)-set(selected_tags)); extra_tag=random.choice(remaining_tags)
    all_tags=selected_tags+[extra_tag]
    with open(path_0,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0000FFFF)|0x00020000; f.write(f"read\t0x{addr:08x}\n")
        word_offset=random.randint(0,15)
        addr=(extra_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        addr=(addr&0x0000FFFF)|0x00020000; f.write(f"read\t0x{addr:08x}")
    with open(path_1,'w') as f:
        word_offset=random.randint(0,15)
        addr=(extra_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        addr=(addr&0x0000FFFF)|0x00020000; f.write(f"read\t0x{addr:08x}")
    with open(path_mem,'w') as f:
        for tag in all_tags:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0000FFC0)|0x00020000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t" + '\t'.join(data) + '\n')
    print("Testcase 21 created")
def testcase_22(n_set=16):
    base_path="subsystem_testcase/testcase_22/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,4)
    remaining_tags=list(set(available_tags)-set(selected_tags)); extra_tag=random.choice(remaining_tags)
    all_tags=selected_tags+[extra_tag]
    with open(path_0,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0000FFFF)|0x00020000; f.write(f"read\t0x{addr:08x}\n")
        word_offset=random.randint(0,15)
        last_addr=(extra_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        last_addr=(last_addr&0x0000FFFF)|0x00020000; f.write(f"read\t0x{last_addr:08x}")
    with open(path_1,'w') as f:
        word_offset=random.randint(0,15)
        mirror_addr=(extra_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        mirror_addr=(mirror_addr&0x0000FFFF)|0x00020000; f.write(f"read\t0x{mirror_addr:08x}")
    with open(path_mem,'w') as f:
        for tag in all_tags:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0000FFC0)|0x00020000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t" + '\t'.join(data) + '\n')
    print("Testcase 22 created")
def testcase_23(n_set=16):
    base_path="subsystem_testcase/testcase_23/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,4)
    remaining_tags=list(set(available_tags)-set(selected_tags)); extra_tag=random.choice(remaining_tags)
    all_tags=selected_tags+[extra_tag]
    with open(path_0,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0000FFFF)|0x00020000
            data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{addr:08x}\t{data}\n")
        word_offset=random.randint(0,15)
        last_addr=(extra_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        last_addr=(last_addr&0x0000FFFF)|0x00020000; f.write(f"read\t0x{last_addr:08x}")
    with open(path_1,'w') as f:
        word_offset=random.randint(0,15)
        mirror_addr=(extra_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        mirror_addr=(mirror_addr&0x0000FFFF)|0x00020000; f.write(f"read\t0x{mirror_addr:08x}")
    with open(path_mem,'w') as f:
        for tag in all_tags:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0000FFC0)|0x00020000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t" + '\t'.join(data) + '\n')
    print("Testcase 23 created")
def testcase_24(n_set=16):
    base_path="subsystem_testcase/testcase_24/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,random.randint(1,4))
    chosen_tag=random.choice(selected_tags); all_tags=selected_tags+[chosen_tag]
    with open(path_1,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0000FFFF)|0x00020000; f.write(f"read\t0x{addr:08x}\n")
        word_offset=random.randint(0,15)
        addr=(chosen_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        addr=(addr&0x0000FFFF)|0x00020000; f.write(f"read\t0x{addr:08x}")
    with open(path_0,'w') as f: pass
    with open(path_mem,'w') as f:
        for tag in set(all_tags):
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0000FFC0)|0x00020000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t" + '\t'.join(data) + '\n')
    print("Testcase 24 created")
def testcase_25(n_set=16):
    base_path="subsystem_testcase/testcase_25/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,random.randint(1,3))
    remaining_tags=list(set(available_tags)-set(selected_tags)); extra_tag=random.choice(remaining_tags)
    all_tags=selected_tags+[extra_tag]
    with open(path_1,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0000FFFF)|0x00020000; f.write(f"read\t0x{addr:08x}\n")
        word_offset=random.randint(0,15)
        addr=(extra_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        addr=(addr&0x0000FFFF)|0x00020000; f.write(f"read\t0x{addr:08x}")
    with open(path_0,'w') as f: pass
    with open(path_mem,'w') as f:
        for tag in all_tags:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0000FFC0)|0x00020000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t" + '\t'.join(data) + '\n')
    print("Testcase 25 created")
def testcase_26(n_set=16):
    base_path="subsystem_testcase/testcase_26/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,4)
    remaining_tags=list(set(available_tags)-set(selected_tags)); extra_tag=random.choice(remaining_tags)
    all_tags=selected_tags+[extra_tag]
    with open(path_1,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0000FFFF)|0x00020000; f.write(f"read\t0x{addr:08x}\n")
        word_offset=random.randint(0,15)
        addr=(extra_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        addr=(addr&0x0000FFFF)|0x00020000; f.write(f"read\t0x{addr:08x}")
    with open(path_0,'w') as f: pass
    with open(path_mem,'w') as f:
        for tag in all_tags:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0000FFC0)|0x00020000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t" + '\t'.join(data) + '\n')
    print("Testcase 26 created")
def testcase_27(n_set=16):
    base_path="subsystem_testcase/testcase_27/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,4)
    remaining_tags=list(set(available_tags)-set(selected_tags)); extra_tag=random.choice(remaining_tags)
    all_tags=selected_tags+[extra_tag]
    with open(path_1,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0000FFFF)|0x00020000
            data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{addr:08x}\t{data}\n")
        word_offset=random.randint(0,15)
        addr=(extra_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        addr=(addr&0x0000FFFF)|0x00020000; f.write(f"read\t0x{addr:08x}")
    with open(path_0,'w') as f: pass
    with open(path_mem,'w') as f:
        for tag in all_tags:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0000FFC0)|0x00020000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t" + '\t'.join(data) + '\n')
    print("Testcase 27 created")
def testcase_28(n_set=16):
    base_path="subsystem_testcase/testcase_28/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,random.randint(1,3))
    remaining_tags=list(set(available_tags)-set(selected_tags)); extra_tag=random.choice(remaining_tags)
    all_tags=selected_tags+[extra_tag]
    with open(path_1,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0000FFFF)|0x00020000; f.write(f"read\t0x{addr:08x}\n")
        word_offset=random.randint(0,15)
        addr=(extra_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        addr=(addr&0x0000FFFF)|0x00020000; f.write(f"read\t0x{addr:08x}")
    with open(path_0,'w') as f:
        word_offset=random.randint(0,15)
        addr=(extra_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        addr=(addr&0x0000FFFF)|0x00020000; f.write(f"read\t0x{addr:08x}")
    with open(path_mem,'w') as f:
        for tag in all_tags:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0000FFC0)|0x00020000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t" + '\t'.join(data) + '\n')
    print("Testcase 28 created")
def testcase_29(n_set=16):
    base_path="subsystem_testcase/testcase_29/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,4)
    remaining_tags=list(set(available_tags)-set(selected_tags)); extra_tag=random.choice(remaining_tags)
    all_tags=selected_tags+[extra_tag]
    with open(path_1,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0000FFFF)|0x00020000; f.write(f"read\t0x{addr:08x}\n")
        word_offset=random.randint(0,15)
        last_addr=(extra_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        last_addr=(last_addr&0x0000FFFF)|0x00020000; f.write(f"read\t0x{last_addr:08x}")
    with open(path_0,'w') as f:
        word_offset=random.randint(0,15)
        mirror_addr=(extra_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        mirror_addr=(mirror_addr&0x0000FFFF)|0x00020000; f.write(f"read\t0x{mirror_addr:08x}")
    with open(path_mem,'w') as f:
        for tag in all_tags:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0000FFC0)|0x00020000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t" + '\t'.join(data) + '\n')
    print("Testcase 29 created")
def testcase_30(n_set=16):
    base_path="subsystem_testcase/testcase_30/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,4)
    remaining_tags=list(set(available_tags)-set(selected_tags)); extra_tag=random.choice(remaining_tags)
    all_tags=selected_tags+[extra_tag]
    with open(path_1,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0000FFFF)|0x00020000
            data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{addr:08x}\t{data}\n")
        word_offset=random.randint(0,15)
        last_addr=(extra_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        last_addr=(last_addr&0x0000FFFF)|0x00020000; f.write(f"read\t0x{last_addr:08x}")
    with open(path_0,'w') as f:
        word_offset=random.randint(0,15)
        mirror_addr=(extra_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        mirror_addr=(mirror_addr&0x0000FFFF)|0x00020000; f.write(f"read\t0x{mirror_addr:08x}")
    with open(path_mem,'w') as f:
        for tag in all_tags:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0000FFC0)|0x00020000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t" + '\t'.join(data) + '\n')
    print("Testcase 30 created")
def testcase_31(n_set=16):
    base_path="subsystem_testcase/testcase_31/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,random.randint(1,4))
    chosen_tag=random.choice(selected_tags); all_tags=set(selected_tags)
    with open(path_0,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0000FFFF)|0x00020000; f.write(f"read\t0x{addr:08x}\n")
        word_offset=random.randint(0,15)
        addr=(chosen_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        addr=(addr&0x0000FFFF)|0x00020000
        data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{addr:08x}\t{data}"); all_tags.add(chosen_tag)
    with open(path_1,'w') as f: pass
    with open(path_mem,'w') as f:
        for tag in all_tags:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0000FFC0)|0x00020000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t" + '\t'.join(data) + '\n')
    print("Testcase 31 created")
def testcase_32(n_set=16):
    base_path="subsystem_testcase/testcase_32/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,random.randint(1,3))
    remaining_tags=list(set(available_tags)-set(selected_tags)); write_tag=random.choice(remaining_tags)
    all_tags=selected_tags+[write_tag]
    with open(path_0,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0000FFFF)|0x00020000; f.write(f"read\t0x{addr:08x}\n")
        word_offset=random.randint(0,15)
        addr=(write_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        addr=(addr&0x0000FFFF)|0x00020000
        data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{addr:08x}\t{data}")
    with open(path_1,'w') as f: pass
    with open(path_mem,'w') as f:
        for tag in all_tags:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0000FFC0)|0x00020000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t" + '\t'.join(data) + '\n')
    print("Testcase 32 created")
def testcase_33(n_set=16):
    base_path="subsystem_testcase/testcase_33/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,4)
    remaining_tags=list(set(available_tags)-set(selected_tags)); write_tag=random.choice(remaining_tags)
    all_tags=selected_tags+[write_tag]
    with open(path_0,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0000FFFF)|0x00020000; f.write(f"read\t0x{addr:08x}\n")
        word_offset=random.randint(0,15)
        addr=(write_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        addr=(addr&0x0000FFFF)|0x00020000
        data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{addr:08x}\t{data}")
    with open(path_1,'w') as f: pass
    with open(path_mem,'w') as f:
        for tag in all_tags:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0000FFC0)|0x00020000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t" + '\t'.join(data) + '\n')
    print("Testcase 33 created")
def testcase_34(n_set=16):
    base_path="subsystem_testcase/testcase_34/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,4)
    remaining_tags=list(set(available_tags)-set(selected_tags)); write_tag=random.choice(remaining_tags)
    all_tags=selected_tags+[write_tag]
    with open(path_0,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0000FFFF)|0x00020000
            data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{addr:08x}\t{data}\n")
        word_offset=random.randint(0,15)
        addr=(write_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        addr=(addr&0x0000FFFF)|0x00020000
        data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{addr:08x}\t{data}")
    with open(path_1,'w') as f: pass
    with open(path_mem,'w') as f:
        for tag in all_tags:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0000FFC0)|0x00020000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t" + '\t'.join(data) + '\n')
    print("Testcase 34 created")
def testcase_35(n_set=16):
    base_path="subsystem_testcase/testcase_35/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,random.randint(1,3))
    remaining_tags=list(set(available_tags)-set(selected_tags)); write_tag=random.choice(remaining_tags)
    all_tags=selected_tags+[write_tag]
    with open(path_0,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0000FFFF)|0x00020000; f.write(f"read\t0x{addr:08x}\n")
        word_offset=random.randint(0,15)
        write_addr=(write_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        write_addr=(write_addr&0x0000FFFF)|0x00020000
        data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{write_addr:08x}\t{data}")
    with open(path_1,'w') as f:
        word_offset=random.randint(0,15)
        mirror_addr=(write_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        mirror_addr=(mirror_addr&0x0000FFFF)|0x00020000; f.write(f"read\t0x{mirror_addr:08x}")
    with open(path_mem,'w') as f:
        for tag in all_tags:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0000FFC0)|0x00020000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t" + '\t'.join(data) + '\n')
    print("Testcase 35 created")
def testcase_36(n_set=16):
    base_path="subsystem_testcase/testcase_36/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,4)
    remaining_tags=list(set(available_tags)-set(selected_tags)); write_tag=random.choice(remaining_tags)
    all_tags=selected_tags+[write_tag]
    with open(path_0,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0000FFFF)|0x00020000; f.write(f"read\t0x{addr:08x}\n")
        word_offset=random.randint(0,15)
        write_addr=(write_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        write_addr=(write_addr&0x0000FFFF)|0x00020000
        data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{write_addr:08x}\t{data}")
    with open(path_1,'w') as f:
        word_offset=random.randint(0,15)
        mirror_addr=(write_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        mirror_addr=(mirror_addr&0x0000FFFF)|0x00020000; f.write(f"read\t0x{mirror_addr:08x}")
    with open(path_mem,'w') as f:
        for tag in all_tags:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0000FFC0)|0x00020000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t" + '\t'.join(data) + '\n')
    print("Testcase 36 created")
def testcase_37(n_set=16):
    base_path="subsystem_testcase/testcase_37/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,4)
    remaining_tags=list(set(available_tags)-set(selected_tags)); write_tag=random.choice(remaining_tags)
    all_tags=selected_tags+[write_tag]
    with open(path_0,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0000FFFF)|0x00020000
            data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{addr:08x}\t{data}\n")
        word_offset=random.randint(0,15)
        write_addr=(write_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        write_addr=(write_addr&0x0000FFFF)|0x00020000
        data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{write_addr:08x}\t{data}")
    with open(path_1,'w') as f:
        word_offset=random.randint(0,15)
        read_addr=(write_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        read_addr=(read_addr&0x0000FFFF)|0x00020000; f.write(f"read\t0x{read_addr:08x}")
    with open(path_mem,'w') as f:
        for tag in all_tags:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0000FFC0)|0x00020000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t" + '\t'.join(data) + '\n')
    print("Testcase 37 created")
def testcase_38(n_set=16):
    base_path="subsystem_testcase/testcase_38/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,random.randint(1,4))
    chosen_tag=random.choice(selected_tags); all_tags=set(selected_tags)
    with open(path_1,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0000FFFF)|0x00020000; f.write(f"read\t0x{addr:08x}\n")
        word_offset=random.randint(0,15)
        addr=(chosen_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        addr=(addr&0x0000FFFF)|0x00020000
        data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{addr:08x}\t{data}"); all_tags.add(chosen_tag)
    with open(path_0,'w') as f: pass
    with open(path_mem,'w') as f:
        for tag in all_tags:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0000FFC0)|0x00020000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t" + '\t'.join(data) + '\n')
    print("Testcase 38 created")
def testcase_39(n_set=16):
    base_path="subsystem_testcase/testcase_39/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,random.randint(1,3))
    remaining_tags=list(set(available_tags)-set(selected_tags)); write_tag=random.choice(remaining_tags)
    all_tags=selected_tags+[write_tag]
    with open(path_1,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0000FFFF)|0x00020000; f.write(f"read\t0x{addr:08x}\n")
        word_offset=random.randint(0,15)
        addr=(write_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        addr=(addr&0x0000FFFF)|0x00020000
        data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{addr:08x}\t{data}")
    with open(path_0,'w') as f: pass
    with open(path_mem,'w') as f:
        for tag in all_tags:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0000FFC0)|0x00020000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t" + '\t'.join(data) + '\n')
    print("Testcase 39 created")
def testcase_40(n_set=16):
    base_path="subsystem_testcase/testcase_40/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,4)
    remaining_tags=list(set(available_tags)-set(selected_tags)); write_tag=random.choice(remaining_tags)
    all_tags=selected_tags+[write_tag]
    with open(path_1,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0000FFFF)|0x00020000; f.write(f"read\t0x{addr:08x}\n")
        word_offset=random.randint(0,15)
        addr=(write_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        addr=(addr&0x0000FFFF)|0x00020000
        data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{addr:08x}\t{data}")
    with open(path_0,'w') as f: pass
    with open(path_mem,'w') as f:
        for tag in all_tags:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0000FFC0)|0x00020000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t" + '\t'.join(data) + '\n')
    print("Testcase 40 created")
def testcase_41(n_set=16):
    base_path="subsystem_testcase/testcase_41/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,4)
    remaining_tags=list(set(available_tags)-set(selected_tags)); write_tag=random.choice(remaining_tags)
    all_tags=selected_tags+[write_tag]
    with open(path_1,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0000FFFF)|0x00020000
            data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{addr:08x}\t{data}\n")
        word_offset=random.randint(0,15)
        addr=(write_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        addr=(addr&0x0000FFFF)|0x00020000
        data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{addr:08x}\t{data}")
    with open(path_0,'w') as f: pass
    with open(path_mem,'w') as f:
        for tag in all_tags:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0000FFC0)|0x00020000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t" + '\t'.join(data) + '\n')
    print("Testcase 41 created")
def testcase_42(n_set=16):
    base_path="subsystem_testcase/testcase_42/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,random.randint(1,3))
    remaining_tags=list(set(available_tags)-set(selected_tags)); write_tag=random.choice(remaining_tags)
    all_tags=selected_tags+[write_tag]
    with open(path_1,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0000FFFF)|0x00020000; f.write(f"read\t0x{addr:08x}\n")
        word_offset=random.randint(0,15)
        write_addr=(write_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        write_addr=(write_addr&0x0000FFFF)|0x00020000
        data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{write_addr:08x}\t{data}")
    with open(path_0,'w') as f:
        word_offset=random.randint(0,15)
        mirror_addr=(write_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        mirror_addr=(mirror_addr&0x0000FFFF)|0x00020000; f.write(f"read\t0x{mirror_addr:08x}")
    with open(path_mem,'w') as f:
        for tag in all_tags:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0000FFC0)|0x00020000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t" + '\t'.join(data) + '\n')
    print("Testcase 42 created")
def testcase_43(n_set=16):
    base_path="subsystem_testcase/testcase_43/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,4)
    remaining_tags=list(set(available_tags)-set(selected_tags)); write_tag=random.choice(remaining_tags)
    all_tags=selected_tags+[write_tag]
    with open(path_1,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0000FFFF)|0x00020000; f.write(f"read\t0x{addr:08x}\n")
        word_offset=random.randint(0,15)
        write_addr=(write_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        write_addr=(write_addr&0x0000FFFF)|0x00020000
        data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{write_addr:08x}\t{data}")
    with open(path_0,'w') as f:
        word_offset=random.randint(0,15)
        mirror_addr=(write_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        mirror_addr=(mirror_addr&0x0000FFFF)|0x00020000; f.write(f"read\t0x{mirror_addr:08x}")
    with open(path_mem,'w') as f:
        for tag in all_tags:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0000FFC0)|0x00020000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t" + '\t'.join(data) + '\n')
    print("Testcase 43 created")
def testcase_44(n_set=16):
    base_path="subsystem_testcase/testcase_44/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,4)
    remaining_tags=list(set(available_tags)-set(selected_tags)); write_tag=random.choice(remaining_tags)
    all_tags=selected_tags+[write_tag]
    with open(path_1,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0000FFFF)|0x00020000
            data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{addr:08x}\t{data}\n")
        word_offset=random.randint(0,15)
        write_addr=(write_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        write_addr=(write_addr&0x0000FFFF)|0x00020000
        data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{write_addr:08x}\t{data}")
    with open(path_0,'w') as f:
        word_offset=random.randint(0,15)
        read_addr=(write_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        read_addr=(read_addr&0x0000FFFF)|0x00020000; f.write(f"read\t0x{read_addr:08x}")
    with open(path_mem,'w') as f:
        for tag in all_tags:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0000FFC0)|0x00020000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t" + '\t'.join(data) + '\n')
    print("Testcase 44 created")
def testcase_45(n_set=16):
    base_path="subsystem_testcase/testcase_45/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,random.randint(1,4))
    mirror_tag=random.choice(selected_tags); all_tags=selected_tags.copy()
    with open(path_0,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0001FFFF)|0x00020000; f.write(f"read\t0x{addr:08x}\n")
        read_word_offset=random.randint(0,15)
        read_addr=(mirror_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(read_word_offset<<2)
        read_addr=(read_addr&0x0001FFFF)|0x00020000; f.write(f"read\t0x{read_addr:08x}\n")
        write_word_offset=random.randint(0,15)
        write_addr=(mirror_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(write_word_offset<<2)
        write_addr=(write_addr&0x0001FFFF)|0x00020000
        data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{write_addr:08x}\t{data}")
    with open(path_1,'w') as f: pass
    with open(path_mem,'w') as f:
        for tag in list(set(all_tags+[mirror_tag])):
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0001FFC0)|0x00020000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t"+'\t'.join(data)+'\n')
    print("Testcase 45 created")
def testcase_46(n_set=16):
    base_path="subsystem_testcase/testcase_46/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); num_reads=random.randint(1,3)
    selected_tags=random.sample(available_tags,num_reads)
    remaining_tags=list(set(available_tags)-set(selected_tags)); new_tag=random.choice(remaining_tags)
    with open(path_0,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0001FFFF)|0x00020000; f.write(f"read\t0x{addr:08x}\n")
        word_offset=random.randint(0,15)
        read_addr=(new_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        read_addr=(read_addr&0x0001FFFF)|0x00020000; f.write(f"read\t0x{read_addr:08x}\n")
        write_addr=(new_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(random.randint(0,15)<<2)
        write_addr=(write_addr&0x0001FFFF)|0x00020000; data=f"0x{random.randint(0,2**32-1):08x}"
        f.write(f"write\t0x{write_addr:08x}\t{data}")
    with open(path_1,'w') as f: pass
    with open(path_mem,'w') as f:
        for tag in selected_tags+[new_tag]:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0001FFC0)|0x00020000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t"+'\t'.join(data)+'\n')
    print("Testcase 46 created")
def testcase_47(n_set=16):
    base_path="subsystem_testcase/testcase_47/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,4)
    remaining_tags=list(set(available_tags)-set(selected_tags)); new_tag=random.choice(remaining_tags)
    with open(path_0,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0001FFFF)|0x00020000; f.write(f"read\t0x{addr:08x}\n")
        word_offset=random.randint(0,15)
        read_addr=(new_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        read_addr=(read_addr&0x0001FFFF)|0x00020000; f.write(f"read\t0x{read_addr:08x}\n")
        write_addr=(new_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(random.randint(0,15)<<2)
        write_addr=(write_addr&0x0001FFFF)|0x00020000; data=f"0x{random.randint(0,2**32-1):08x}"
        f.write(f"write\t0x{write_addr:08x}\t{data}")
    with open(path_1,'w') as f: pass
    with open(path_mem,'w') as f:
        all_tags=selected_tags+[new_tag]
        for tag in all_tags:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0001FFC0)|0x00020000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t"+'\t'.join(data)+'\n')
    print("Testcase 47 created")
def testcase_48(n_set=16):
    base_path="subsystem_testcase/testcase_48/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,4)
    remaining_tags=list(set(available_tags)-set(selected_tags)); new_tag=random.choice(remaining_tags)
    with open(path_0,'w') as f:
        for tag in selected_tags:  # 4 lệnh write với tag khác nhau
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0001FFFF)|0x00020000
            data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{addr:08x}\t{data}\n")
        word_offset=random.randint(0,15)  # lệnh read với tag mới
        read_addr=(new_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        read_addr=(read_addr&0x0001FFFF)|0x00020000; f.write(f"read\t0x{read_addr:08x}\n")
        word_offset=random.randint(0,15)  # lệnh write trùng tag với read vừa tạo
        write_addr=(new_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        write_addr=(write_addr&0x0001FFFF)|0x00020000
        data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{write_addr:08x}\t{data}")
    with open(path_1,'w') as f: pass
    with open(path_mem,'w') as f:
        for tag in selected_tags+[new_tag]:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0001FFC0)|0x00020000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t"+'\t'.join(data)+'\n')
    print("Testcase 48 created")
def testcase_49(n_set=16):
    base_path="subsystem_testcase/testcase_49/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    num_read=random.randint(1,3); available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,num_read)
    remaining_tags=list(set(available_tags)-set(selected_tags)); new_tag=random.choice(remaining_tags)
    with open(path_0,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0001FFFF)|0x00020000; f.write(f"read\t0x{addr:08x}\n")
        word_offset=random.randint(0,15)
        read_addr=(new_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        read_addr=(read_addr&0x0001FFFF)|0x00020000; f.write(f"read\t0x{read_addr:08x}\n")
        word_offset=random.randint(0,15)
        write_addr=(new_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        write_addr=(write_addr&0x0001FFFF)|0x00020000
        data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{write_addr:08x}\t{data}")
    with open(path_1,'w') as f:
        word_offset=random.randint(0,15)
        addr=(new_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        addr=(addr&0x0001FFFF)|0x00020000; f.write(f"read\t0x{addr:08x}")
    with open(path_mem,'w') as f:
        for tag in selected_tags+[new_tag]:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0001FFC0)|0x00020000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t"+'\t'.join(data)+'\n')
    print("Testcase 49 created")
def testcase_50(n_set=16):
    base_path="subsystem_testcase/testcase_50/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,4)
    remaining_tags=list(set(available_tags)-set(selected_tags)); new_tag=random.choice(remaining_tags)
    with open(path_0,'w') as f:
        for tag in selected_tags:  # 4 read khác tag
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0001FFFF)|0x00020000
            f.write(f"read\t0x{addr:08x}\n")
        word_offset=random.randint(0,15)  # read với tag mới
        read_addr=(new_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        read_addr=(read_addr&0x0001FFFF)|0x00020000; f.write(f"read\t0x{read_addr:08x}\n")
        word_offset=random.randint(0,15)  # write trùng tag với read trên
        write_addr=(new_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        write_addr=(write_addr&0x0001FFFF)|0x00020000
        data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{write_addr:08x}\t{data}")
    with open(path_1,'w') as f:  # inst_1 read trùng tag cuối
        word_offset=random.randint(0,15)
        inst1_addr=(new_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        inst1_addr=(inst1_addr&0x0001FFFF)|0x00020000; f.write(f"read\t0x{inst1_addr:08x}")
    with open(path_mem,'w') as f:
        for tag in selected_tags+[new_tag]:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0001FFC0)|0x00020000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t"+'\t'.join(data)+'\n')
    print("Testcase 50 created")
def testcase_51(n_set=16):
    base_path="subsystem_testcase/testcase_51/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,4)
    remaining_tags=list(set(available_tags)-set(selected_tags)); mid_tag=random.choice(remaining_tags)
    with open(path_0,'w') as f:
        for tag in selected_tags:  # 4 write khác tag
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0001FFFF)|0x00020000
            data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{addr:08x}\t{data}\n")
        word_offset=random.randint(0,15)  # read với tag mới
        read_addr=(mid_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        read_addr=(read_addr&0x0001FFFF)|0x00020000; f.write(f"read\t0x{read_addr:08x}\n")
        word_offset=random.randint(0,15)  # write lại đúng tag của read trên
        write_addr=(mid_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        write_addr=(write_addr&0x0001FFFF)|0x00020000
        data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{write_addr:08x}\t{data}")
    with open(path_1,'w') as f:  # inst_1 đọc lại đúng tag của write cuối
        word_offset=random.randint(0,15)
        inst1_addr=(mid_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        inst1_addr=(inst1_addr&0x0001FFFF)|0x00020000; f.write(f"read\t0x{inst1_addr:08x}")
    with open(path_mem,'w') as f:
        for tag in selected_tags+[mid_tag]:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0001FFC0)|0x00020000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t"+'\t'.join(data)+'\n')
    print("Testcase 51 created")
def testcase_52(n_set=16):
    base_path="subsystem_testcase/testcase_52/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); num_reads=random.randint(1,4)
    selected_tags=random.sample(available_tags,num_reads)
    shared_tag=random.choice(selected_tags)
    with open(path_0,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0001FFFF)|0x00020000; f.write(f"read\t0x{addr:08x}\n")
        word_offset=random.randint(0,15)
        write_addr=(shared_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        write_addr=(write_addr&0x0001FFFF)|0x00020000
        data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{write_addr:08x}\t{data}\n")
        word_offset=random.randint(0,15)
        read_addr2=(shared_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        read_addr2=(read_addr2&0x0001FFFF)|0x00020000; f.write(f"read\t0x{read_addr2:08x}")
    with open(path_1,'w') as f: pass
    with open(path_mem,'w') as f:
        all_tags=set(selected_tags+[shared_tag])
        for tag in all_tags:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0001FFC0)|0x00020000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t"+'\t'.join(data)+'\n')
    print("Testcase 52 created")
def testcase_53(n_set=16):
    base_path="subsystem_testcase/testcase_53/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); num_reads=random.randint(1,3)
    selected_tags=random.sample(available_tags,num_reads)
    remaining_tags=list(set(available_tags)-set(selected_tags)); write_tag=random.choice(remaining_tags)
    with open(path_0,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0001FFFF)|0x00020000; f.write(f"read\t0x{addr:08x}\n")
        word_offset=random.randint(0,15)
        write_addr=(write_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        write_addr=(write_addr&0x0001FFFF)|0x00020000
        data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{write_addr:08x}\t{data}\n")
        word_offset=random.randint(0,15)
        read_addr2=(write_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        read_addr2=(read_addr2&0x0001FFFF)|0x00020000; f.write(f"read\t0x{read_addr2:08x}")
    with open(path_1,'w') as f: pass
    with open(path_mem,'w') as f:
        all_tags=set(selected_tags+[write_tag])
        for tag in all_tags:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0001FFC0)|0x00020000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t"+'\t'.join(data)+'\n')
    print("Testcase 53 created")
def testcase_54(n_set=16):
    base_path = "subsystem_testcase/testcase_54/"; os.makedirs(base_path, exist_ok=True)
    path_0 = os.path.join(base_path, "instr_mem_A.mem"); path_1 = os.path.join(base_path, "instr_mem_B.mem"); path_mem = os.path.join(base_path, "main_memory_init.mem")
    tag_bits = 32 - (n_set.bit_length() + 4 + 2); set_index = random.randint(0, n_set - 1)
    available_tags = list(range(1 << tag_bits)); selected_tags = random.sample(available_tags, 4)
    remaining_tags = list(set(available_tags) - set(selected_tags)); write_tag = random.choice(remaining_tags)
    all_tags = selected_tags + [write_tag]
    with open(path_0, 'w') as f:
        for tag in selected_tags:  # 4 read cùng set khác tag
            word_offset = random.randint(0, 15)
            addr = (tag << (n_set.bit_length() + 4 + 2)) | (set_index << 6) | (word_offset << 2)
            addr = (addr & 0x0001FFFF) | 0x00020000; f.write(f"read\t0x{addr:08x}\n")
        word_offset = random.randint(0, 15)  # write cùng set, tag khác
        write_addr = (write_tag << (n_set.bit_length() + 4 + 2)) | (set_index << 6) | (word_offset << 2)
        write_addr = (write_addr & 0x0001FFFF) | 0x00020000
        data = f"0x{random.randint(0, 2 ** 32 - 1):08x}"; f.write(f"write\t0x{write_addr:08x}\t{data}\n")
        read_offset = random.randint(0, 15)  # read lại đúng tag của lệnh write
        read_addr = (write_tag << (n_set.bit_length() + 4 + 2)) | (set_index << 6) | (read_offset << 2)
        read_addr = (read_addr & 0x0001FFFF) | 0x00020000; f.write(f"read\t0x{read_addr:08x}")
    with open(path_1, 'w') as f: pass
    with open(path_mem, 'w') as f:
        for tag in all_tags:
            block_addr = (tag << (n_set.bit_length() + 4 + 2)) | (set_index << 6)
            block_addr = (block_addr & 0x0001FFC0) | 0x00020000
            data = [f"0x{random.randint(0, 2**32 - 1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t" + '\t'.join(data) + '\n')
    print("Testcase 54 created")
def testcase_55(n_set=16):
    base_path="subsystem_testcase/testcase_55/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(n_set.bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,4)
    remaining_tags=list(set(available_tags)-set(selected_tags)); write_tag=random.choice(remaining_tags); all_tags=selected_tags+[write_tag]
    def shared(addr): return (addr&0x0003FFFF)|0x00020000
    with open(path_0,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15); addr=(tag<<(n_set.bit_length()+4+2))|(set_index<<6)|(word_offset<<2); addr=shared(addr)
            data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{addr:08x}\t{data}\n")
        word_offset=random.randint(0,15); write_addr=(write_tag<<(n_set.bit_length()+4+2))|(set_index<<6)|(word_offset<<2); write_addr=shared(write_addr)
        data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{write_addr:08x}\t{data}\n")
        read_offset=random.randint(0,15); read_addr=(write_tag<<(n_set.bit_length()+4+2))|(set_index<<6)|(read_offset<<2); read_addr=shared(read_addr)
        f.write(f"read\t0x{read_addr:08x}")
    with open(path_1,'w') as f: pass
    with open(path_mem,'w') as f:
        for tag in all_tags:
            block_addr=(tag<<(n_set.bit_length()+4+2))|(set_index<<6); block_addr=shared(block_addr&0xFFFFFFC0)
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t"+'\t'.join(data)+'\n')
    print("Testcase 55 created")
def testcase_56(n_set=16):
    base_path="subsystem_testcase/testcase_56/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(n_set.bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); num_read=random.randint(1,3); selected_tags=random.sample(available_tags,num_read)
    remaining_tags=list(set(available_tags)-set(selected_tags)); write_tag=random.choice(remaining_tags)
    def shared(addr): return (addr&0x0003FFFF)|0x00020000
    addr_list=[]  # thu thập địa chỉ cần tạo mem
    with open(path_0,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15); addr=(tag<<(n_set.bit_length()+4+2))|(set_index<<6)|(word_offset<<2); addr=shared(addr)
            f.write(f"read\t0x{addr:08x}\n"); addr_list.append(addr)
        word_offset=random.randint(0,15); write_addr=(write_tag<<(n_set.bit_length()+4+2))|(set_index<<6)|(word_offset<<2); write_addr=shared(write_addr)
        data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{write_addr:08x}\t{data}\n"); addr_list.append(write_addr)
        read_offset=random.randint(0,15); read_addr=(write_tag<<(n_set.bit_length()+4+2))|(set_index<<6)|(read_offset<<2); read_addr=shared(read_addr)
        f.write(f"read\t0x{read_addr:08x}"); addr_list.append(read_addr)
    with open(path_1,'w') as f:
        ref_offset=random.randint(0,15); ref_addr=(write_tag<<(n_set.bit_length()+4+2))|(set_index<<6)|(ref_offset<<2); ref_addr=shared(ref_addr)
        f.write(f"read\t0x{ref_addr:08x}"); addr_list.append(ref_addr)
    with open(path_mem,'w') as f:
        blocks=set([(addr>>6)<<6 for addr in addr_list])
        for block_addr in blocks:
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t"+'\t'.join(data)+'\n')
    print("Testcase 56 created")
def testcase_57(n_set=16):
    base_path="subsystem_testcase/testcase_57/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(n_set.bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=set(range(1<<tag_bits)); selected_tags=random.sample(list(available_tags),4)
    remaining_tags=list(available_tags-set(selected_tags)); write_tag=random.choice(remaining_tags)
    all_tags=selected_tags+[write_tag]; used_blocks=set()
    with open(path_0,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15); addr=(tag<<(4+n_set.bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0000FFFF)|0x00020000; f.write(f"read\t0x{addr:08x}\n")
        word_offset=random.randint(0,15); write_addr=(write_tag<<(4+n_set.bit_length()+2))|(set_index<<6)|(word_offset<<2)
        write_addr=(write_addr&0x0000FFFF)|0x00020000; data=f"0x{random.randint(0,2**32-1):08x}"
        f.write(f"write\t0x{write_addr:08x}\t{data}\n")
        word_offset=random.randint(0,15); read_back=(write_tag<<(4+n_set.bit_length()+2))|(set_index<<6)|(word_offset<<2)
        read_back=(read_back&0x0000FFFF)|0x00020000; f.write(f"read\t0x{read_back:08x}")
    with open(path_1,'w') as f:
        word_offset=random.randint(0,15); addr=(write_tag<<(4+n_set.bit_length()+2))|(set_index<<6)|(word_offset<<2)
        addr=(addr&0x0000FFFF)|0x00020000; f.write(f"read\t0x{addr:08x}")
    with open(path_mem,'w') as f:
        for tag in all_tags:
            block_addr=(tag<<(4+n_set.bit_length()+2))|(set_index<<6); block_addr=(block_addr&0x0000FFC0)|0x00020000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t"+'\t'.join(data)+'\n')
    print("Testcase 57 created")
def testcase_58(n_set=16):
    base_path="subsystem_testcase/testcase_58/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(n_set.bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=set(range(1<<tag_bits)); selected_tags=random.sample(list(available_tags),4)
    remaining_tags=list(available_tags-set(selected_tags)); write_tag=random.choice(remaining_tags)
    all_tags=selected_tags+[write_tag]
    with open(path_0,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+n_set.bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0000FFFF)|0x00020000
            data=f"0x{random.randint(0,2**32-1):08x}"
            f.write(f"write\t0x{addr:08x}\t{data}\n")
        word_offset=random.randint(0,15)
        write_addr=(write_tag<<(4+n_set.bit_length()+2))|(set_index<<6)|(word_offset<<2); write_addr=(write_addr&0x0000FFFF)|0x00020000
        data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{write_addr:08x}\t{data}\n")
        word_offset=random.randint(0,15)
        read_addr=(write_tag<<(4+n_set.bit_length()+2))|(set_index<<6)|(word_offset<<2); read_addr=(read_addr&0x0000FFFF)|0x00020000
        f.write(f"read\t0x{read_addr:08x}")
    with open(path_1,'w') as f:
        word_offset=random.randint(0,15)
        addr=(write_tag<<(4+n_set.bit_length()+2))|(set_index<<6)|(word_offset<<2); addr=(addr&0x0000FFFF)|0x00020000
        f.write(f"read\t0x{addr:08x}")
    written_blocks=set()
    with open(path_mem,'w') as f:
        for tag in all_tags:
            block_addr=(tag<<(4+n_set.bit_length()+2))|(set_index<<6); block_addr=(block_addr&0x0000FFC0)|0x00020000
            if block_addr in written_blocks: continue
            written_blocks.add(block_addr)
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t"+'\t'.join(data)+'\n')
    print("Testcase 58 created")
def testcase_59(n_set=16):
    base_path="subsystem_testcase/testcase_59/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,random.randint(1,4))
    mirror_tag=random.choice(selected_tags); all_tags=selected_tags.copy()
    with open(path_1,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0001FFFF)|0x00020000; f.write(f"read\t0x{addr:08x}\n")
        read_word_offset=random.randint(0,15)
        read_addr=(mirror_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(read_word_offset<<2)
        read_addr=(read_addr&0x0001FFFF)|0x00020000; f.write(f"read\t0x{read_addr:08x}\n")
        write_word_offset=random.randint(0,15)
        write_addr=(mirror_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(write_word_offset<<2)
        write_addr=(write_addr&0x0001FFFF)|0x00020000
        data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{write_addr:08x}\t{data}")
    with open(path_0,'w') as f: pass
    with open(path_mem,'w') as f:
        for tag in list(set(all_tags+[mirror_tag])):
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0001FFC0)|0x00020000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t"+'\t'.join(data)+'\n')
    print("Testcase 59 created")
def testcase_60(n_set=16):
    base_path="subsystem_testcase/testcase_60/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); num_reads=random.randint(1,3)
    selected_tags=random.sample(available_tags,num_reads)
    remaining_tags=list(set(available_tags)-set(selected_tags)); new_tag=random.choice(remaining_tags)
    with open(path_1,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0001FFFF)|0x00020000; f.write(f"read\t0x{addr:08x}\n")
        word_offset=random.randint(0,15)
        read_addr=(new_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        read_addr=(read_addr&0x0001FFFF)|0x00020000; f.write(f"read\t0x{read_addr:08x}\n")
        write_addr=(new_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(random.randint(0,15)<<2)
        write_addr=(write_addr&0x0001FFFF)|0x00020000; data=f"0x{random.randint(0,2**32-1):08x}"
        f.write(f"write\t0x{write_addr:08x}\t{data}")
    with open(path_0,'w') as f: pass
    with open(path_mem,'w') as f:
        for tag in selected_tags+[new_tag]:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0001FFC0)|0x00020000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t"+'\t'.join(data)+'\n')
    print("Testcase 60 created")
def testcase_61(n_set=16):
    base_path="subsystem_testcase/testcase_61/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,4)
    remaining_tags=list(set(available_tags)-set(selected_tags)); new_tag=random.choice(remaining_tags)
    with open(path_1,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0001FFFF)|0x00020000; f.write(f"read\t0x{addr:08x}\n")
        word_offset=random.randint(0,15)
        read_addr=(new_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        read_addr=(read_addr&0x0001FFFF)|0x00020000; f.write(f"read\t0x{read_addr:08x}\n")
        write_addr=(new_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(random.randint(0,15)<<2)
        write_addr=(write_addr&0x0001FFFF)|0x00020000; data=f"0x{random.randint(0,2**32-1):08x}"
        f.write(f"write\t0x{write_addr:08x}\t{data}")
    with open(path_0,'w') as f: pass
    with open(path_mem,'w') as f:
        all_tags=selected_tags+[new_tag]
        for tag in all_tags:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0001FFC0)|0x00020000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t"+'\t'.join(data)+'\n')
    print("Testcase 61 created")
def testcase_62(n_set=16):
    base_path="subsystem_testcase/testcase_62/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,4)
    remaining_tags=list(set(available_tags)-set(selected_tags)); new_tag=random.choice(remaining_tags)
    with open(path_1,'w') as f:
        for tag in selected_tags:  # 4 lệnh write với tag khác nhau
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0001FFFF)|0x00020000
            data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{addr:08x}\t{data}\n")
        word_offset=random.randint(0,15)  # lệnh read với tag mới
        read_addr=(new_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        read_addr=(read_addr&0x0001FFFF)|0x00020000; f.write(f"read\t0x{read_addr:08x}\n")
        word_offset=random.randint(0,15)  # lệnh write trùng tag với read vừa tạo
        write_addr=(new_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        write_addr=(write_addr&0x0001FFFF)|0x00020000
        data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{write_addr:08x}\t{data}")
    with open(path_0,'w') as f: pass
    with open(path_mem,'w') as f:
        for tag in selected_tags+[new_tag]:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0001FFC0)|0x00020000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t"+'\t'.join(data)+'\n')
    print("Testcase 62 created")
def testcase_63(n_set=16):
    base_path="subsystem_testcase/testcase_63/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    num_read=random.randint(1,3); available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,num_read)
    remaining_tags=list(set(available_tags)-set(selected_tags)); new_tag=random.choice(remaining_tags)
    with open(path_1,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0001FFFF)|0x00020000; f.write(f"read\t0x{addr:08x}\n")
        word_offset=random.randint(0,15)
        read_addr=(new_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        read_addr=(read_addr&0x0001FFFF)|0x00020000; f.write(f"read\t0x{read_addr:08x}\n")
        word_offset=random.randint(0,15)
        write_addr=(new_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        write_addr=(write_addr&0x0001FFFF)|0x00020000
        data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{write_addr:08x}\t{data}")
    with open(path_0,'w') as f:
        word_offset=random.randint(0,15)
        addr=(new_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        addr=(addr&0x0001FFFF)|0x00020000; f.write(f"read\t0x{addr:08x}")
    with open(path_mem,'w') as f:
        for tag in selected_tags+[new_tag]:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0001FFC0)|0x00020000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t"+'\t'.join(data)+'\n')
    print("Testcase 63 created")
def testcase_64(n_set=16):
    base_path="subsystem_testcase/testcase_64/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,4)
    remaining_tags=list(set(available_tags)-set(selected_tags)); new_tag=random.choice(remaining_tags)
    with open(path_1,'w') as f:
        for tag in selected_tags:  # 4 read khác tag
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0001FFFF)|0x00020000
            f.write(f"read\t0x{addr:08x}\n")
        word_offset=random.randint(0,15)  # read với tag mới
        read_addr=(new_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        read_addr=(read_addr&0x0001FFFF)|0x00020000; f.write(f"read\t0x{read_addr:08x}\n")
        word_offset=random.randint(0,15)  # write trùng tag với read trên
        write_addr=(new_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        write_addr=(write_addr&0x0001FFFF)|0x00020000
        data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{write_addr:08x}\t{data}")
    with open(path_0,'w') as f:  # inst_1 read trùng tag cuối
        word_offset=random.randint(0,15)
        inst1_addr=(new_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        inst1_addr=(inst1_addr&0x0001FFFF)|0x00020000; f.write(f"read\t0x{inst1_addr:08x}")
    with open(path_mem,'w') as f:
        for tag in selected_tags+[new_tag]:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0001FFC0)|0x00020000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t"+'\t'.join(data)+'\n')
    print("Testcase 64 created")
def testcase_65(n_set=16):
    base_path="subsystem_testcase/testcase_65/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,4)
    remaining_tags=list(set(available_tags)-set(selected_tags)); mid_tag=random.choice(remaining_tags)
    with open(path_1,'w') as f:
        for tag in selected_tags:  # 4 write khác tag
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0001FFFF)|0x00020000
            data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{addr:08x}\t{data}\n")
        word_offset=random.randint(0,15)  # read với tag mới
        read_addr=(mid_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        read_addr=(read_addr&0x0001FFFF)|0x00020000; f.write(f"read\t0x{read_addr:08x}\n")
        word_offset=random.randint(0,15)  # write lại đúng tag của read trên
        write_addr=(mid_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        write_addr=(write_addr&0x0001FFFF)|0x00020000
        data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{write_addr:08x}\t{data}")
    with open(path_0,'w') as f:  # inst_1 đọc lại đúng tag của write cuối
        word_offset=random.randint(0,15)
        inst1_addr=(mid_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        inst1_addr=(inst1_addr&0x0001FFFF)|0x00020000; f.write(f"read\t0x{inst1_addr:08x}")
    with open(path_mem,'w') as f:
        for tag in selected_tags+[mid_tag]:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0001FFC0)|0x00020000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t"+'\t'.join(data)+'\n')
    print("Testcase 65 created")
def testcase_66(n_set=16):
    base_path="subsystem_testcase/testcase_66/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); num_reads=random.randint(1,4)
    selected_tags=random.sample(available_tags,num_reads)
    shared_tag=random.choice(selected_tags)
    with open(path_1,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0001FFFF)|0x00020000; f.write(f"read\t0x{addr:08x}\n")
        word_offset=random.randint(0,15)
        write_addr=(shared_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        write_addr=(write_addr&0x0001FFFF)|0x00020000
        data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{write_addr:08x}\t{data}\n")
        word_offset=random.randint(0,15)
        read_addr2=(shared_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        read_addr2=(read_addr2&0x0001FFFF)|0x00020000; f.write(f"read\t0x{read_addr2:08x}")
    with open(path_0,'w') as f: pass
    with open(path_mem,'w') as f:
        all_tags=set(selected_tags+[shared_tag])
        for tag in all_tags:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0001FFC0)|0x00020000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t"+'\t'.join(data)+'\n')
    print("Testcase 66 created")
def testcase_67(n_set=16):
    base_path="subsystem_testcase/testcase_67/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(int(n_set).bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); num_reads=random.randint(1,3)
    selected_tags=random.sample(available_tags,num_reads)
    remaining_tags=list(set(available_tags)-set(selected_tags)); write_tag=random.choice(remaining_tags)
    with open(path_1,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0001FFFF)|0x00020000; f.write(f"read\t0x{addr:08x}\n")
        word_offset=random.randint(0,15)
        write_addr=(write_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        write_addr=(write_addr&0x0001FFFF)|0x00020000
        data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{write_addr:08x}\t{data}\n")
        word_offset=random.randint(0,15)
        read_addr2=(write_tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)|(word_offset<<2)
        read_addr2=(read_addr2&0x0001FFFF)|0x00020000; f.write(f"read\t0x{read_addr2:08x}")
    with open(path_0,'w') as f: pass
    with open(path_mem,'w') as f:
        all_tags=set(selected_tags+[write_tag])
        for tag in all_tags:
            block_addr=(tag<<(4+int(n_set).bit_length()+2))|(set_index<<6)
            block_addr=(block_addr&0x0001FFC0)|0x00020000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t"+'\t'.join(data)+'\n')
    print("Testcase 67 created")
def testcase_68(n_set=16):
    base_path = "subsystem_testcase/testcase_68/"; os.makedirs(base_path, exist_ok=True)
    path_0 = os.path.join(base_path, "instr_mem_A.mem"); path_1 = os.path.join(base_path, "instr_mem_B.mem"); path_mem = os.path.join(base_path, "main_memory_init.mem")
    tag_bits = 32 - (n_set.bit_length() + 4 + 2); set_index = random.randint(0, n_set - 1)
    available_tags = list(range(1 << tag_bits)); selected_tags = random.sample(available_tags, 4)
    remaining_tags = list(set(available_tags) - set(selected_tags)); write_tag = random.choice(remaining_tags)
    all_tags = selected_tags + [write_tag]
    with open(path_1, 'w') as f:
        for tag in selected_tags:  # 4 read cùng set khác tag
            word_offset = random.randint(0, 15)
            addr = (tag << (n_set.bit_length() + 4 + 2)) | (set_index << 6) | (word_offset << 2)
            addr = (addr & 0x0001FFFF) | 0x00020000; f.write(f"read\t0x{addr:08x}\n")
        word_offset = random.randint(0, 15)  # write cùng set, tag khác
        write_addr = (write_tag << (n_set.bit_length() + 4 + 2)) | (set_index << 6) | (word_offset << 2)
        write_addr = (write_addr & 0x0001FFFF) | 0x00020000
        data = f"0x{random.randint(0, 2 ** 32 - 1):08x}"; f.write(f"write\t0x{write_addr:08x}\t{data}\n")
        read_offset = random.randint(0, 15)  # read lại đúng tag của lệnh write
        read_addr = (write_tag << (n_set.bit_length() + 4 + 2)) | (set_index << 6) | (read_offset << 2)
        read_addr = (read_addr & 0x0001FFFF) | 0x00020000; f.write(f"read\t0x{read_addr:08x}")
    with open(path_0, 'w') as f: pass
    with open(path_mem, 'w') as f:
        for tag in all_tags:
            block_addr = (tag << (n_set.bit_length() + 4 + 2)) | (set_index << 6)
            block_addr = (block_addr & 0x0001FFC0) | 0x00020000
            data = [f"0x{random.randint(0, 2**32 - 1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t" + '\t'.join(data) + '\n')
    print("Testcase 68 created")
def testcase_69(n_set=16):
    base_path="subsystem_testcase/testcase_69/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(n_set.bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); selected_tags=random.sample(available_tags,4)
    remaining_tags=list(set(available_tags)-set(selected_tags)); write_tag=random.choice(remaining_tags); all_tags=selected_tags+[write_tag]
    def shared(addr): return (addr&0x0003FFFF)|0x00020000
    with open(path_1,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15); addr=(tag<<(n_set.bit_length()+4+2))|(set_index<<6)|(word_offset<<2); addr=shared(addr)
            data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{addr:08x}\t{data}\n")
        word_offset=random.randint(0,15); write_addr=(write_tag<<(n_set.bit_length()+4+2))|(set_index<<6)|(word_offset<<2); write_addr=shared(write_addr)
        data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{write_addr:08x}\t{data}\n")
        read_offset=random.randint(0,15); read_addr=(write_tag<<(n_set.bit_length()+4+2))|(set_index<<6)|(read_offset<<2); read_addr=shared(read_addr)
        f.write(f"read\t0x{read_addr:08x}")
    with open(path_0,'w') as f: pass
    with open(path_mem,'w') as f:
        for tag in all_tags:
            block_addr=(tag<<(n_set.bit_length()+4+2))|(set_index<<6); block_addr=shared(block_addr&0xFFFFFFC0)
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t"+'\t'.join(data)+'\n')
    print("Testcase 69 created")
def testcase_70(n_set=16):
    base_path="subsystem_testcase/testcase_70/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(n_set.bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=list(range(1<<tag_bits)); num_read=random.randint(1,3); selected_tags=random.sample(available_tags,num_read)
    remaining_tags=list(set(available_tags)-set(selected_tags)); write_tag=random.choice(remaining_tags)
    def shared(addr): return (addr&0x0003FFFF)|0x00020000
    addr_list=[]  # thu thập địa chỉ cần tạo mem
    with open(path_1,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15); addr=(tag<<(n_set.bit_length()+4+2))|(set_index<<6)|(word_offset<<2); addr=shared(addr)
            f.write(f"read\t0x{addr:08x}\n"); addr_list.append(addr)
        word_offset=random.randint(0,15); write_addr=(write_tag<<(n_set.bit_length()+4+2))|(set_index<<6)|(word_offset<<2); write_addr=shared(write_addr)
        data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{write_addr:08x}\t{data}\n"); addr_list.append(write_addr)
        read_offset=random.randint(0,15); read_addr=(write_tag<<(n_set.bit_length()+4+2))|(set_index<<6)|(read_offset<<2); read_addr=shared(read_addr)
        f.write(f"read\t0x{read_addr:08x}"); addr_list.append(read_addr)
    with open(path_0,'w') as f:
        ref_offset=random.randint(0,15); ref_addr=(write_tag<<(n_set.bit_length()+4+2))|(set_index<<6)|(ref_offset<<2); ref_addr=shared(ref_addr)
        f.write(f"read\t0x{ref_addr:08x}"); addr_list.append(ref_addr)
    with open(path_mem,'w') as f:
        blocks=set([(addr>>6)<<6 for addr in addr_list])
        for block_addr in blocks:
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t"+'\t'.join(data)+'\n')
    print("Testcase 70 created")
def testcase_71(n_set=16):
    base_path="subsystem_testcase/testcase_71/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(n_set.bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=set(range(1<<tag_bits)); selected_tags=random.sample(list(available_tags),4)
    remaining_tags=list(available_tags-set(selected_tags)); write_tag=random.choice(remaining_tags)
    all_tags=selected_tags+[write_tag]; used_blocks=set()
    with open(path_1,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15); addr=(tag<<(4+n_set.bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0000FFFF)|0x00020000; f.write(f"read\t0x{addr:08x}\n")
        word_offset=random.randint(0,15); write_addr=(write_tag<<(4+n_set.bit_length()+2))|(set_index<<6)|(word_offset<<2)
        write_addr=(write_addr&0x0000FFFF)|0x00020000; data=f"0x{random.randint(0,2**32-1):08x}"
        f.write(f"write\t0x{write_addr:08x}\t{data}\n")
        word_offset=random.randint(0,15); read_back=(write_tag<<(4+n_set.bit_length()+2))|(set_index<<6)|(word_offset<<2)
        read_back=(read_back&0x0000FFFF)|0x00020000; f.write(f"read\t0x{read_back:08x}")
    with open(path_0,'w') as f:
        word_offset=random.randint(0,15); addr=(write_tag<<(4+n_set.bit_length()+2))|(set_index<<6)|(word_offset<<2)
        addr=(addr&0x0000FFFF)|0x00020000; f.write(f"read\t0x{addr:08x}")
    with open(path_mem,'w') as f:
        for tag in all_tags:
            block_addr=(tag<<(4+n_set.bit_length()+2))|(set_index<<6); block_addr=(block_addr&0x0000FFC0)|0x00020000
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t"+'\t'.join(data)+'\n')
    print("Testcase 71 created")
def testcase_72(n_set=16):
    base_path="subsystem_testcase/testcase_72/"; os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem"); path_1=os.path.join(base_path,"instr_mem_B.mem"); path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(n_set.bit_length()+4+2); set_index=random.randint(0,n_set-1)
    available_tags=set(range(1<<tag_bits)); selected_tags=random.sample(list(available_tags),4)
    remaining_tags=list(available_tags-set(selected_tags)); write_tag=random.choice(remaining_tags)
    all_tags=selected_tags+[write_tag]
    with open(path_1,'w') as f:
        for tag in selected_tags:
            word_offset=random.randint(0,15)
            addr=(tag<<(4+n_set.bit_length()+2))|(set_index<<6)|(word_offset<<2)
            addr=(addr&0x0000FFFF)|0x00020000
            data=f"0x{random.randint(0,2**32-1):08x}"
            f.write(f"write\t0x{addr:08x}\t{data}\n")
        word_offset=random.randint(0,15)
        write_addr=(write_tag<<(4+n_set.bit_length()+2))|(set_index<<6)|(word_offset<<2); write_addr=(write_addr&0x0000FFFF)|0x00020000
        data=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{write_addr:08x}\t{data}\n")
        word_offset=random.randint(0,15)
        read_addr=(write_tag<<(4+n_set.bit_length()+2))|(set_index<<6)|(word_offset<<2); read_addr=(read_addr&0x0000FFFF)|0x00020000
        f.write(f"read\t0x{read_addr:08x}")
    with open(path_0,'w') as f:
        word_offset=random.randint(0,15)
        addr=(write_tag<<(4+n_set.bit_length()+2))|(set_index<<6)|(word_offset<<2); addr=(addr&0x0000FFFF)|0x00020000
        f.write(f"read\t0x{addr:08x}")
    written_blocks=set()
    with open(path_mem,'w') as f:
        for tag in all_tags:
            block_addr=(tag<<(4+n_set.bit_length()+2))|(set_index<<6); block_addr=(block_addr&0x0000FFC0)|0x00020000
            if block_addr in written_blocks: continue
            written_blocks.add(block_addr)
            data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            f.write(f"0x{block_addr:08x}\t"+'\t'.join(data)+'\n')
    print("Testcase 72 created")
def testcase_73(n_set=16):
    base="subsystem_testcase/testcase_73/"; os.makedirs(base,exist_ok=True)
    p0=os.path.join(base,"instr_mem_A.mem"); p1=os.path.join(base,"instr_mem_B.mem"); pm=os.path.join(base,"main_memory_init.mem")
    tag_bits=32-(n_set.bit_length()+4+2); set_idx=random.randint(0,n_set-1)
    tags=random.sample(range(1<<tag_bits),4); used=set(tags)
    rtag=random.choice(list(set(range(1<<tag_bits))-used)); all_addrs=[]
    with open(p0,'w') as f:
        for t in tags:
            wo=random.randint(0,15); a=(t<<(n_set.bit_length()+6))|(set_idx<<6)|(wo<<2); a=(a&0x3FFFF)|0x20000
            f.write(f"write\t0x{a:08x}\t0x{random.randint(0,2**32-1):08x}\n"); all_addrs.append(a)
        rwo=random.randint(0,15); ra=(rtag<<(n_set.bit_length()+6))|(set_idx<<6)|(rwo<<2); ra=(ra&0x3FFFF)|0x20000
        f.write(f"read\t0x{ra:08x}"); all_addrs.append(ra)
    with open(p1,'w') as f:
        wwo=random.randint(0,15); wa=(rtag<<(n_set.bit_length()+6))|(set_idx<<6)|(wwo<<2); wa=(wa&0x3FFFF)|0x20000
        f.write(f"write\t0x{wa:08x}\t0x{random.randint(0,2**32-1):08x}"); all_addrs.append(wa)
    written_blocks=set();
    with open(pm,'w') as f:
        for addr in all_addrs:
            block=(addr>>6)<<6; block=(block&0x3FFC0)|0x20000
            if block not in written_blocks:
                data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
                f.write(f"0x{block:08x}\t"+'\t'.join(data)+'\n'); written_blocks.add(block)
    print("Testcase 73 created")
def testcase_74(n_set=16):
    base="subsystem_testcase/testcase_74/"; os.makedirs(base,exist_ok=True)
    p0=os.path.join(base,"instr_mem_A.mem"); p1=os.path.join(base,"instr_mem_B.mem"); pm=os.path.join(base,"main_memory_init.mem")
    tag_bits=32-(n_set.bit_length()+4+2); set_idx=random.randint(0,n_set-1)
    tags=random.sample(range(1<<tag_bits),4); used=set(tags)
    rtag=random.choice(list(set(range(1<<tag_bits))-used)); all_addrs=[]
    with open(p0,'w') as f:
        for t in tags:
            wo=random.randint(0,15); a=(t<<(n_set.bit_length()+6))|(set_idx<<6)|(wo<<2); a=(a&0x3FFFF)|0x20000
            f.write(f"write\t0x{a:08x}\t0x{random.randint(0,2**32-1):08x}\n"); all_addrs.append(a)
        rwo=random.randint(0,15); ra=(rtag<<(n_set.bit_length()+6))|(set_idx<<6)|(rwo<<2); ra=(ra&0x3FFFF)|0x20000
        f.write(f"read\t0x{ra:08x}"); all_addrs.append(ra)
    with open(p1,'w') as f:
        diff_set=(set_idx+1)%n_set; wo=random.randint(0,15)
        tag=random.choice(list(set(range(1<<tag_bits))-used-{rtag}))
        a=(tag<<(n_set.bit_length()+6))|(diff_set<<6)|(wo<<2); a=(a&0x3FFFF)|0x20000
        f.write(f"write\t0x{a:08x}\t0x{random.randint(0,2**32-1):08x}"); all_addrs.append(a)
    written_blocks=set();
    with open(pm,'w') as f:
        for addr in all_addrs:
            block=(addr>>6)<<6; block=(block&0x3FFC0)|0x20000
            if block not in written_blocks:
                data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
                f.write(f"0x{block:08x}\t"+'\t'.join(data)+'\n'); written_blocks.add(block)
    print("Testcase 74 created")
def testcase_75(n_set=16):
    base="subsystem_testcase/testcase_75/"; os.makedirs(base,exist_ok=True)
    p0=os.path.join(base,"instr_mem_A.mem"); p1=os.path.join(base,"instr_mem_B.mem"); pm=os.path.join(base,"main_memory_init.mem")
    tag_bits=32-(n_set.bit_length()+4+2); set_idx=random.randint(0,n_set-1)
    tags=random.sample(range(1<<tag_bits),4); used=set(tags)
    wtag=random.choice(list(set(range(1<<tag_bits))-used)); all_addrs=[]
    with open(p0,'w') as f:
        for t in tags:
            wo=random.randint(0,15); a=(t<<(n_set.bit_length()+6))|(set_idx<<6)|(wo<<2); a=(a&0x3FFFF)|0x20000
            f.write(f"write\t0x{a:08x}\t0x{random.randint(0,2**32-1):08x}\n"); all_addrs.append(a)
        wwo=random.randint(0,15); wa=(wtag<<(n_set.bit_length()+6))|(set_idx<<6)|(wwo<<2); wa=(wa&0x3FFFF)|0x20000
        wdata=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{wa:08x}\t{wdata}"); all_addrs.append(wa)
    with open(p1,'w') as f:
        rwo=random.randint(0,15); ra=(wtag<<(n_set.bit_length()+6))|(set_idx<<6)|(rwo<<2); ra=(ra&0x3FFFF)|0x20000
        f.write(f"read\t0x{ra:08x}"); all_addrs.append(ra)
    written_blocks=set();
    with open(pm,'w') as f:
        for addr in all_addrs:
            block=(addr>>6)<<6; block=(block&0x3FFC0)|0x20000
            if block not in written_blocks:
                data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
                f.write(f"0x{block:08x}\t"+'\t'.join(data)+'\n'); written_blocks.add(block)
    print("Testcase 75 created")
def testcase_76(n_set=16):
    base="subsystem_testcase/testcase_76/"; os.makedirs(base,exist_ok=True)
    p0=os.path.join(base,"instr_mem_A.mem"); p1=os.path.join(base,"instr_mem_B.mem"); pm=os.path.join(base,"main_memory_init.mem")
    tag_bits=32-(n_set.bit_length()+4+2); set_idx=random.randint(0,n_set-1)
    tags=random.sample(range(1<<tag_bits),4); used_tags=set(tags)
    wtag=random.choice(list(set(range(1<<tag_bits))-used_tags)); all_addrs=[]
    with open(p0,'w') as f:
        for t in tags:
            wo=random.randint(0,15); a=(t<<(n_set.bit_length()+6))|(set_idx<<6)|(wo<<2); a=(a&0x3FFFF)|0x20000
            f.write(f"write\t0x{a:08x}\t0x{random.randint(0,2**32-1):08x}\n"); all_addrs.append(a)
        wwo=random.randint(0,15); wa=(wtag<<(n_set.bit_length()+6))|(set_idx<<6)|(wwo<<2); wa=(wa&0x3FFFF)|0x20000
        f.write(f"write\t0x{wa:08x}\t0x{random.randint(0,2**32-1):08x}"); all_addrs.append(wa)
    inst1_set=(set_idx+1)%n_set; rtag=random.randint(0,(1<<tag_bits)-1); rwo=random.randint(0,15)
    ra=(rtag<<(n_set.bit_length()+6))|(inst1_set<<6)|(rwo<<2); ra=(ra&0x3FFFF)|0x20000
    with open(p1,'w') as f: f.write(f"read\t0x{ra:08x}"); all_addrs.append(ra)
    written=set();
    with open(pm,'w') as f:
        for addr in all_addrs:
            block=(addr>>6)<<6; block=(block&0x3FFC0)|0x20000
            if block not in written:
                data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
                f.write(f"0x{block:08x}\t"+'\t'.join(data)+'\n'); written.add(block)
    print("Testcase 76 created")
def testcase_77(n_set=16):
    base="subsystem_testcase/testcase_77/"; os.makedirs(base,exist_ok=True)
    p0=os.path.join(base,"instr_mem_A.mem"); p1=os.path.join(base,"instr_mem_B.mem"); pm=os.path.join(base,"main_memory_init.mem")
    tag_bits=32-(n_set.bit_length()+4+2); set_idx=random.randint(0,n_set-1)
    tags=random.sample(range(1<<tag_bits),4); used=set(tags)
    rtag=random.choice(list(set(range(1<<tag_bits))-used)); all_addrs=[]
    with open(p1,'w') as f:
        for t in tags:
            wo=random.randint(0,15); a=(t<<(n_set.bit_length()+6))|(set_idx<<6)|(wo<<2); a=(a&0x3FFFF)|0x20000
            f.write(f"write\t0x{a:08x}\t0x{random.randint(0,2**32-1):08x}\n"); all_addrs.append(a)
        rwo=random.randint(0,15); ra=(rtag<<(n_set.bit_length()+6))|(set_idx<<6)|(rwo<<2); ra=(ra&0x3FFFF)|0x20000
        f.write(f"read\t0x{ra:08x}"); all_addrs.append(ra)
    with open(p0,'w') as f:
        wwo=random.randint(0,15); wa=(rtag<<(n_set.bit_length()+6))|(set_idx<<6)|(wwo<<2); wa=(wa&0x3FFFF)|0x20000
        f.write(f"write\t0x{wa:08x}\t0x{random.randint(0,2**32-1):08x}"); all_addrs.append(wa)
    written_blocks=set();
    with open(pm,'w') as f:
        for addr in all_addrs:
            block=(addr>>6)<<6; block=(block&0x3FFC0)|0x20000
            if block not in written_blocks:
                data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
                f.write(f"0x{block:08x}\t"+'\t'.join(data)+'\n'); written_blocks.add(block)
    print("Testcase 77 created")
def testcase_78(n_set=16):
    base="subsystem_testcase/testcase_78/"; os.makedirs(base,exist_ok=True)
    p0=os.path.join(base,"instr_mem_A.mem"); p1=os.path.join(base,"instr_mem_B.mem"); pm=os.path.join(base,"main_memory_init.mem")
    tag_bits=32-(n_set.bit_length()+4+2); set_idx=random.randint(0,n_set-1)
    tags=random.sample(range(1<<tag_bits),4); used=set(tags)
    rtag=random.choice(list(set(range(1<<tag_bits))-used)); all_addrs=[]
    with open(p1,'w') as f:
        for t in tags:
            wo=random.randint(0,15); a=(t<<(n_set.bit_length()+6))|(set_idx<<6)|(wo<<2); a=(a&0x3FFFF)|0x20000
            f.write(f"write\t0x{a:08x}\t0x{random.randint(0,2**32-1):08x}\n"); all_addrs.append(a)
        rwo=random.randint(0,15); ra=(rtag<<(n_set.bit_length()+6))|(set_idx<<6)|(rwo<<2); ra=(ra&0x3FFFF)|0x20000
        f.write(f"read\t0x{ra:08x}"); all_addrs.append(ra)
    with open(p0,'w') as f:
        diff_set=(set_idx+1)%n_set; wo=random.randint(0,15)
        tag=random.choice(list(set(range(1<<tag_bits))-used-{rtag}))
        a=(tag<<(n_set.bit_length()+6))|(diff_set<<6)|(wo<<2); a=(a&0x3FFFF)|0x20000
        f.write(f"write\t0x{a:08x}\t0x{random.randint(0,2**32-1):08x}"); all_addrs.append(a)
    written_blocks=set();
    with open(pm,'w') as f:
        for addr in all_addrs:
            block=(addr>>6)<<6; block=(block&0x3FFC0)|0x20000
            if block not in written_blocks:
                data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
                f.write(f"0x{block:08x}\t"+'\t'.join(data)+'\n'); written_blocks.add(block)
    print("Testcase 78 created")
def testcase_79(n_set=16):
    base="subsystem_testcase/testcase_79/"; os.makedirs(base,exist_ok=True)
    p0=os.path.join(base,"instr_mem_A.mem"); p1=os.path.join(base,"instr_mem_B.mem"); pm=os.path.join(base,"main_memory_init.mem")
    tag_bits=32-(n_set.bit_length()+4+2); set_idx=random.randint(0,n_set-1)
    tags=random.sample(range(1<<tag_bits),4); used=set(tags)
    wtag=random.choice(list(set(range(1<<tag_bits))-used)); all_addrs=[]
    with open(p1,'w') as f:
        for t in tags:
            wo=random.randint(0,15); a=(t<<(n_set.bit_length()+6))|(set_idx<<6)|(wo<<2); a=(a&0x3FFFF)|0x20000
            f.write(f"write\t0x{a:08x}\t0x{random.randint(0,2**32-1):08x}\n"); all_addrs.append(a)
        wwo=random.randint(0,15); wa=(wtag<<(n_set.bit_length()+6))|(set_idx<<6)|(wwo<<2); wa=(wa&0x3FFFF)|0x20000
        wdata=f"0x{random.randint(0,2**32-1):08x}"; f.write(f"write\t0x{wa:08x}\t{wdata}"); all_addrs.append(wa)
    with open(p0,'w') as f:
        rwo=random.randint(0,15); ra=(wtag<<(n_set.bit_length()+6))|(set_idx<<6)|(rwo<<2); ra=(ra&0x3FFFF)|0x20000
        f.write(f"read\t0x{ra:08x}"); all_addrs.append(ra)
    written_blocks=set();
    with open(pm,'w') as f:
        for addr in all_addrs:
            block=(addr>>6)<<6; block=(block&0x3FFC0)|0x20000
            if block not in written_blocks:
                data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
                f.write(f"0x{block:08x}\t"+'\t'.join(data)+'\n'); written_blocks.add(block)
    print("Testcase 79 created")
def testcase_80(n_set=16):
    base="subsystem_testcase/testcase_80/"; os.makedirs(base,exist_ok=True)
    p0=os.path.join(base,"instr_mem_A.mem"); p1=os.path.join(base,"instr_mem_B.mem"); pm=os.path.join(base,"main_memory_init.mem")
    tag_bits=32-(n_set.bit_length()+4+2); set_idx=random.randint(0,n_set-1)
    tags=random.sample(range(1<<tag_bits),4); used_tags=set(tags)
    wtag=random.choice(list(set(range(1<<tag_bits))-used_tags)); all_addrs=[]
    with open(p1,'w') as f:
        for t in tags:
            wo=random.randint(0,15); a=(t<<(n_set.bit_length()+6))|(set_idx<<6)|(wo<<2); a=(a&0x3FFFF)|0x20000
            f.write(f"write\t0x{a:08x}\t0x{random.randint(0,2**32-1):08x}\n"); all_addrs.append(a)
        wwo=random.randint(0,15); wa=(wtag<<(n_set.bit_length()+6))|(set_idx<<6)|(wwo<<2); wa=(wa&0x3FFFF)|0x20000
        f.write(f"write\t0x{wa:08x}\t0x{random.randint(0,2**32-1):08x}"); all_addrs.append(wa)
    inst1_set=(set_idx+1)%n_set; rtag=random.randint(0,(1<<tag_bits)-1); rwo=random.randint(0,15)
    ra=(rtag<<(n_set.bit_length()+6))|(inst1_set<<6)|(rwo<<2); ra=(ra&0x3FFFF)|0x20000
    with open(p0,'w') as f: f.write(f"read\t0x{ra:08x}"); all_addrs.append(ra)
    written=set();
    with open(pm,'w') as f:
        for addr in all_addrs:
            block=(addr>>6)<<6; block=(block&0x3FFC0)|0x20000
            if block not in written:
                data=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
                f.write(f"0x{block:08x}\t"+'\t'.join(data)+'\n'); written.add(block)
    print("Testcase 80 created")
def testcase_81(n_set=16):
    base_path = "subsystem_testcase/testcase_81/"
    os.makedirs(base_path, exist_ok=True)
    path_0 = os.path.join(base_path, "instr_mem_A.mem")
    path_1 = os.path.join(base_path, "instr_mem_B.mem")
    path_mem = os.path.join(base_path, "main_memory_init.mem")
    tag_bits = 32 - (n_set.bit_length() + 4 + 2)
    def shared(addr): return (addr & 0x3FFFF) | 0x20000
    def block_addr(addr): return addr & 0xFFFFFFC0
    setA = random.randint(0, n_set - 1)
    tagA = random.randint(0, (1 << tag_bits) - 1)
    wordA = random.randint(0, 15)
    readA = shared((tagA << (n_set.bit_length() + 4 + 2)) | (setA << 6) | (wordA << 2))
    setB = random.randint(0, n_set - 1)
    tagB = random.randint(0, (1 << tag_bits) - 1)
    wordB = random.randint(0, 15)
    readB = shared((tagB << (n_set.bit_length() + 4 + 2)) | (setB << 6) | (wordB << 2))
    wordB2 = random.randint(0, 15)
    readB2 = shared((tagB << (n_set.bit_length() + 4 + 2)) | (setB << 6) | (wordB2 << 2))
    wordA2 = random.randint(0, 15)
    readA2 = shared((tagA << (n_set.bit_length() + 4 + 2)) | (setA << 6) | (wordA2 << 2))
    with open(path_0, "w") as f0:
        f0.write(f"read\t0x{readA:08x}\nread\t0x{readB:08x}\n")
    with open(path_1, "w") as f1:
        f1.write(f"read\t0x{readB2:08x}\nread\t0x{readA2:08x}\n")
    blocks = {block_addr(readA), block_addr(readB)}
    with open(path_mem, "w") as fm:
        for blk in blocks:
            data_words = [f"0x{random.randint(0, 2**32 - 1):08x}" for _ in range(16)]
            fm.write(f"0x{blk:08x}\t" + "\t".join(data_words) + "\n")
    print("Testcase 81 created")
def testcase_82(n_set=16):
    base_path = "subsystem_testcase/testcase_82/"
    os.makedirs(base_path, exist_ok=True)
    path_0 = os.path.join(base_path,"instr_mem_A.mem")
    path_1 = os.path.join(base_path,"instr_mem_B.mem")
    path_mem = os.path.join(base_path,"main_memory_init.mem")
    tag_bits = 32 - (n_set.bit_length() + 4 + 2)
    def shared(addr): return (addr & 0x3FFFF) | 0x20000
    def block_addr(addr): return addr & 0xFFFFFFC0
    setA = random.randint(0,n_set-1)
    tagA = random.randint(0,(1<<tag_bits)-1)
    wordA = random.randint(0,15)
    readA = shared((tagA<<(n_set.bit_length()+4+2)) | (setA<<6) | (wordA<<2))
    setB = random.randint(0,n_set-1)
    tagB = random.randint(0,(1<<tag_bits)-1)
    wordB = random.randint(0,15)
    readB = shared((tagB<<(n_set.bit_length()+4+2)) | (setB<<6) | (wordB<<2))
    wordB2 = random.randint(0,15)
    readB2 = shared((tagB<<(n_set.bit_length()+4+2)) | (setB<<6) | (wordB2<<2))
    while True:
        setX = random.randint(0,n_set-1)
        if setX!=setA and setX!=setB:
            break
    tagX = random.randint(0,(1<<tag_bits)-1)
    wordX = random.randint(0,15)
    readX = shared((tagX<<(n_set.bit_length()+4+2)) | (setX<<6) | (wordX<<2))
    with open(path_0,"w") as f0:
        f0.write(f"read\t0x{readA:08x}\nread\t0x{readB:08x}\n")
    with open(path_1,"w") as f1:
        f1.write(f"read\t0x{readB2:08x}\nread\t0x{readX:08x}\n")
    blocks = {block_addr(readA), block_addr(readB), block_addr(readX)}
    with open(path_mem,"w") as fm:
        for blk in blocks:
            data_words = [f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            fm.write(f"0x{blk:08x}\t" + "\t".join(data_words) + "\n")
    print("Testcase 82 created")
def testcase_83(n_set=16):
    base_path = "subsystem_testcase/testcase_83/"
    os.makedirs(base_path, exist_ok=True)
    path_0 = os.path.join(base_path, "instr_mem_A.mem")
    path_1 = os.path.join(base_path, "instr_mem_B.mem")
    path_mem = os.path.join(base_path, "main_memory_init.mem")
    tag_bits = 32 - (n_set.bit_length() + 4 + 2)
    def shared(addr): return (addr & 0x3FFFF) | 0x20000
    def block_addr(addr): return addr & 0xFFFFFFC0
    setA = random.randint(0, n_set - 1)
    tagA = random.randint(0, (1 << tag_bits) - 1)
    wordA = random.randint(0, 15)
    readA = shared((tagA << (n_set.bit_length()+4+2)) | (setA << 6) | (wordA << 2))
    setB = random.randint(0, n_set - 1)
    tagB = random.randint(0, (1 << tag_bits) - 1)
    wordB = random.randint(0, 15)
    readB = shared((tagB << (n_set.bit_length()+4+2)) | (setB << 6) | (wordB << 2))
    while True:
        setX = random.randint(0, n_set - 1)
        if setX != setA and setX != setB:
            break
    tagX = random.randint(0, (1 << tag_bits) - 1)
    wordX = random.randint(0, 15)
    readX = shared((tagX << (n_set.bit_length()+4+2)) | (setX << 6) | (wordX << 2))
    wordA2 = random.randint(0, 15)
    readA2 = shared((tagA << (n_set.bit_length()+4+2)) | (setA << 6) | (wordA2 << 2))
    with open(path_0, "w") as f0:
        f0.write(f"read\t0x{readA:08x}\nread\t0x{readB:08x}\n")
    with open(path_1, "w") as f1:
        f1.write(f"read\t0x{readX:08x}\nread\t0x{readA2:08x}\n")
    blocks = {block_addr(readA), block_addr(readB), block_addr(readX), block_addr(readA2)}
    with open(path_mem, "w") as fm:
        for blk in blocks:
            data_words = [f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            fm.write(f"0x{blk:08x}\t" + "\t".join(data_words) + "\n")
    print("Testcase 83 created")
def testcase_84(n_set=16):
    base_path = "subsystem_testcase/testcase_84/"
    os.makedirs(base_path, exist_ok=True)
    path_0 = os.path.join(base_path, "instr_mem_A.mem")
    path_1 = os.path.join(base_path, "instr_mem_B.mem")
    path_mem = os.path.join(base_path, "main_memory_init.mem")
    tag_bits = 32 - (n_set.bit_length() + 4 + 2)
    def shared(addr): return (addr & 0x3FFFF) | 0x20000
    def block_addr(addr): return addr & 0xFFFFFFC0
    setA = random.randint(0, n_set - 1)
    tagA = random.randint(0, (1 << tag_bits) - 1)
    wordA = random.randint(0, 15)
    readA = shared((tagA << (n_set.bit_length() + 4 + 2)) | (setA << 6) | (wordA << 2))
    setB = random.randint(0, n_set - 1)
    tagB = random.randint(0, (1 << tag_bits) - 1)
    wordB = random.randint(0, 15)
    writeB = shared((tagB << (n_set.bit_length() + 4 + 2)) | (setB << 6) | (wordB << 2))
    dataB = f"0x{random.randint(0, 2**32 - 1):08x}"
    wordB2 = random.randint(0, 15)
    readB = shared((tagB << (n_set.bit_length() + 4 + 2)) | (setB << 6) | (wordB2 << 2))
    wordA2 = random.randint(0, 15)
    writeA = shared((tagA << (n_set.bit_length() + 4 + 2)) | (setA << 6) | (wordA2 << 2))
    dataA = f"0x{random.randint(0, 2**32 - 1):08x}"
    with open(path_0, "w") as f0: f0.write(f"read\t0x{readA:08x}\nwrite\t0x{writeB:08x}\t{dataB}\n")
    with open(path_1, "w") as f1: f1.write(f"read\t0x{readB:08x}\nwrite\t0x{writeA:08x}\t{dataA}\n")
    blocks = {block_addr(readA), block_addr(writeB)}
    with open(path_mem, "w") as fm:
        for blk in blocks:
            data_words = [f"0x{random.randint(0, 2**32 - 1):08x}" for _ in range(16)]
            fm.write(f"0x{blk:08x}\t" + "\t".join(data_words) + "\n")
    print("Testcase 84 created")
def testcase_85(n_set=16):
    base_path="subsystem_testcase/testcase_85/"
    os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem")
    path_1=os.path.join(base_path,"instr_mem_B.mem")
    path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(n_set.bit_length()+4+2)
    def shared(addr): return (addr & 0x3FFFF) | 0x20000
    def block_addr(addr): return addr & 0xFFFFFFC0
    setA=random.randint(0,n_set-1)
    tagA=random.randint(0,(1<<tag_bits)-1)
    wordA=random.randint(0,15)
    readA=shared((tagA<<(n_set.bit_length()+4+2))|(setA<<6)|(wordA<<2))
    setB=random.randint(0,n_set-1)
    tagB=random.randint(0,(1<<tag_bits)-1)
    wordB=random.randint(0,15)
    writeB=shared((tagB<<(n_set.bit_length()+4+2))|(setB<<6)|(wordB<<2))
    dataB=f"0x{random.randint(0,2**32-1):08x}"
    wordB2=random.randint(0,15)
    readB=shared((tagB<<(n_set.bit_length()+4+2))|(setB<<6)|(wordB2<<2))
    while True:
        setX=random.randint(0,n_set-1)
        if setX!=setA and setX!=setB: break
    tagX=random.randint(0,(1<<tag_bits)-1)
    wordX=random.randint(0,15)
    writeX=shared((tagX<<(n_set.bit_length()+4+2))|(setX<<6)|(wordX<<2))
    dataX=f"0x{random.randint(0,2**32-1):08x}"
    with open(path_0,"w") as f0: f0.write(f"read\t0x{readA:08x}\nwrite\t0x{writeB:08x}\t{dataB}\n")
    with open(path_1,"w") as f1: f1.write(f"read\t0x{readB:08x}\nwrite\t0x{writeX:08x}\t{dataX}\n")
    blocks={block_addr(readA),block_addr(writeB),block_addr(readB),block_addr(writeX)}
    with open(path_mem,"w") as fm:
        for blk in blocks:
            fm.write(f"0x{blk:08x}\t"+'\t'.join(f"0x{random.randint(0,2**32-1):08x}"for _ in range(16))+"\n")
    print("Testcase 85 created")
def testcase_86(n_set=16):
    base_path="subsystem_testcase/testcase_86/"
    os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem")
    path_1=os.path.join(base_path,"instr_mem_B.mem")
    path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(n_set.bit_length()+4+2)
    def shared(addr): return (addr & 0x3FFFF) | 0x20000
    def block_addr(addr): return addr & 0xFFFFFFC0
    setA=random.randint(0,n_set-1)
    tagA=random.randint(0,(1<<tag_bits)-1)
    wordA=random.randint(0,15)
    readA=shared((tagA<<(n_set.bit_length()+4+2))|(setA<<6)|(wordA<<2))
    setB=random.randint(0,n_set-1)
    tagB=random.randint(0,(1<<tag_bits)-1)
    wordB=random.randint(0,15)
    writeB=shared((tagB<<(n_set.bit_length()+4+2))|(setB<<6)|(wordB<<2))
    dataB=f"0x{random.randint(0,2**32-1):08x}"
    while True:
        setX=random.randint(0,n_set-1)
        if setX!=setA and setX!=setB: break
    tagX=random.randint(0,(1<<tag_bits)-1)
    wordX=random.randint(0,15)
    readX=shared((tagX<<(n_set.bit_length()+4+2))|(setX<<6)|(wordX<<2))
    wordA2=random.randint(0,15)
    writeA2=shared((tagA<<(n_set.bit_length()+4+2))|(setA<<6)|(wordA2<<2))
    dataA2=f"0x{random.randint(0,2**32-1):08x}"
    with open(path_0,"w")as f0: f0.write(f"read\t0x{readA:08x}\nwrite\t0x{writeB:08x}\t{dataB}\n")
    with open(path_1,"w")as f1: f1.write(f"read\t0x{readX:08x}\nwrite\t0x{writeA2:08x}\t{dataA2}\n")
    blocks={block_addr(readA),block_addr(writeB),block_addr(readX),block_addr(writeA2)}
    with open(path_mem,"w")as fm:
        for blk in blocks: fm.write(f"0x{blk:08x}\t"+'\t'.join(f"0x{random.randint(0,2**32-1):08x}"for _ in range(16))+"\n")
    print("Testcase 86 created")
def testcase_87(n_set=16):
    base_path="subsystem_testcase/testcase_87/"
    os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem")
    path_1=os.path.join(base_path,"instr_mem_B.mem")
    path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(n_set.bit_length()+4+2)
    def shared(addr): return (addr & 0x3FFFF) | 0x20000
    def block_addr(addr): return addr & 0xFFFFFFC0
    setA=random.randint(0,n_set-1)
    tagA=random.randint(0,(1<<tag_bits)-1)
    wordA=random.randint(0,15)
    readA=shared((tagA<<(n_set.bit_length()+4+2))|(setA<<6)|(wordA<<2))
    setB=random.randint(0,n_set-1)
    tagB=random.randint(0,(1<<tag_bits)-1)
    wordB=random.randint(0,15)
    readB=shared((tagB<<(n_set.bit_length()+4+2))|(setB<<6)|(wordB<<2))
    wordB2=random.randint(0,15)
    readB2=shared((tagB<<(n_set.bit_length()+4+2))|(setB<<6)|(wordB2<<2))
    wordA2=random.randint(0,15)
    writeA2=shared((tagA<<(n_set.bit_length()+4+2))|(setA<<6)|(wordA2<<2))
    dataA2=f"0x{random.randint(0,2**32-1):08x}"
    with open(path_0,"w")as f0:
        f0.write(f"read\t0x{readA:08x}\nread\t0x{readB:08x}\n")
    with open(path_1,"w")as f1:
        f1.write(f"read\t0x{readB2:08x}\nwrite\t0x{writeA2:08x}\t{dataA2}\n")
    blocks={block_addr(readA),block_addr(readB),block_addr(readB2),block_addr(writeA2)}
    with open(path_mem,"w")as fm:
        for blk in blocks: fm.write(f"0x{blk:08x}\t"+'\t'.join(f"0x{random.randint(0,2**32-1):08x}"for _ in range(16))+"\n")
    print("Testcase 87 created")
def testcase_88(n_set=16):
    base_path="subsystem_testcase/testcase_88/"
    os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem")
    path_1=os.path.join(base_path,"instr_mem_B.mem")
    path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(n_set.bit_length()+4+2)
    def shared(addr): return (addr & 0x3FFFF) | 0x20000
    def block_addr(addr): return addr & 0xFFFFFFC0
    setA=random.randint(0,n_set-1)
    tagA=random.randint(0,(1<<tag_bits)-1)
    wordA=random.randint(0,15)
    readA=shared((tagA<<(n_set.bit_length()+4+2))|(setA<<6)|(wordA<<2))
    setB=random.randint(0,n_set-1)
    tagB=random.randint(0,(1<<tag_bits)-1)
    wordB=random.randint(0,15)
    readB=shared((tagB<<(n_set.bit_length()+4+2))|(setB<<6)|(wordB<<2))
    wordB2=random.randint(0,15)
    readB2=shared((tagB<<(n_set.bit_length()+4+2))|(setB<<6)|(wordB2<<2))
    while True:
        setX=random.randint(0,n_set-1)
        if setX!=setA and setX!=setB: break
    tagX=random.randint(0,(1<<tag_bits)-1)
    wordX=random.randint(0,15)
    writeX=shared((tagX<<(n_set.bit_length()+4+2))|(setX<<6)|(wordX<<2))
    dataX=f"0x{random.randint(0,2**32-1):08x}"
    with open(path_0,"w")as f0:
        f0.write(f"read\t0x{readA:08x}\nread\t0x{readB:08x}\n")
    with open(path_1,"w")as f1:
        f1.write(f"read\t0x{readB2:08x}\nwrite\t0x{writeX:08x}\t{dataX}\n")
    blocks={block_addr(readA),block_addr(readB),block_addr(readB2),block_addr(writeX)}
    with open(path_mem,"w")as fm:
        for blk in blocks:
            fm.write(f"0x{blk:08x}\t"+'\t'.join(f"0x{random.randint(0,2**32-1):08x}"for _ in range(16))+"\n")
    print("Testcase 88 created")
def testcase_89(n_set=16):
    base_path="subsystem_testcase/testcase_89/"
    os.makedirs(base_path,exist_ok=True)
    path_0=os.path.join(base_path,"instr_mem_A.mem")
    path_1=os.path.join(base_path,"instr_mem_B.mem")
    path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(n_set.bit_length()+4+2)
    def shared(addr): return (addr & 0x3FFFF) | 0x20000
    def block_addr(addr): return addr & 0xFFFFFFC0
    setA=random.randint(0,n_set-1)
    tagA=random.randint(0,(1<<tag_bits)-1)
    wordA=random.randint(0,15)
    readA=shared((tagA<<(n_set.bit_length()+4+2))|(setA<<6)|(wordA<<2))
    setB=random.randint(0,n_set-1)
    tagB=random.randint(0,(1<<tag_bits)-1)
    wordB=random.randint(0,15)
    readB=shared((tagB<<(n_set.bit_length()+4+2))|(setB<<6)|(wordB<<2))
    while True:
        setX=random.randint(0,n_set-1)
        if setX!=setA and setX!=setB: break
    tagX=random.randint(0,(1<<tag_bits)-1)
    wordX=random.randint(0,15)
    readX=shared((tagX<<(n_set.bit_length()+4+2))|(setX<<6)|(wordX<<2))
    wordA2=random.randint(0,15)
    writeA2=shared((tagA<<(n_set.bit_length()+4+2))|(setA<<6)|(wordA2<<2))
    dataA2=f"0x{random.randint(0,2**32-1):08x}"
    with open(path_0,"w")as f0:
        f0.write(f"read\t0x{readA:08x}\nread\t0x{readB:08x}\n")
    with open(path_1,"w")as f1:
        f1.write(f"read\t0x{readX:08x}\nwrite\t0x{writeA2:08x}\t{dataA2}\n")
    blocks={block_addr(readA),block_addr(readB),block_addr(readX),block_addr(writeA2)}
    with open(path_mem,"w")as fm:
        for blk in blocks:
            fm.write(f"0x{blk:08x}\t"+'\t'.join(f"0x{random.randint(0,2**32-1):08x}"for _ in range(16))+"\n")
    print("Testcase 89 created")
def testcase_90(n_set=16):
    base_path = "subsystem_testcase/testcase_90/"
    os.makedirs(base_path, exist_ok=True)
    path_inst0 = os.path.join(base_path, "instr_mem_A.mem")
    path_inst1 = os.path.join(base_path, "instr_mem_B.mem")
    path_mem = os.path.join(base_path, "main_memory_init.mem")
    tag_bits = 32 - (n_set.bit_length() + 4 + 2)
    def shared_address(addr): return (addr & 0x3FFFF) | 0x20000
    def block_address(addr): return addr & 0xFFFFFFC0
    set_inst0_1 = random.randint(0, n_set - 1)
    tag_inst0_1 = random.randint(0, (1 << tag_bits) - 1)
    word_inst0_1 = random.randint(0, 15)
    inst0_read1 = shared_address((tag_inst0_1 << (n_set.bit_length() + 4 + 2)) | (set_inst0_1 << 6) | (word_inst0_1 << 2))
    set_inst0_2 = random.randint(0, n_set - 1)
    tag_inst0_2 = random.randint(0, (1 << tag_bits) - 1)
    word_inst0_2 = random.randint(0, 15)
    inst0_read2 = shared_address((tag_inst0_2 << (n_set.bit_length() + 4 + 2)) | (set_inst0_2 << 6) | (word_inst0_2 << 2))
    word_inst0_3 = random.randint(0, 15)
    inst0_read3 = shared_address((tag_inst0_2 << (n_set.bit_length() + 4 + 2)) | (set_inst0_2 << 6) | (word_inst0_3 << 2))
    word_inst1 = random.randint(0, 15)
    inst1_read = shared_address((tag_inst0_1 << (n_set.bit_length() + 4 + 2)) | (set_inst0_1 << 6) | (word_inst1 << 2))
    with open(path_inst0, "w") as file_inst0: file_inst0.write(f"read\t0x{inst0_read1:08x}\nread\t0x{inst0_read2:08x}\nread\t0x{inst0_read3:08x}\n")
    with open(path_inst1, "w") as file_inst1: file_inst1.write(f"read\t0x{inst1_read:08x}\n")
    blocks = {block_address(inst0_read1), block_address(inst0_read2), block_address(inst0_read3)}
    with open(path_mem, "w") as file_mem:
        for block in blocks: file_mem.write(f"0x{block:08x}\t" + "\t".join(f"0x{random.randint(0, 2**32 - 1):08x}" for _ in range(16)) + "\n")
    print("Testcase 90 created")
def testcase_91(n_set=16):
    base_path = "subsystem_testcase/testcase_91/"
    os.makedirs(base_path, exist_ok=True)
    path_inst0 = os.path.join(base_path, "instr_mem_A.mem")
    path_inst1 = os.path.join(base_path, "instr_mem_B.mem")
    path_mem = os.path.join(base_path, "main_memory_init.mem")
    tag_bits = 32 - (n_set.bit_length() + 4 + 2)
    def shared(addr): return (addr & 0x3FFFF) | 0x20000
    def block_address(addr): return addr & 0xFFFFFFC0
    set_inst0_first = random.randint(0, n_set - 1)
    tag_inst0_first = random.randint(0, (1 << tag_bits) - 1)
    word_inst0_first = random.randint(0, 15)
    inst0_read1 = shared((tag_inst0_first << (n_set.bit_length() + 4 + 2)) | (set_inst0_first << 6) | (word_inst0_first << 2))
    set_inst0_second = random.randint(0, n_set - 1)
    tag_inst0_second = random.randint(0, (1 << tag_bits) - 1)
    word_inst0_second = random.randint(0, 15)
    inst0_read2 = shared((tag_inst0_second << (n_set.bit_length() + 4 + 2)) | (set_inst0_second << 6) | (word_inst0_second << 2))
    word_inst0_third = random.randint(0, 15)
    inst0_read3 = shared((tag_inst0_second << (n_set.bit_length() + 4 + 2)) | (set_inst0_second << 6) | (word_inst0_third << 2))
    while True:
        set_inst1 = random.randint(0, n_set - 1)
        if set_inst1 != set_inst0_first and set_inst1 != set_inst0_second:
            break
    tag_inst1 = random.randint(0, (1 << tag_bits) - 1)
    word_inst1 = random.randint(0, 15)
    inst1_read = shared((tag_inst1 << (n_set.bit_length() + 4 + 2)) | (set_inst1 << 6) | (word_inst1 << 2))
    with open(path_inst0, "w") as file_inst0:
        file_inst0.write(f"read\t0x{inst0_read1:08x}\nread\t0x{inst0_read2:08x}\nread\t0x{inst0_read3:08x}\n")
    with open(path_inst1, "w") as file_inst1:
        file_inst1.write(f"read\t0x{inst1_read:08x}\n")
    blocks = {block_address(inst0_read1), block_address(inst0_read2), block_address(inst0_read3), block_address(inst1_read)}
    with open(path_mem, "w") as file_mem:
        for block in blocks:
            file_mem.write(f"0x{block:08x}\t" + "\t".join(f"0x{random.randint(0, 2**32 - 1):08x}" for _ in range(16)) + "\n")
    print("Testcase 91 created")
def testcase_92(n_set=16):
    base_path = "subsystem_testcase/testcase_92/"
    os.makedirs(base_path, exist_ok=True)
    inst0_path = os.path.join(base_path, "instr_mem_A.mem")
    inst1_path = os.path.join(base_path, "instr_mem_B.mem")
    mem_data_path = os.path.join(base_path, "main_memory_init.mem")
    tag_bits = 32 - (n_set.bit_length() + 4 + 2)
    def shared_address(address): return (address & 0x3FFFF) | 0x20000
    def block_address(address): return address & 0xFFFFFFC0
    inst0_set1 = random.randint(0, n_set - 1)
    inst0_tag1 = random.randint(0, (1 << tag_bits) - 1)
    inst0_word1 = random.randint(0, 15)
    inst0_read1 = shared_address((inst0_tag1 << (n_set.bit_length() + 4 + 2)) | (inst0_set1 << 6) | (inst0_word1 << 2))
    inst0_set2 = random.randint(0, n_set - 1)
    inst0_tag2 = random.randint(0, (1 << tag_bits) - 1)
    inst0_word2 = random.randint(0, 15)
    inst0_read2 = shared_address((inst0_tag2 << (n_set.bit_length() + 4 + 2)) | (inst0_set2 << 6) | (inst0_word2 << 2))
    inst0_word3 = random.randint(0, 15)
    inst0_read3 = shared_address((inst0_tag2 << (n_set.bit_length() + 4 + 2)) | (inst0_set2 << 6) | (inst0_word3 << 2))
    inst1_word = random.randint(0, 15)
    inst1_write = shared_address((inst0_tag1 << (n_set.bit_length() + 4 + 2)) | (inst0_set1 << 6) | (inst1_word << 2))
    inst1_data = f"0x{random.randint(0, 2**32-1):08x}"
    with open(inst0_path, "w") as file_inst0: file_inst0.write(f"read\t0x{inst0_read1:08x}\nread\t0x{inst0_read2:08x}\nread\t0x{inst0_read3:08x}\n")
    with open(inst1_path, "w") as file_inst1: file_inst1.write(f"write\t0x{inst1_write:08x}\t{inst1_data}\n")
    blocks = {block_address(inst0_read1), block_address(inst0_read2), block_address(inst0_read3)}
    with open(mem_data_path, "w") as file_mem:
        for block in blocks: file_mem.write(f"0x{block:08x}\t" + "\t".join(f"0x{random.randint(0, 2**32-1):08x}" for _ in range(16)) + "\n")
    print("Testcase 92 created")
def testcase_93(n_set=16):
    base_path="subsystem_testcase/testcase_93/"
    os.makedirs(base_path,exist_ok=True)
    path_inst0=os.path.join(base_path,"instr_mem_A.mem")
    path_inst1=os.path.join(base_path,"instr_mem_B.mem")
    path_mem=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(n_set.bit_length()+4+2)
    def shared_address(addr): return (addr & 0x3FFFF)|0x20000
    def block_address(addr): return addr & 0xFFFFFFC0
    inst0_set1=random.randint(0,n_set-1)
    inst0_tag1=random.randint(0,(1<<tag_bits)-1)
    inst0_word1=random.randint(0,15)
    inst0_read1=shared_address((inst0_tag1<<(n_set.bit_length()+4+2))|(inst0_set1<<6)|(inst0_word1<<2))
    inst0_set2=random.randint(0,n_set-1)
    inst0_tag2=random.randint(0,(1<<tag_bits)-1)
    inst0_word2=random.randint(0,15)
    inst0_read2=shared_address((inst0_tag2<<(n_set.bit_length()+4+2))|(inst0_set2<<6)|(inst0_word2<<2))
    inst0_word3=random.randint(0,15)
    inst0_read3=shared_address((inst0_tag2<<(n_set.bit_length()+4+2))|(inst0_set2<<6)|(inst0_word3<<2))
    inst1_set=random.randint(0,n_set-1)
    while True:
        inst1_tag=random.randint(0,(1<<tag_bits)-1)
        if inst1_tag!=inst0_tag1 and inst1_tag!=inst0_tag2: break
    inst1_word=random.randint(0,15)
    inst1_write=shared_address((inst1_tag<<(n_set.bit_length()+4+2))|(inst1_set<<6)|(inst1_word<<2))
    inst1_data=f"0x{random.randint(0,2**32-1):08x}"
    with open(path_inst0,"w") as f_inst0: f_inst0.write(f"read\t0x{inst0_read1:08x}\nread\t0x{inst0_read2:08x}\nread\t0x{inst0_read3:08x}\n")
    with open(path_inst1,"w") as f_inst1: f_inst1.write(f"write\t0x{inst1_write:08x}\t{inst1_data}\n")
    blocks={block_address(inst0_read1),block_address(inst0_read2),block_address(inst0_read3)}
    with open(path_mem,"w") as f_mem:
        for block in blocks: f_mem.write(f"0x{block:08x}\t"+"\t".join(f"0x{random.randint(0,2**32-1):08x}" for _ in range(16))+"\n")
    print("Testcase 93 created")
def testcase_94(n_set=16):
    base_path = "subsystem_testcase/testcase_94/"
    os.makedirs(base_path, exist_ok=True)
    inst0_path = os.path.join(base_path, "instr_mem_A.mem")
    inst1_path = os.path.join(base_path, "instr_mem_B.mem")
    mem_data_path = os.path.join(base_path, "main_memory_init.mem")
    tag_bits = 32 - (n_set.bit_length() + 4 + 2)
    def shared_address(addr): return (addr & 0x3FFFF) | 0x20000
    def block_address(addr): return addr & 0xFFFFFFC0
    tagA = random.randint(0, (1 << tag_bits) - 1)
    setA = random.randint(0, n_set - 1)
    wordA = random.randint(0, 15)
    inst0_read1 = shared_address((tagA << (n_set.bit_length() + 4 + 2)) | (setA << 6) | (wordA << 2))
    tagB = random.randint(0, (1 << tag_bits) - 1)
    setB = random.randint(0, n_set - 1)
    wordB = random.randint(0, 15)
    inst0_read2 = shared_address((tagB << (n_set.bit_length() + 4 + 2)) | (setB << 6) | (wordB << 2))
    wordB2 = random.randint(0, 15)
    inst0_write = shared_address((tagB << (n_set.bit_length() + 4 + 2)) | (setB << 6) | (wordB2 << 2))
    inst0_write_data = f"0x{random.randint(0, 2**32-1):08x}"
    wordA2 = random.randint(0, 15)
    inst1_read = shared_address((tagA << (n_set.bit_length() + 4 + 2)) | (setA << 6) | (wordA2 << 2))
    with open(inst0_path, "w") as f0:
        f0.write(f"read\t0x{inst0_read1:08x}\nread\t0x{inst0_read2:08x}\nwrite\t0x{inst0_write:08x}\t{inst0_write_data}\n")
    with open(inst1_path, "w") as f1:
        f1.write(f"read\t0x{inst1_read:08x}\n")
    blocks = {block_address(inst0_read1), block_address(inst0_read2), block_address(inst0_write)}
    with open(mem_data_path, "w") as fmem:
        for block in blocks:
            data_words = [f"0x{random.randint(0, 2**32-1):08x}" for _ in range(16)]
            fmem.write(f"0x{block:08x}\t" + "\t".join(data_words) + "\n")
    print("Testcase 94 created")
def testcase_95(n_set=16):
    base_path="subsystem_testcase/testcase_95/"
    os.makedirs(base_path,exist_ok=True)
    inst0_path=os.path.join(base_path,"instr_mem_A.mem")
    inst1_path=os.path.join(base_path,"instr_mem_B.mem")
    mem_data_path=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(n_set.bit_length()+4+2)
    def shared_address(address): return (address & 0x3FFFF)|0x20000
    def block_address(address): return address & 0xFFFFFFC0
    inst0_set1=random.randint(0,n_set-1)
    inst0_tag1=random.randint(0,(1<<tag_bits)-1)
    inst0_word1=random.randint(0,15)
    inst0_read1=shared_address((inst0_tag1<<(n_set.bit_length()+4+2))|(inst0_set1<<6)|(inst0_word1<<2))
    inst0_set2=random.randint(0,n_set-1)
    inst0_tag2=random.randint(0,(1<<tag_bits)-1)
    inst0_word2=random.randint(0,15)
    inst0_read2=shared_address((inst0_tag2<<(n_set.bit_length()+4+2))|(inst0_set2<<6)|(inst0_word2<<2))
    inst0_word3=random.randint(0,15)
    inst0_write=shared_address((inst0_tag2<<(n_set.bit_length()+4+2))|(inst0_set2<<6)|(inst0_word3<<2))
    inst0_write_data=f"0x{random.randint(0,2**32-1):08x}"
    while True:
        inst1_set=random.randint(0,n_set-1)
        if inst1_set!=inst0_set1 and inst1_set!=inst0_set2: break
    inst1_tag=random.randint(0,(1<<tag_bits)-1)
    inst1_word=random.randint(0,15)
    inst1_read=shared_address((inst1_tag<<(n_set.bit_length()+4+2))|(inst1_set<<6)|(inst1_word<<2))
    with open(inst0_path,"w") as file_inst0: file_inst0.write(f"read\t0x{inst0_read1:08x}\nread\t0x{inst0_read2:08x}\nwrite\t0x{inst0_write:08x}\t{inst0_write_data}\n")
    with open(inst1_path,"w") as file_inst1: file_inst1.write(f"read\t0x{inst1_read:08x}\n")
    blocks={block_address(inst0_read1),block_address(inst0_read2),block_address(inst0_write),block_address(inst1_read)}
    with open(mem_data_path,"w") as file_mem:
        for block in blocks: file_mem.write(f"0x{block:08x}\t"+"\t".join(f"0x{random.randint(0,2**32-1):08x}" for _ in range(16))+"\n")
    print("Testcase 95 created")
def testcase_96(n_set=16):
    base_path="subsystem_testcase/testcase_96/"
    os.makedirs(base_path,exist_ok=True)
    inst0_path=os.path.join(base_path,"instr_mem_A.mem")
    inst1_path=os.path.join(base_path,"instr_mem_B.mem")
    mem_data_path=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(n_set.bit_length()+4+2)
    def shared_address(address): return (address & 0x3FFFF)|0x20000
    def block_address(address): return address & 0xFFFFFFC0
    inst0_set1=random.randint(0,n_set-1)
    inst0_tag1=random.randint(0,(1<<tag_bits)-1)
    inst0_word1=random.randint(0,15)
    inst0_read1=shared_address((inst0_tag1<<(n_set.bit_length()+4+2))|(inst0_set1<<6)|(inst0_word1<<2))
    inst0_set2=random.randint(0,n_set-1)
    inst0_tag2=random.randint(0,(1<<tag_bits)-1)
    inst0_word2=random.randint(0,15)
    inst0_read2=shared_address((inst0_tag2<<(n_set.bit_length()+4+2))|(inst0_set2<<6)|(inst0_word2<<2))
    inst0_word_write=random.randint(0,15)
    inst0_write=shared_address((inst0_tag2<<(n_set.bit_length()+4+2))|(inst0_set2<<6)|(inst0_word_write<<2))
    inst0_write_data=f"0x{random.randint(0,2**32-1):08x}"
    inst1_word=random.randint(0,15)
    inst1_write=shared_address((inst0_tag1<<(n_set.bit_length()+4+2))|(inst0_set1<<6)|(inst1_word<<2))
    inst1_write_data=f"0x{random.randint(0,2**32-1):08x}"
    with open(inst0_path,"w") as f0: f0.write(f"read\t0x{inst0_read1:08x}\nread\t0x{inst0_read2:08x}\nwrite\t0x{inst0_write:08x}\t{inst0_write_data}\n")
    with open(inst1_path,"w") as f1: f1.write(f"write\t0x{inst1_write:08x}\t{inst1_write_data}\n")
    blocks={block_address(inst0_read1),block_address(inst0_read2),block_address(inst0_write)}
    with open(mem_data_path,"w") as fm:
        for blk in blocks: fm.write(f"0x{blk:08x}\t"+"\t".join(f"0x{random.randint(0,2**32-1):08x}" for _ in range(16))+"\n")
    print("Testcase 96 created")
def testcase_97(n_set=16):
    base_path="subsystem_testcase/testcase_97/"
    os.makedirs(base_path,exist_ok=True)
    inst0_path=os.path.join(base_path,"instr_mem_A.mem")
    inst1_path=os.path.join(base_path,"instr_mem_B.mem")
    mem_data_path=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(n_set.bit_length()+4+2)
    def shared_address(address): return (address & 0x3FFFF)|0x20000
    def block_address(address): return address & 0xFFFFFFC0
    inst0_set1=random.randint(0,n_set-1)
    inst0_tag1=random.randint(0,(1<<tag_bits)-1)
    inst0_word1=random.randint(0,15)
    inst0_read1=shared_address((inst0_tag1<<(n_set.bit_length()+4+2))|(inst0_set1<<6)|(inst0_word1<<2))
    inst0_set2=random.randint(0,n_set-1)
    inst0_tag2=random.randint(0,(1<<tag_bits)-1)
    inst0_word2=random.randint(0,15)
    inst0_read2=shared_address((inst0_tag2<<(n_set.bit_length()+4+2))|(inst0_set2<<6)|(inst0_word2<<2))
    inst0_word_write=random.randint(0,15)
    inst0_write=shared_address((inst0_tag2<<(n_set.bit_length()+4+2))|(inst0_set2<<6)|(inst0_word_write<<2))
    inst0_write_data=f"0x{random.randint(0,2**32-1):08x}"
    while True:
        inst1_set=random.randint(0,n_set-1)
        if inst1_set!=inst0_set1 and inst1_set!=inst0_set2: break
    inst1_tag=random.randint(0,(1<<tag_bits)-1)
    inst1_word=random.randint(0,15)
    inst1_write=shared_address((inst1_tag<<(n_set.bit_length()+4+2))|(inst1_set<<6)|(inst1_word<<2))
    inst1_write_data=f"0x{random.randint(0,2**32-1):08x}"
    with open(inst0_path,"w") as f0: f0.write(f"read\t0x{inst0_read1:08x}\nread\t0x{inst0_read2:08x}\nwrite\t0x{inst0_write:08x}\t{inst0_write_data}\n")
    with open(inst1_path,"w") as f1: f1.write(f"write\t0x{inst1_write:08x}\t{inst1_write_data}\n")
    blocks={block_address(inst0_read1),block_address(inst0_read2),block_address(inst0_write),block_address(inst1_write)}
    with open(mem_data_path,"w") as fm:
        for block in blocks: fm.write(f"0x{block:08x}\t"+"\t".join(f"0x{random.randint(0,2**32-1):08x}" for _ in range(16))+"\n")
    print("Testcase 97 created")
def testcase_98(n_set=16):
    base_path = "subsystem_testcase/testcase_98/"
    os.makedirs(base_path, exist_ok=True)
    inst0_path = os.path.join(base_path, "instr_mem_A.mem")
    inst1_path = os.path.join(base_path, "instr_mem_B.mem")
    mem_data_path = os.path.join(base_path, "main_memory_init.mem")
    tag_bits = 32 - (n_set.bit_length() + 4 + 2)
    def shared_address(address): return (address & 0x3FFFF) | 0x20000
    def block_address(address): return address & 0xFFFFFFC0
    set_read0 = random.randint(0, n_set - 1)
    tag_read0 = random.randint(0, (1 << tag_bits) - 1)
    word_read0 = random.randint(0, 15)
    inst0_read0 = shared_address((tag_read0 << (n_set.bit_length() + 4 + 2)) | (set_read0 << 6) | (word_read0 << 2))
    while True:
        set_write = random.randint(0, n_set - 1)
        if set_write != set_read0:
            break
    write_tags = []
    inst0_writes = []
    for _ in range(4):
        tag_write = random.randint(0, (1 << tag_bits) - 1)
        write_tags.append(tag_write)
        word_write = random.randint(0, 15)
        inst0_writes.append(shared_address((tag_write << (n_set.bit_length() + 4 + 2)) | (set_write << 6) | (word_write << 2)))
    while True:
        tag_read_last = random.randint(0, (1 << tag_bits) - 1)
        if tag_read_last not in write_tags:
            break
    word_read_last = random.randint(0, 15)
    inst0_read_last = shared_address((tag_read_last << (n_set.bit_length() + 4 + 2)) | (set_write << 6) | (word_read_last << 2))
    word_inst1 = random.randint(0, 15)
    inst1_read = shared_address((tag_read0 << (n_set.bit_length() + 4 + 2)) | (set_read0 << 6) | (word_inst1 << 2))
    with open(inst0_path, "w") as f0:
        f0.write(f"read\t0x{inst0_read0:08x}\n")
        for write_inst in inst0_writes:
            f0.write(f"write\t0x{write_inst:08x}\t0x{random.randint(0,2**32-1):08x}\n")
        f0.write(f"read\t0x{inst0_read_last:08x}\n")
    with open(inst1_path, "w") as f1:
        f1.write(f"read\t0x{inst1_read:08x}\n")
    blocks = set([block_address(inst0_read0), block_address(inst0_read_last)] + [block_address(x) for x in inst0_writes])
    with open(mem_data_path, "w") as fmem:
        for blk in blocks:
            fmem.write(f"0x{blk:08x}\t" + "\t".join(f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)) + "\n")
    print("Testcase 98 created")
def testcase_99(n_set=16):
    base_path = "subsystem_testcase/testcase_99/"
    os.makedirs(base_path, exist_ok=True)
    inst0_path = os.path.join(base_path, "instr_mem_A.mem")
    inst1_path = os.path.join(base_path, "instr_mem_B.mem")
    mem_data_path = os.path.join(base_path, "main_memory_init.mem")
    tag_bits = 32 - (n_set.bit_length() + 4 + 2)
    def shared_address(address): return (address & 0x3FFFF) | 0x20000
    def block_address(address): return address & 0xFFFFFFC0
    read_set = random.randint(0, n_set - 1)
    read_tag = random.randint(0, (1 << tag_bits) - 1)
    read_word = random.randint(0, 15)
    inst0_read0 = shared_address((read_tag << (n_set.bit_length() + 4 + 2)) | (read_set << 6) | (read_word << 2))
    while True:
        write_set = random.randint(0, n_set - 1)
        if write_set != read_set: break
    write_instructions = []
    write_tags = []
    for _ in range(4):
        write_tag = random.randint(0, (1 << tag_bits) - 1)
        write_tags.append(write_tag)
        write_word = random.randint(0, 15)
        inst0_write = shared_address((write_tag << (n_set.bit_length() + 4 + 2)) | (write_set << 6) | (write_word << 2))
        write_instructions.append((inst0_write, f"0x{random.randint(0,2**32-1):08x}"))
    while True:
        final_read_tag = random.randint(0, (1 << tag_bits) - 1)
        if final_read_tag not in write_tags: break
    final_read_word = random.randint(0, 15)
    inst0_final_read = shared_address((final_read_tag << (n_set.bit_length() + 4 + 2)) | (write_set << 6) | (final_read_word << 2))
    while True:
        inst1_set = random.randint(0, n_set - 1)
        if inst1_set != read_set and inst1_set != write_set: break
    inst1_tag = random.randint(0, (1 << tag_bits) - 1)
    inst1_word = random.randint(0, 15)
    inst1_read = shared_address((inst1_tag << (n_set.bit_length() + 4 + 2)) | (inst1_set << 6) | (inst1_word << 2))
    with open(inst0_path, "w") as f0:
        f0.write(f"read\t0x{inst0_read0:08x}\n")
        for write_inst, data in write_instructions:
            f0.write(f"write\t0x{write_inst:08x}\t{data}\n")
        f0.write(f"read\t0x{inst0_final_read:08x}\n")
    with open(inst1_path, "w") as f1:
        f1.write(f"read\t0x{inst1_read:08x}\n")
    all_blocks = {block_address(inst0_read0), block_address(inst0_final_read), block_address(inst1_read)}
    for write_inst, _ in write_instructions:
        all_blocks.add(block_address(write_inst))
    with open(mem_data_path, "w") as fm:
        for block in all_blocks:
            fm.write(f"0x{block:08x}\t" + "\t".join(f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)) + "\n")
    print("Testcase 99 created")
def testcase_100(n_set=16):
    base_path="subsystem_testcase/testcase_100/";os.makedirs(base_path,exist_ok=True)
    inst0_path=os.path.join(base_path,"instr_mem_A.mem");inst1_path=os.path.join(base_path,"instr_mem_B.mem");mem_data_path=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(n_set.bit_length()+4+2)
    def shared_address(address): return (address & 0x3FFFF)|0x20000
    def block_address(address): return address & 0xFFFFFFC0
    read_set=random.randint(0,n_set-1)
    read_tag=random.randint(0,(1<<tag_bits)-1)
    read_word=random.randint(0,15)
    inst0_read0=shared_address((read_tag<<(n_set.bit_length()+4+2))|(read_set<<6)|(read_word<<2))
    while True:
        write_set=random.randint(0,n_set-1)
        if write_set!=read_set: break
    write_insts=[];write_tags=[]
    for _ in range(4):
        tag_write=random.randint(0,(1<<tag_bits)-1)
        write_tags.append(tag_write)
        word_write=random.randint(0,15)
        addr_write=shared_address((tag_write<<(n_set.bit_length()+4+2))|(write_set<<6)|(word_write<<2))
        data_write=f"0x{random.randint(0,2**32-1):08x}"
        write_insts.append((addr_write,data_write))
    while True:
        final_read_tag=random.randint(0,(1<<tag_bits)-1)
        if final_read_tag not in write_tags: break
    final_read_word=random.randint(0,15)
    inst0_final_read=shared_address((final_read_tag<<(n_set.bit_length()+4+2))|(write_set<<6)|(final_read_word<<2))
    inst1_word=random.randint(0,15)
    inst1_write=shared_address((read_tag<<(n_set.bit_length()+4+2))|(read_set<<6)|(inst1_word<<2))
    inst1_write_data=f"0x{random.randint(0,2**32-1):08x}"
    with open(inst0_path,"w") as f0:
        f0.write(f"read\t0x{inst0_read0:08x}\n")
        for addr,data in write_insts:
            f0.write(f"write\t0x{addr:08x}\t{data}\n")
        f0.write(f"read\t0x{inst0_final_read:08x}\n")
    with open(inst1_path,"w") as f1:
        f1.write(f"write\t0x{inst1_write:08x}\t{inst1_write_data}\n")
    blocks={block_address(inst0_read0),block_address(inst0_final_read)}
    for addr,data in write_insts:
        blocks.add(block_address(addr))
    with open(mem_data_path,"w") as fmem:
        for blk in blocks: fmem.write(f"0x{blk:08x}\t"+"\t".join(f"0x{random.randint(0,2**32-1):08x}" for _ in range(16))+"\n")
    print("Testcase 100 created")
def testcase_101(n_set=16):
    base_path="subsystem_testcase/testcase_101/"
    os.makedirs(base_path,exist_ok=True)
    inst0_path=os.path.join(base_path,"instr_mem_A.mem")
    inst1_path=os.path.join(base_path,"instr_mem_B.mem")
    mem_data_path=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(n_set.bit_length()+4+2)
    def shared_address(address): return (address & 0x3FFFF)|0x20000
    def block_address(address): return address & 0xFFFFFFC0
    read_set=random.randint(0,n_set-1)
    read_tag=random.randint(0,(1<<tag_bits)-1)
    read_word=random.randint(0,15)
    inst0_read0=shared_address((read_tag<<(n_set.bit_length()+4+2))|(read_set<<6)|(read_word<<2))
    while True:
        write_set=random.randint(0,n_set-1)
        if write_set!=read_set: break
    write_insts=[]
    write_tags=[]
    for _ in range(4):
        w_tag=random.randint(0,(1<<tag_bits)-1)
        write_tags.append(w_tag)
        w_word=random.randint(0,15)
        addr=shared_address((w_tag<<(n_set.bit_length()+4+2))|(write_set<<6)|(w_word<<2))
        data=f"0x{random.randint(0,2**32-1):08x}"
        write_insts.append((addr,data))
    while True:
        final_read_tag=random.randint(0,(1<<tag_bits)-1)
        if final_read_tag not in write_tags: break
    final_read_word=random.randint(0,15)
    inst0_final_read=shared_address((final_read_tag<<(n_set.bit_length()+4+2))|(write_set<<6)|(final_read_word<<2))
    while True:
        inst1_set=random.randint(0,n_set-1)
        if inst1_set!=read_set and inst1_set!=write_set: break
    inst1_tag=random.randint(0,(1<<tag_bits)-1)
    inst1_word=random.randint(0,15)
    inst1_write=shared_address((inst1_tag<<(n_set.bit_length()+4+2))|(inst1_set<<6)|(inst1_word<<2))
    inst1_data=f"0x{random.randint(0,2**32-1):08x}"
    with open(inst0_path,"w") as f0:
        f0.write(f"read\t0x{inst0_read0:08x}\n")
        for addr,data in write_insts:
            f0.write(f"write\t0x{addr:08x}\t{data}\n")
        f0.write(f"read\t0x{inst0_final_read:08x}\n")
    with open(inst1_path,"w") as f1:
        f1.write(f"write\t0x{inst1_write:08x}\t{inst1_data}\n")
    blocks=set([block_address(inst0_read0),block_address(inst0_final_read),block_address(inst1_write)])
    for addr,_ in write_insts:
        blocks.add(block_address(addr))
    with open(mem_data_path,"w") as fmem:
        for blk in blocks:
            fmem.write(f"0x{blk:08x}\t"+"\t".join(f"0x{random.randint(0,2**32-1):08x}" for _ in range(16))+"\n")
    print("Testcase 101 created")
def testcase_102(n_set=16):
    base_path="subsystem_testcase/testcase_102/"
    os.makedirs(base_path,exist_ok=True)
    inst0_path=os.path.join(base_path,"instr_mem_A.mem")
    inst1_path=os.path.join(base_path,"instr_mem_B.mem")
    mem_data_path=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(n_set.bit_length()+4+2)
    def shared_address(address): return (address & 0x3FFFF)|0x20000
    def block_address(address): return address & 0xFFFFFFC0
    read_set=random.randint(0,n_set-1)
    read_tag=random.randint(0,(1<<tag_bits)-1)
    read_word=random.randint(0,15)
    inst0_read0=shared_address((read_tag<<(n_set.bit_length()+4+2))|(read_set<<6)|(read_word<<2))
    while True:
        write_set=random.randint(0,n_set-1)
        if write_set!=read_set: break
    write_insts=[]
    write_tags=[]
    for _ in range(4):
        tag_write=random.randint(0,(1<<tag_bits)-1)
        write_tags.append(tag_write)
        write_word=random.randint(0,15)
        addr_write=shared_address((tag_write<<(n_set.bit_length()+4+2))|(write_set<<6)|(write_word<<2))
        data_write=f"0x{random.randint(0,2**32-1):08x}"
        write_insts.append((addr_write,data_write))
    while True:
        final_write_tag=random.randint(0,(1<<tag_bits)-1)
        if final_write_tag not in write_tags: break
    final_write_word=random.randint(0,15)
    inst0_final_write=shared_address((final_write_tag<<(n_set.bit_length()+4+2))|(write_set<<6)|(final_write_word<<2))
    final_write_data=f"0x{random.randint(0,2**32-1):08x}"
    inst1_word=random.randint(0,15)
    inst1_read=shared_address((read_tag<<(n_set.bit_length()+4+2))|(read_set<<6)|(inst1_word<<2))
    with open(inst0_path,"w") as f0:
        f0.write(f"read\t0x{inst0_read0:08x}\n")
        for addr,data in write_insts:
            f0.write(f"write\t0x{addr:08x}\t{data}\n")
        f0.write(f"write\t0x{inst0_final_write:08x}\t{final_write_data}\n")
    with open(inst1_path,"w") as f1:
        f1.write(f"read\t0x{inst1_read:08x}\n")
    blocks={block_address(inst0_read0),block_address(inst0_final_write)}
    for addr,_ in write_insts:
        blocks.add(block_address(addr))
    with open(mem_data_path,"w") as fmem:
        for block in blocks:
            data_words="\t".join(f"0x{random.randint(0,2**32-1):08x}" for _ in range(16))
            fmem.write(f"0x{block:08x}\t{data_words}\n")
    print("Testcase 102 created")
def testcase_103(n_set=16):
    base_path="subsystem_testcase/testcase_103/"
    os.makedirs(base_path,exist_ok=True)
    inst0_path=os.path.join(base_path,"instr_mem_A.mem")
    inst1_path=os.path.join(base_path,"instr_mem_B.mem")
    mem_data_path=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(n_set.bit_length()+4+2)
    def shared_address(addr): return (addr & 0x3FFFF)|0x20000
    def block_address(addr): return addr & 0xFFFFFFC0
    read_set=random.randint(0,n_set-1)
    read_tag=random.randint(0,(1<<tag_bits)-1)
    read_word=random.randint(0,15)
    inst0_read=shared_address((read_tag<<(n_set.bit_length()+4+2))|(read_set<<6)|(read_word<<2))
    while True:
        write_set=random.randint(0,n_set-1)
        if write_set!=read_set: break
    write_insts=[]
    write_tags=[]
    for _ in range(4):
        w_tag=random.randint(0,(1<<tag_bits)-1)
        write_tags.append(w_tag)
        w_word=random.randint(0,15)
        addr=shared_address((w_tag<<(n_set.bit_length()+4+2))|(write_set<<6)|(w_word<<2))
        data=f"0x{random.randint(0,2**32-1):08x}"
        write_insts.append((addr,data))
    while True:
        extra_write_tag=random.randint(0,(1<<tag_bits)-1)
        if extra_write_tag not in write_tags: break
    extra_write_word=random.randint(0,15)
    inst0_extra_write=shared_address((extra_write_tag<<(n_set.bit_length()+4+2))|(write_set<<6)|(extra_write_word<<2))
    extra_write_data=f"0x{random.randint(0,2**32-1):08x}"
    while True:
        inst1_set=random.randint(0,n_set-1)
        if inst1_set!=read_set and inst1_set!=write_set: break
    inst1_tag=random.randint(0,(1<<tag_bits)-1)
    inst1_word=random.randint(0,15)
    inst1_read=shared_address((inst1_tag<<(n_set.bit_length()+4+2))|(inst1_set<<6)|(inst1_word<<2))
    with open(inst0_path,"w") as f0:
        f0.write(f"read\t0x{inst0_read:08x}\n")
        for addr,data in write_insts:
            f0.write(f"write\t0x{addr:08x}\t{data}\n")
        f0.write(f"write\t0x{inst0_extra_write:08x}\t{extra_write_data}\n")
    with open(inst1_path,"w") as f1:
        f1.write(f"read\t0x{inst1_read:08x}\n")
    blocks=set([block_address(inst0_read),block_address(inst0_extra_write),block_address(inst1_read)])
    for addr,_ in write_insts:
        blocks.add(block_address(addr))
    with open(mem_data_path,"w") as fmem:
        for blk in blocks:
            fmem.write(f"0x{blk:08x}\t"+"\t".join(f"0x{random.randint(0,2**32-1):08x}" for _ in range(16))+"\n")
    print("Testcase 103 created")
def testcase_104(n_set=16):
    base_path="subsystem_testcase/testcase_104/"; os.makedirs(base_path, exist_ok=True)
    inst0_path=os.path.join(base_path,"instr_mem_A.mem"); inst1_path=os.path.join(base_path,"instr_mem_B.mem"); mem_data_path=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(n_set.bit_length()+4+2)
    def shared_address(addr): return (addr & 0x3FFFF)|0x20000
    def block_address(addr): return addr & 0xFFFFFFC0
    read_set=random.randint(0,n_set-1)
    read_tag=random.randint(0,(1<<tag_bits)-1)
    read_word=random.randint(0,15)
    inst0_read=shared_address((read_tag<<(n_set.bit_length()+4+2))|(read_set<<6)|(read_word<<2))
    while True:
        write_set=random.randint(0,n_set-1)
        if write_set!=read_set: break
    write_insts=[]; write_tags=[]
    for _ in range(4):
        w_tag=random.randint(0,(1<<tag_bits)-1)
        write_tags.append(w_tag)
        w_word=random.randint(0,15)
        addr=shared_address((w_tag<<(n_set.bit_length()+4+2))|(write_set<<6)|(w_word<<2))
        data=f"0x{random.randint(0,2**32-1):08x}"
        write_insts.append((addr,data))
    while True:
        extra_tag=random.randint(0,(1<<tag_bits)-1)
        if extra_tag not in write_tags: break
    extra_word=random.randint(0,15)
    inst0_extra_write=shared_address((extra_tag<<(n_set.bit_length()+4+2))|(write_set<<6)|(extra_word<<2))
    extra_data=f"0x{random.randint(0,2**32-1):08x}"
    inst1_word=random.randint(0,15)
    inst1_write=shared_address((read_tag<<(n_set.bit_length()+4+2))|(read_set<<6)|(inst1_word<<2))
    inst1_data=f"0x{random.randint(0,2**32-1):08x}"
    with open(inst0_path,"w") as f0:
        f0.write(f"read\t0x{inst0_read:08x}\n")
        for addr,data in write_insts:
            f0.write(f"write\t0x{addr:08x}\t{data}\n")
        f0.write(f"write\t0x{inst0_extra_write:08x}\t{extra_data}\n")
    with open(inst1_path,"w") as f1:
        f1.write(f"write\t0x{inst1_write:08x}\t{inst1_data}\n")
    blocks=set([block_address(inst0_read),block_address(inst0_extra_write)])
    for addr,_ in write_insts: blocks.add(block_address(addr))
    with open(mem_data_path,"w") as fm:
        for blk in blocks:
            fm.write(f"0x{blk:08x}\t"+"\t".join(f"0x{random.randint(0,2**32-1):08x}" for _ in range(16))+"\n")
    print("Testcase 104 created")
def testcase_105(n_set=16):
    base_path="subsystem_testcase/testcase_105/"; os.makedirs(base_path, exist_ok=True)
    inst0_path=os.path.join(base_path,"instr_mem_A.mem"); inst1_path=os.path.join(base_path,"instr_mem_B.mem"); mem_data_path=os.path.join(base_path,"main_memory_init.mem")
    tag_bits=32-(n_set.bit_length()+4+2)
    def shared_address(addr): return (addr & 0x3FFFF)|0x20000
    def block_address(addr): return addr & 0xFFFFFFC0
    read_set=random.randint(0,n_set-1)
    read_tag=random.randint(0,(1<<tag_bits)-1)
    read_word=random.randint(0,15)
    inst0_read=shared_address((read_tag<<(n_set.bit_length()+4+2))|(read_set<<6)|(read_word<<2))
    while True:
        write_set=random.randint(0,n_set-1)
        if write_set!=read_set: break
    write_insts=[]; write_tags=[]
    for _ in range(4):
        write_tag=random.randint(0,(1<<tag_bits)-1)
        write_tags.append(write_tag)
        write_word=random.randint(0,15)
        addr=shared_address((write_tag<<(n_set.bit_length()+4+2))|(write_set<<6)|(write_word<<2))
        data=f"0x{random.randint(0,2**32-1):08x}"
        write_insts.append((addr,data))
    while True:
        extra_write_tag=random.randint(0,(1<<tag_bits)-1)
        if extra_write_tag not in write_tags: break
    extra_write_word=random.randint(0,15)
    inst0_extra_write=shared_address((extra_write_tag<<(n_set.bit_length()+4+2))|(write_set<<6)|(extra_write_word<<2))
    extra_write_data=f"0x{random.randint(0,2**32-1):08x}"
    while True:
        inst1_set=random.randint(0,n_set-1)
        if inst1_set!=read_set and inst1_set!=write_set: break
    inst1_tag=random.randint(0,(1<<tag_bits)-1)
    inst1_word=random.randint(0,15)
    inst1_write=shared_address((inst1_tag<<(n_set.bit_length()+4+2))|(inst1_set<<6)|(inst1_word<<2))
    inst1_data=f"0x{random.randint(0,2**32-1):08x}"
    with open(inst0_path,"w") as f0:
        f0.write(f"read\t0x{inst0_read:08x}\n")
        for addr,data in write_insts:
            f0.write(f"write\t0x{addr:08x}\t{data}\n")
        f0.write(f"write\t0x{inst0_extra_write:08x}\t{extra_write_data}\n")
    with open(inst1_path,"w") as f1:
        f1.write(f"write\t0x{inst1_write:08x}\t{inst1_data}\n")
    blocks=set([block_address(inst0_read), block_address(inst0_extra_write), block_address(inst1_write)])
    for addr,_ in write_insts:
        blocks.add(block_address(addr))
    with open(mem_data_path,"w") as fm:
        for blk in blocks:
            fm.write(f"0x{blk:08x}\t"+"\t".join(f"0x{random.randint(0,2**32-1):08x}" for _ in range(16))+"\n")
    print("Testcase 105 created")
def testcase_106(n_set=16):
    base_path = "subsystem_testcase/testcase_106/"
    os.makedirs(base_path, exist_ok=True)
    path_0 = os.path.join(base_path, "instr_mem_A.mem")
    path_1 = os.path.join(base_path, "instr_mem_B.mem")
    path_mem = os.path.join(base_path, "main_memory_init.mem")

    # Số bit tag = 32 - (log2(n_set) + 4 + 2) nhưng ta chỉ cần 7 bit tag (0..127) để không vượt 0x3FFFF
    # Layout addr: 0x20000 + (tag << 10) + (set << 6) + (word_offset << 2)

    tag_limit = 128  # Đảm bảo không vượt 0x3FFFF
    def block_addr(a): return a & 0xFFFFFFC0

    # 1) Chọn set duy nhất
    chosen_set = random.randint(0, n_set - 1)

    # 2) Tạo 8 tag duy nhất cho 8 lệnh write
    all_8_tags = random.sample(range(tag_limit), 8)

    # 3) Chia 8 tag -> 4 cho inst_0, 4 cho inst_1
    tags_inst0 = all_8_tags[:4]
    tags_inst1 = all_8_tags[4:]

    # 4) Tạo 4 lệnh write inst_0
    writes_inst0 = []
    for t in tags_inst0:
        wofs = random.randint(0, 15)
        addr = 0x00020000 + (t << 10) + (chosen_set << 6) + (wofs << 2)
        data = f"0x{random.randint(0, 2**32 - 1):08x}"
        writes_inst0.append((addr, data))

    # 5) Tạo 4 lệnh write inst_1
    writes_inst1 = []
    for t in tags_inst1:
        wofs = random.randint(0, 15)
        addr = 0x00020000 + (t << 10) + (chosen_set << 6) + (wofs << 2)
        data = f"0x{random.randint(0, 2**32 - 1):08x}"
        writes_inst1.append((addr, data))

    # 6) Tạo 1 tag dành cho 2 lệnh read (chắc chắn khác 8 tag trên)
    while True:
        read_tag = random.randint(0, tag_limit - 1)
        if read_tag not in all_8_tags:
            break

    # Tạo read cho inst_0
    rd_word_0 = random.randint(0, 15)
    read_addr_0 = 0x00020000 + (read_tag << 10) + (chosen_set << 6) + (rd_word_0 << 2)

    # Tạo read cho inst_1 (cùng tag, cùng set)
    rd_word_1 = random.randint(0, 15)
    read_addr_1 = 0x00020000 + (read_tag << 10) + (chosen_set << 6) + (rd_word_1 << 2)

    # 7) Ghi file inst_0
    with open(path_0, "w") as f0:
        # 4 write
        for (addr, data) in writes_inst0:
            f0.write(f"write\t0x{addr:08x}\t{data}\n")
        # 1 read
        f0.write(f"read\t0x{read_addr_0:08x}\n")

    # 8) Ghi file inst_1
    with open(path_1, "w") as f1:
        # 4 write
        for (addr, data) in writes_inst1:
            f1.write(f"write\t0x{addr:08x}\t{data}\n")
        # 1 read
        f1.write(f"read\t0x{read_addr_1:08x}\n")

    # 9) Tạo mem_data: cho tất cả địa chỉ (8 writes + 2 reads)
    all_addrs = [x[0] for x in writes_inst0] + [x[0] for x in writes_inst1] + [read_addr_0, read_addr_1]
    blocks = {block_addr(a) for a in all_addrs}

    with open(path_mem, "w") as fm:
        for blk in blocks:
            data_words = [f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            fm.write(f"0x{blk:08x}\t" + "\t".join(data_words) + "\n")

    print("Testcase 106 created")
def testcase_107(n_set=16):  # tạo 4 read khác tag + 4 read trùng tag
    import os,random
    bp="subsystem_testcase/testcase_107/";os.makedirs(bp,exist_ok=True)  # tạo folder
    p0=os.path.join(bp,"instr_mem_A.mem");p1=os.path.join(bp,"instr_mem_B.mem");pm=os.path.join(bp,"main_memory_init.mem")
    tg_lim=128  # giới hạn tag
    def blk(a):return a&0xFFFFFFC0  # block address
    cs=random.randint(0,n_set-1)  # chosen set
    t4=random.sample(range(tg_lim),4)  # 4 tag khác nhau
    r0=[]
    for t in t4:  # 4 lệnh read khác tag
        wofs=random.randint(0,15)
        a=0x20000+(t<<10)+(cs<<6)+(wofs<<2)
        r0.append(a)
    for t in t4:  # 4 lệnh read trùng tag
        wofs=random.randint(0,15)
        a=0x20000+(t<<10)+(cs<<6)+(wofs<<2)
        r0.append(a)
    with open(p0,"w") as f0:  # ghi inst_0
        for a in r0:f0.write(f"read\t0x{a:08x}\n")
    with open(p1,"w"): pass  # inst_1 để trống
    blocks={blk(a)for a in r0}
    with open(pm,"w") as fm:  # mem_data
        for b in blocks:
            d=[f"0x{random.randint(0,2**32-1):08x}"for _ in range(16)]
            fm.write(f"0x{b:08x}\t"+"\t".join(d)+"\n")
    print("Testcase 107 created")
def testcase_108(n_set=16):  # 4 read khác tag + 4 write trùng tag
    import os,random
    bp="subsystem_testcase/testcase_108/";os.makedirs(bp,exist_ok=True)  # folder
    p0=os.path.join(bp,"instr_mem_A.mem");p1=os.path.join(bp,"instr_mem_B.mem");pm=os.path.join(bp,"main_memory_init.mem")
    tg_lim=128  # giới hạn tag
    def blk(a):return a&0xFFFFFFC0
    cs=random.randint(0,n_set-1)  # chosen set
    t4=random.sample(range(tg_lim),4)  # 4 tag cho 4 lệnh read
    reads=[];writes=[]
    for t in t4:  # tạo địa chỉ 4 read
        wofs=random.randint(0,15)
        a=0x20000+(t<<10)+(cs<<6)+(wofs<<2)
        reads.append(a)
    for t in t4:  # tạo địa chỉ 4 write trùng tag
        wofs=random.randint(0,15)
        a=0x20000+(t<<10)+(cs<<6)+(wofs<<2)
        d=f"0x{random.randint(0,2**32-1):08x}"
        writes.append((a,d))
    with open(p0,"w") as f0:
        for a in reads:f0.write(f"read\t0x{a:08x}\n")  # ghi 4 read
        for a,d in writes:f0.write(f"write\t0x{a:08x}\t{d}\n")  # ghi 4 write
    with open(p1,"w"): pass  # inst_1 rỗng
    blocks={blk(a)for a in reads}|{blk(a)for a,_ in writes}
    with open(pm,"w") as fm:
        for b in blocks:
            d=[f"0x{random.randint(0,2**32-1):08x}"for _ in range(16)]
            fm.write(f"0x{b:08x}\t"+"\t".join(d)+"\n")
    print("Testcase 108 created")
def testcase_109(n_set=16):  # 4 read cùng set, khác tag
    import os, random
    bp = "subsystem_testcase/testcase_109/"
    os.makedirs(bp, exist_ok=True)
    p0 = os.path.join(bp, "instr_mem_A.mem")
    p1 = os.path.join(bp, "instr_mem_B.mem")
    pm = os.path.join(bp, "main_memory_init.mem")
    tag_limit = 128  # giới hạn tag để đảm bảo địa chỉ nằm trong 0x20000..0x3FFFF
    def block_addr(a): return a & 0xFFFFFFC0
    chosen_set = random.randint(0, n_set - 1)
    tags_4 = random.sample(range(tag_limit), 4)  # 4 tag khác nhau
    reads = []
    for t in tags_4:
        word_offset = random.randint(0, 15)
        addr = 0x20000 + (t << 10) + (chosen_set << 6) + (word_offset << 2)
        reads.append(addr)
    with open(p0, "w") as f0:
        for a in reads:
            f0.write(f"read\t0x{a:08x}\n")
    with open(p1, "w"): pass
    blocks = {block_addr(a) for a in reads}
    with open(pm, "w") as fm:
        for b in blocks:
            data_line = [f"0x{random.randint(0, 2**32 - 1):08x}" for _ in range(16)]
            fm.write(f"0x{b:08x}\t" + "\t".join(data_line) + "\n")
    print("Testcase 109 created")
def testcase_110(n_set=16):  # 4 write inst_0 + 4 read inst_1, cùng set, tag cặp đôi
    import os, random
    bp = "subsystem_testcase/testcase_110/"
    os.makedirs(bp, exist_ok=True)
    p0 = os.path.join(bp, "instr_mem_A.mem")
    p1 = os.path.join(bp, "instr_mem_B.mem")
    pm = os.path.join(bp, "main_memory_init.mem")
    tag_limit = 128  # giới hạn tag đảm bảo vùng 0x20000..0x3FFFF
    def block_addr(a): return a & 0xFFFFFFC0

    chosen_set = random.randint(0, n_set - 1)  # cùng set
    tags_4 = random.sample(range(tag_limit), 4)  # 4 tag khác nhau

    # Tạo 4 write cho inst_0
    writes_0 = []
    for t in tags_4:
        word_offset = random.randint(0, 15)
        addr = 0x20000 + (t << 10) + (chosen_set << 6) + (word_offset << 2)
        data_val = f"0x{random.randint(0, 2**32 - 1):08x}"
        writes_0.append((addr, data_val))

    # Tạo 4 read cho inst_1 (cùng tag với từng write)
    reads_1 = []
    for t in tags_4:
        word_offset = random.randint(0, 15)
        addr = 0x20000 + (t << 10) + (chosen_set << 6) + (word_offset << 2)
        reads_1.append(addr)

    with open(p0, "w") as f0:
        for (a, d) in writes_0:
            f0.write(f"write\t0x{a:08x}\t{d}\n")

    with open(p1, "w") as f1:
        for a in reads_1:
            f1.write(f"read\t0x{a:08x}\n")

    # Tạo mem_data cho tất cả lệnh trong inst_0
    blocks = {block_addr(a) for (a, _) in writes_0}
    with open(pm, "w") as fm:
        for blk in blocks:
            data_line = [f"0x{random.randint(0, 2**32 - 1):08x}" for _ in range(16)]
            fm.write(f"0x{blk:08x}\t" + "\t".join(data_line) + "\n")

    print("Testcase 110 created")
def testcase_111(n_set=16):  # 4 write (unique tags) + 4 read (unique tags, different from writes)
    import os, random
    bp = "subsystem_testcase/testcase_111/"
    os.makedirs(bp, exist_ok=True)
    p0 = os.path.join(bp, "instr_mem_A.mem")
    p1 = os.path.join(bp, "instr_mem_B.mem")
    pm = os.path.join(bp, "main_memory_init.mem")
    tag_limit = 128
    def block_addr(a): return a & 0xFFFFFFC0

    chosen_set = random.randint(0, n_set - 1)

    # Lấy 8 tag: 4 cho write, 4 cho read
    all_tags_8 = random.sample(range(tag_limit), 8)
    w_tags = all_tags_8[:4]
    r_tags = all_tags_8[4:]

    writes = []
    for t in w_tags:
        word_offset = random.randint(0, 15)
        addr = 0x20000 + (t << 10) + (chosen_set << 6) + (word_offset << 2)
        data_val = f"0x{random.randint(0, 2**32 - 1):08x}"
        writes.append((addr, data_val))

    reads = []
    for t in r_tags:
        word_offset = random.randint(0, 15)
        addr = 0x20000 + (t << 10) + (chosen_set << 6) + (word_offset << 2)
        reads.append(addr)

    with open(p0, "w") as f0:
        for (a, d) in writes:
            f0.write(f"write\t0x{a:08x}\t{d}\n")
        for a in reads:
            f0.write(f"read\t0x{a:08x}\n")

    with open(p1, "w"): pass

    blocks = {block_addr(a) for (a, _) in writes} | {block_addr(a) for a in reads}
    with open(pm, "w") as fm:
        for blk in blocks:
            dline = [f"0x{random.randint(0, 2**32 - 1):08x}" for _ in range(16)]
            fm.write(f"0x{blk:08x}\t" + "\t".join(dline) + "\n")

    print("Testcase 111 created")
def testcase_112(n_set=16):  # 8 writes in inst_0 (all same set, distinct tags), then 4 reads in inst_1 (matching last 4 writes' tags)
    import os, random
    bp="subsystem_testcase/testcase_112/"
    os.makedirs(bp,exist_ok=True)
    p0=os.path.join(bp,"instr_mem_A.mem")
    p1=os.path.join(bp,"instr_mem_B.mem")
    pm=os.path.join(bp,"main_memory_init.mem")
    tag_lim=128
    def blk(a):return a&0xFFFFFFC0
    chosen_set=random.randint(0,n_set-1)
    # 8 tags for inst_0: first 4 writes, next 4 writes
    all_tags_8=random.sample(range(tag_lim),8)
    tags_0_1=all_tags_8[:4]  # first 4 writes
    tags_0_2=all_tags_8[4:]  # second 4 writes
    writes_0_1=[]
    writes_0_2=[]
    for t in tags_0_1:
        wofs=random.randint(0,15)
        addr=0x20000+(t<<10)+(chosen_set<<6)+(wofs<<2)
        data=f"0x{random.randint(0,2**32-1):08x}"
        writes_0_1.append((addr,data))
    for t in tags_0_2:
        wofs=random.randint(0,15)
        addr=0x20000+(t<<10)+(chosen_set<<6)+(wofs<<2)
        data=f"0x{random.randint(0,2**32-1):08x}"
        writes_0_2.append((addr,data))
    # inst_1: 4 reads matching the second 4 writes
    reads_1=[]
    for t in tags_0_2:
        wofs=random.randint(0,15)
        addr=0x20000+(t<<10)+(chosen_set<<6)+(wofs<<2)
        reads_1.append(addr)
    with open(p0,"w") as f0:
        for(a,d)in writes_0_1:f0.write(f"write\t0x{a:08x}\t{d}\n")
        for(a,d)in writes_0_2:f0.write(f"write\t0x{a:08x}\t{d}\n")
    with open(p1,"w") as f1:
        for a in reads_1:f1.write(f"read\t0x{a:08x}\n")
    # mem_data: addresses from inst_0 only
    all_writes_0=[x[0]for x in writes_0_1]+[x[0]for x in writes_0_2]
    blocks={blk(a)for a in all_writes_0}
    with open(pm,"w") as fm:
        for b in blocks:
            d=[f"0x{random.randint(0,2**32-1):08x}"for _ in range(16)]
            fm.write(f"0x{b:08x}\t"+"\t".join(d)+"\n")
    print("Testcase 112 created")
def testcase_113(n_set=16):  # 4 writes + 2 reads in inst_0, 4 writes + 2 reads in inst_1, all same set, no overlapping tags
    import os, random
    bp = "subsystem_testcase/testcase_113/"
    os.makedirs(bp, exist_ok=True)
    p0 = os.path.join(bp, "instr_mem_A.mem")
    p1 = os.path.join(bp, "instr_mem_B.mem")
    pm = os.path.join(bp, "main_memory_init.mem")

    # Mỗi địa chỉ: 0x20000 + (tag << 10) + (set << 6) + (word_offset << 2), đảm bảo vùng chung 0x20000..0x3FFFF
    # Tạo tổng cộng 12 tag duy nhất: 4 write + 2 read (inst_0), 4 write + 2 read (inst_1)
    # -> Không trùng tag giữa tất cả lệnh
    tag_limit = 128
    all_tags_12 = random.sample(range(tag_limit), 12)

    # Chia:
    #  - w0_tags (4 lệnh write inst_0)
    #  - r0_tags (2 lệnh read inst_0)
    #  - w1_tags (4 lệnh write inst_1)
    #  - r1_tags (2 lệnh read inst_1)
    w0_tags = all_tags_12[0:4]
    r0_tags = all_tags_12[4:6]
    w1_tags = all_tags_12[6:10]
    r1_tags = all_tags_12[10:12]

    def block_addr(a): return a & 0xFFFFFFC0

    # Tất cả lệnh đều dùng chung 1 set (user yêu cầu set của inst_1 = set lệnh cuối inst_0 => tương đương 1 set)
    chosen_set = random.randint(0, n_set - 1)

    # Sinh địa chỉ + data cho writes, địa chỉ cho reads
    def make_addr(tag):
        word_off = random.randint(0,15)
        return 0x20000 + (tag<<10) + (chosen_set<<6) + (word_off<<2)

    writes_0 = []
    for t in w0_tags:
        addr = make_addr(t)
        data = f"0x{random.randint(0,2**32-1):08x}"
        writes_0.append((addr, data))

    reads_0 = []
    for t in r0_tags:
        addr = make_addr(t)
        reads_0.append(addr)

    writes_1 = []
    for t in w1_tags:
        addr = make_addr(t)
        data = f"0x{random.randint(0,2**32-1):08x}"
        writes_1.append((addr, data))

    reads_1 = []
    for t in r1_tags:
        addr = make_addr(t)
        reads_1.append(addr)

    # Ghi inst_0: 4 write (w0_tags) + 2 read (r0_tags)
    with open(p0,"w") as f0:
        for (addr, data) in writes_0:
            f0.write(f"write\t0x{addr:08x}\t{data}\n")
        for addr in reads_0:
            f0.write(f"read\t0x{addr:08x}\n")

    # Ghi inst_1: 4 write (w1_tags) + 2 read (r1_tags)
    with open(p1,"w") as f1:
        for (addr, data) in writes_1:
            f1.write(f"write\t0x{addr:08x}\t{data}\n")
        for addr in reads_1:
            f1.write(f"read\t0x{addr:08x}\n")

    # Tạo mem_data cho tất cả (inst_0 + inst_1)
    all_addresses = [a for (a,_) in writes_0] + reads_0 + [a for (a,_) in writes_1] + reads_1
    blocks = {block_addr(a) for a in all_addresses}
    with open(pm,"w") as fm:
        for blk in blocks:
            data_line = [f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            fm.write(f"0x{blk:08x}\t" + "\t".join(data_line) + "\n")

    print("Testcase 113 created")
def testcase_114(n_set=16):
    import os,random
    bp="subsystem_testcase/testcase_114/"
    os.makedirs(bp,exist_ok=True)
    p0=os.path.join(bp,"instr_mem_A.mem");p1=os.path.join(bp,"instr_mem_B.mem");pm=os.path.join(bp,"main_memory_init.mem")
    tag_lim=128
    def blk(a):return a&0xFFFFFFC0
    cs=random.randint(0,n_set-1)  # set cho toàn bộ
    # Tổng cộng 12 lệnh write: inst_0 có 6, inst_1 có 6, tất cả khác tag
    all_tags_12=random.sample(range(tag_lim),12)
    w0_4=all_tags_12[:4]   # 4 lệnh write đầu inst_0
    w0_2=all_tags_12[4:6]  # 2 lệnh write kế tiếp inst_0
    w1_4=all_tags_12[6:10] # 4 lệnh write đầu inst_1
    w1_2=all_tags_12[10:]  # 2 lệnh write kế tiếp inst_1
    def make_addr(t):
        wofs=random.randint(0,15)
        return 0x20000+(t<<10)+(cs<<6)+(wofs<<2)
    writes_0_4=[];writes_0_2=[]
    for t in w0_4:
        addr=make_addr(t)
        data=f"0x{random.randint(0,2**32-1):08x}"
        writes_0_4.append((addr,data))
    for t in w0_2:
        addr=make_addr(t)
        data=f"0x{random.randint(0,2**32-1):08x}"
        writes_0_2.append((addr,data))
    writes_1_4=[];writes_1_2=[]
    for t in w1_4:
        addr=make_addr(t)
        data=f"0x{random.randint(0,2**32-1):08x}"
        writes_1_4.append((addr,data))
    for t in w1_2:
        addr=make_addr(t)
        data=f"0x{random.randint(0,2**32-1):08x}"
        writes_1_2.append((addr,data))
    # Ghi inst_0
    with open(p0,"w")as f0:
        for(a,d)in writes_0_4:f0.write(f"write\t0x{a:08x}\t{d}\n")
        for(a,d)in writes_0_2:f0.write(f"write\t0x{a:08x}\t{d}\n")
    # Ghi inst_1
    with open(p1,"w")as f1:
        for(a,d)in writes_1_4:f1.write(f"write\t0x{a:08x}\t{d}\n")
        for(a,d)in writes_1_2:f1.write(f"write\t0x{a:08x}\t{d}\n")
    # mem_data cho tất cả writes
    all_addrs_0=[x[0]for x in writes_0_4]+[x[0]for x in writes_0_2]
    all_addrs_1=[x[0]for x in writes_1_4]+[x[0]for x in writes_1_2]
    blocks={blk(a)for a in all_addrs_0+all_addrs_1}
    with open(pm,"w")as fm:
        for b in blocks:
            d=[f"0x{random.randint(0,2**32-1):08x}"for _ in range(16)]
            fm.write(f"0x{b:08x}\t"+"\t".join(d)+"\n")
    print("Testcase 114 created")
def testcase_115(n_set=16):
    base_path = "subsystem_testcase/testcase_115/"
    os.makedirs(base_path, exist_ok=True)
    path_0 = os.path.join(base_path, "instr_mem_A.mem")
    path_1 = os.path.join(base_path, "instr_mem_B.mem")
    path_mem = os.path.join(base_path, "main_memory_init.mem")

    # Địa chỉ: 0x20000 + (tag << 10) + (set << 6) + (word_offset << 2)
    # => Tất cả nằm trong [0x20000..0x3FFFF]
    tag_limit = 128  # đảm bảo (tag << 10) <= (127 << 10) = 130048, cộng 0x20000 (131072) vẫn <= 0x3FFFF (262143)

    def block_addr(a): return a & 0xFFFFFFC0

    # Chọn set, tag
    chosen_set = random.randint(0, n_set - 1)
    chosen_tag = random.randint(0, tag_limit - 1)

    # inst_0:
    # 1) read addr0
    # 2) read addr1 (cùng set+tag, khác word_offset)
    word0 = random.randint(0, 15)
    addr0 = 0x20000 + (chosen_tag << 10) + (chosen_set << 6) + (word0 << 2)

    word1 = random.randint(0, 15)
    addr1 = 0x20000 + (chosen_tag << 10) + (chosen_set << 6) + (word1 << 2)

    # inst_1:
    # 1) read addr2 (cùng set+tag với lệnh thứ 2 trong inst_0)
    word2 = random.randint(0, 15)
    addr2 = 0x20000 + (chosen_tag << 10) + (chosen_set << 6) + (word2 << 2)

    with open(path_0, "w") as f0:
        f0.write(f"read\t0x{addr0:08x}\n")
        f0.write(f"read\t0x{addr1:08x}\n")

    with open(path_1, "w") as f1:
        f1.write(f"read\t0x{addr2:08x}\n")

    # mem_data: tạo dữ liệu cho tất cả lệnh trong inst_0 (addr0, addr1)
    blocks = {block_addr(addr0), block_addr(addr1)}
    with open(path_mem, "w") as fm:
        for blk in blocks:
            data_words = [f"0x{random.randint(0, 2**32 - 1):08x}" for _ in range(16)]
            fm.write(f"0x{blk:08x}\t" + "\t".join(data_words) + "\n")

    print("Testcase 115 created")
def testcase_116(n_set=16):
    import os, random
    base_path = "subsystem_testcase/testcase_116/"
    os.makedirs(base_path, exist_ok=True)
    path_0 = os.path.join(base_path, "instr_mem_A.mem")
    path_1 = os.path.join(base_path, "instr_mem_B.mem")
    path_mem = os.path.join(base_path, "main_memory_init.mem")

    # Địa chỉ: 0x20000 + (tag << 10) + (set << 6) + (word_offset << 2)
    # => Nằm trong vùng [0x20000..0x3FFFF]
    tag_limit = 128
    def block_addr(a): return a & 0xFFFFFFC0

    chosen_set = random.randint(0, n_set - 1)
    chosen_tag = random.randint(0, tag_limit - 1)

    # inst_0: 1 read
    word0 = random.randint(0, 15)
    addr0 = 0x20000 + (chosen_tag << 10) + (chosen_set << 6) + (word0 << 2)

    # inst_1: 1 read (cùng set+tag với lệnh trong inst_0)
    word1 = random.randint(0, 15)
    addr1 = 0x20000 + (chosen_tag << 10) + (chosen_set << 6) + (word1 << 2)

    with open(path_0, "w") as f0:
        f0.write(f"read\t0x{addr0:08x}\n")

    with open(path_1, "w") as f1:
        f1.write(f"read\t0x{addr1:08x}\n")

    # mem_data: tạo dữ liệu cho lệnh trong inst_0
    blocks = {block_addr(addr0)}
    with open(path_mem, "w") as fm:
        for blk in blocks:
            data_words = [f"0x{random.randint(0, 2**32 - 1):08x}" for _ in range(16)]
            fm.write(f"0x{blk:08x}\t" + "\t".join(data_words) + "\n")

    print("Testcase 116 created")
def testcase_117(n_set=16):
    import os, random
    base_path = "subsystem_testcase/testcase_117/"
    os.makedirs(base_path, exist_ok=True)
    p0 = os.path.join(base_path, "instr_mem_A.mem")
    p1 = os.path.join(base_path, "instr_mem_B.mem")
    pm = os.path.join(base_path, "main_memory_init.mem")
    tag_limit = 128
    def blk(a):return a & 0xFFFFFFC0
    cs = random.randint(0, n_set - 1)
    tg = random.randint(0, tag_limit - 1)
    w0 = random.randint(0, 15)
    addr0 = 0x20000 + (tg << 10) + (cs << 6) + (w0 << 2)
    data0 = f"0x{random.randint(0,2**32-1):08x}"
    w1 = random.randint(0, 15)
    addr1 = 0x20000 + (tg << 10) + (cs << 6) + (w1 << 2)
    data1 = f"0x{random.randint(0,2**32-1):08x}"
    with open(p0,"w") as f0:f0.write(f"write\t0x{addr0:08x}\t{data0}\n")
    with open(p1,"w") as f1:f1.write(f"write\t0x{addr1:08x}\t{data1}\n")
    blocks = {blk(addr0)}
    with open(pm,"w") as fm:
        for b in blocks:
            d=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            fm.write(f"0x{b:08x}\t"+"\t".join(d)+"\n")
    print("Testcase 117 created")
def testcase_118(n_set=16):
    import os, random
    base_path = "subsystem_testcase/testcase_118/"
    os.makedirs(base_path, exist_ok=True)
    p0 = os.path.join(base_path, "instr_mem_A.mem")
    p1 = os.path.join(base_path, "instr_mem_B.mem")
    pm = os.path.join(base_path, "main_memory_init.mem")
    tag_limit = 128
    def blk(a): return a & 0xFFFFFFC0

    chosen_set = random.randint(0, n_set - 1)
    chosen_tag = random.randint(0, tag_limit - 1)

    # inst_0: 1 read
    word0 = random.randint(0, 15)
    addr0 = 0x20000 + (chosen_tag << 10) + (chosen_set << 6) + (word0 << 2)

    # inst_1: 1 write (cùng set + tag)
    word1 = random.randint(0, 15)
    addr1 = 0x20000 + (chosen_tag << 10) + (chosen_set << 6) + (word1 << 2)
    data1 = f"0x{random.randint(0, 2**32-1):08x}"

    with open(p0, "w") as f0:
        f0.write(f"read\t0x{addr0:08x}\n")

    with open(p1, "w") as f1:
        f1.write(f"write\t0x{addr1:08x}\t{data1}\n")

    # mem_data: cho lệnh inst_0
    blocks = {blk(addr0)}
    with open(pm, "w") as fm:
        for b in blocks:
            d = [f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            fm.write(f"0x{b:08x}\t" + "\t".join(d) + "\n")

    print("Testcase 118 created")
def testcase_119(n_set=16):  # inst_0: 1 write; inst_1: 1 read (same set & tag as inst_0 write)
    import os,random
    bp="subsystem_testcase/testcase_119/";os.makedirs(bp,exist_ok=True)
    p0=os.path.join(bp,"instr_mem_A.mem");p1=os.path.join(bp,"instr_mem_B.mem");pm=os.path.join(bp,"main_memory_init.mem")
    tag_bits=32-(n_set.bit_length()+4+2)  # số bit tag
    def blk(a): return a & 0xFFFFFFC0  # lấy block address
    cs=random.randint(0,n_set-1)  # set được chọn
    tg=random.randint(0,(1<<tag_bits)-1)  # tag được chọn
    w0=random.randint(0,15); addr0=0x20000+(tg<<10)+(cs<<6)+(w0<<2)  # địa chỉ write cho inst_0
    data0=f"0x{random.randint(0,2**32-1):08x}"
    w1=random.randint(0,15); addr1=0x20000+(tg<<10)+(cs<<6)+(w1<<2)  # địa chỉ read cho inst_1
    with open(p0,"w") as f0: f0.write(f"write\t0x{addr0:08x}\t{data0}\n")
    with open(p1,"w") as f1: f1.write(f"read\t0x{addr1:08x}\n")
    blocks={blk(addr0)}
    with open(pm,"w") as fm:
        for b in blocks:
            d=[f"0x{random.randint(0,2**32-1):08x}" for _ in range(16)]
            fm.write(f"0x{b:08x}\t"+"\t".join(d)+"\n")
    print("Testcase 119 created")


def main():
    # Danh sách các hàm testcase
    list_testcases = [
        testcase_1, testcase_2, testcase_3, testcase_4, testcase_5, testcase_6, testcase_7, testcase_8, testcase_9,
        testcase_10, testcase_11, testcase_12, testcase_13, testcase_14, testcase_15, testcase_16, testcase_17,
        testcase_18, testcase_19, testcase_20, testcase_21, testcase_22, testcase_23, testcase_24, testcase_25,
        testcase_26, testcase_27, testcase_28, testcase_29, testcase_30, testcase_31, testcase_32, testcase_33,
        testcase_34, testcase_35, testcase_36, testcase_37, testcase_38, testcase_39, testcase_40, testcase_41,
        testcase_42, testcase_43, testcase_44, testcase_45, testcase_46, testcase_47, testcase_48, testcase_49,
        testcase_50, testcase_51, testcase_52, testcase_53, testcase_54, testcase_55, testcase_56, testcase_57,
        testcase_58, testcase_59, testcase_60, testcase_61, testcase_62, testcase_63, testcase_64, testcase_65,
        testcase_66, testcase_67, testcase_68, testcase_69, testcase_70, testcase_71, testcase_72, testcase_73,
        testcase_74, testcase_75, testcase_76, testcase_77, testcase_78, testcase_79, testcase_80, testcase_81,
        testcase_82, testcase_83, testcase_84, testcase_85, testcase_86, testcase_87, testcase_88, testcase_89,
        testcase_90, testcase_91, testcase_92, testcase_93, testcase_94, testcase_95, testcase_96, testcase_97,
        testcase_98, testcase_99, testcase_100, testcase_101, testcase_102, testcase_103, testcase_104, testcase_105,
        testcase_106, testcase_107, testcase_108, testcase_109, testcase_110, testcase_111, testcase_112, testcase_113,
        testcase_114, testcase_115, testcase_116, testcase_117, testcase_118, testcase_119
    ]


    print("========== MENU TẠO TESTCASE ==========")
    print("1. Tạo tất cả 119 testcase")
    print("2. Tạo testcase cụ thể")

    choice = input("Nhập lựa chọn (1 hoặc 2): ")

    if choice == '1':
        # Gọi tuần tự tất cả các hàm testcase
        for func in list_testcases:
            func()
    elif choice == '2':
        # Yêu cầu người dùng nhập số testcase mong muốn
        tc_number = input("Nhập testcase muốn tạo (1-120): ")
        if tc_number.isdigit():
            tc_number = int(tc_number)
            if 1 <= tc_number <= 200:
                # Gọi hàm tương ứng (do index trong list bắt đầu từ 0)
                list_testcases[tc_number - 1]()
            else:
                print("Số testcase không hợp lệ!")
        else:
            print("Vui lòng nhập số hợp lệ!")
    else:
        print("Lựa chọn không hợp lệ!")


if __name__ == "__main__":
    main()
