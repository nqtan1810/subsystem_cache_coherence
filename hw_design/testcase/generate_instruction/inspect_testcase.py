import os
def inspect_testcase(dir_path):
    def to_bin32(value): return f"{value:032b}"
    def parse_fields(addr):
        tag = (addr >> 10) & 0x3F
        set_ = (addr >> 6) & 0xF
        word_offset = (addr >> 2) & 0xF
        return tag, set_, word_offset

    file_instr_A = os.path.join(dir_path, "instr_mem_A.mem")
    file_instr_B = os.path.join(dir_path, "instr_mem_B.mem")
    file_mem = os.path.join(dir_path, "main_memory_init.mem")

    # Inspect instruction memory
    if not os.path.exists(file_instr_A):
        print(f"⚠️ File not found: {file_instr_A}")
    else:
        print(f"\n📂 IMEM A: {file_instr_A}")
        with open(file_instr_A, "r") as f:
            for line in f:
                parts = line.strip().split("\t")
                if len(parts) < 2: continue
                instr_type = parts[0]
                addr_hex = parts[1]
                addr = int(addr_hex, 16)
                bin_ = to_bin32(addr)
                tag, set_, word_offset = parse_fields(addr)
                print(f"{instr_type:<5} | {addr_hex} | {bin_} | Tag: {tag:2d} | Set:{set_:2d} | Word:{word_offset:2d}")

        print(f"\n📂 IMEM B: {file_instr_B}")
        with open(file_instr_B, "r") as f:
            for line in f:
                parts = line.strip().split("\t")
                if len(parts) < 2: continue
                instr_type = parts[0]
                addr_hex = parts[1]
                addr = int(addr_hex, 16)
                bin_ = to_bin32(addr)
                tag, set_, word_offset = parse_fields(addr)
                print(f"{instr_type:<5} | {addr_hex} | {bin_} | Tag: {tag:2d} | Set:{set_:2d} | Word:{word_offset:2d}")

    # Inspect main memory init
    if not os.path.exists(file_mem):
        print(f"\n⚠️ File not found: {file_mem}")
    else:
        print(f"\n📦 MAIN MEMORY INIT: {file_mem}")
        with open(file_mem, "r") as f:
            for line in f:
                print(line.strip())

