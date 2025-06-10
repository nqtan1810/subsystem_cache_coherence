# Refactored version of the provided disassembler as a standalone script with file input/output

def disassemble(hex_file_path: str, asm_file_path: str):
    # Instruction maps
    R_type = {
        '001': 'sll', '011': 'sltu', '110': 'or',
        '010': 'slt', '100': 'xor', '111': 'and',
    }
    LOAD_type = {
        '000': 'lb', '001': 'lh', '010': 'lw', '011': 'ld',
        '100': 'lbu', '101': 'lhu', '110': 'lwu'
    }
    I_type = {
        '000': 'addi', '001': 'slli', '010': 'slti', '011': 'sltiu',
        '100': 'xori', '110': 'ori', '111': 'andi'
    }
    STORE_type = {
        '000': 'sb', '001': 'sh', '010': 'sw', '011': 'sd'
    }
    SBRANCH_type = {
        '000': 'beq', '001': 'bne', '100': 'blt', '101': 'bge',
        '110': 'bltu', '111': 'bgeu'
    }

    def convert_bintodec(temp):
        s = 0
        temp = temp.rjust(32, temp[0])[::-1]
        for i in range(len(temp)):
            if temp[i] == '1':
                s += 2**i
        if temp[-1] == '1':
            s = s - (1 << 32)
        return str(s)

    def convert_hextobin(string):
        return bin(int(string, 16))[2:].zfill(32)

    def instructions_handler(string):
        string = string.strip().replace(' ', '')
        bcode = convert_hextobin(string) if string.startswith('0x') else string.zfill(32)
        return bcode[:32]

    def Rtype_handler(bcode):
        instruction = ''
        if bcode[17:20] == '000':
            instruction += 'add' if bcode[:7] == '0000000' else 'sub'
        elif bcode[17:20] == '101':
            instruction += 'srl' if bcode[:7] == '0000000' else 'sra'
        else:
            instruction += R_type.get(bcode[17:20], 'unknown')
        instruction = instruction.ljust(7, ' ')
        instruction += 'x' + convert_bintodec('0' + bcode[20:25]).ljust(3) + ', '
        instruction += 'x' + convert_bintodec('0' + bcode[12:17]).ljust(3) + ', '
        instruction += 'x' + convert_bintodec('0' + bcode[7:12])
        return instruction

    def Itype_handler(bcode):
        instruction = ''
        opcode = bcode[25:]
        if opcode == '0000011':
            instruction += LOAD_type.get(bcode[17:20], 'unknown')
        elif opcode == '0010011':
            if bcode[17:20] == '101':
                instruction += 'srli' if bcode[:7] == '0000000' else 'srai'
            else:
                instruction += I_type.get(bcode[17:20], 'unknown')
        elif opcode == '1100111':
            instruction += 'jalr'
        instruction = instruction.ljust(7, ' ')
        instruction += 'x' + convert_bintodec('0' + bcode[20:25]).ljust(3) + ', '
        if opcode == '0000011':
            instruction += convert_bintodec(bcode[:12]) + '('
            instruction += 'x' + convert_bintodec('0' + bcode[12:17]) + ')'
        else:
            instruction += 'x' + convert_bintodec('0' + bcode[12:17]).ljust(3) + ', '
            instruction += convert_bintodec(bcode[:12])
        return instruction

    def Stype_handler(bcode):
        instruction = STORE_type.get(bcode[17:20], 'unknown').ljust(7, ' ')
        instruction += 'x' + convert_bintodec('0' + bcode[7:12]).ljust(3) + ', '
        imm = bcode[0:7] + bcode[20:25]
        instruction += convert_bintodec(imm) + '('
        instruction += 'x' + convert_bintodec('0' + bcode[12:17]) + ')'
        return instruction

    def SBtype_handler(bcode):
        instruction = SBRANCH_type.get(bcode[17:20], 'unknown').ljust(7, ' ')
        instruction += 'x' + convert_bintodec('0' + bcode[12:17]).ljust(3) + ', '
        instruction += 'x' + convert_bintodec('0' + bcode[7:12]).ljust(3) + ', '
        imm = bcode[0] + bcode[24] + bcode[1:7] + bcode[20:24] + '0'
        instruction += convert_bintodec(imm.rjust(13, imm[0]))
        return instruction

    def Utype_handler(bcode):
        instruction = 'auipc' if bcode[25:] == '0010111' else 'lui'
        instruction = instruction.ljust(7, ' ')
        instruction += 'x' + convert_bintodec('0' + bcode[20:25]).ljust(3) + ', '
        instruction += convert_bintodec(bcode[0:20])
        return instruction

    def UJtype_handler(bcode):
        instruction = 'jal'.ljust(7, ' ')
        instruction += 'x' + convert_bintodec('0' + bcode[20:25]).ljust(3) + ', '
        imm = bcode[0] + bcode[12:20] + bcode[11] + bcode[1:11] + '0'
        instruction += convert_bintodec(imm.rjust(21, imm[0]))
        return instruction

    # Read hex input and disassemble
    with open(hex_file_path, 'r') as f:
        hex_lines = f.readlines()

    instruction_result = {}
    PC = 0

    for line in hex_lines:
        if line.strip() == '':
            continue
        bcode = instructions_handler(line)
        opcode = bcode[25:]
        if opcode == '0110011':
            instruction_result[PC] = Rtype_handler(bcode)
        elif opcode in ('0000011', '0010011', '1100111'):
            instruction_result[PC] = Itype_handler(bcode)
        elif opcode == '0100011':
            instruction_result[PC] = Stype_handler(bcode)
        elif opcode == '1100011':
            instruction_result[PC] = SBtype_handler(bcode)
        elif opcode in ('0110111', '0010111'):
            instruction_result[PC] = Utype_handler(bcode)
        elif opcode == '1101111':
            instruction_result[PC] = UJtype_handler(bcode)
        else:
            instruction_result[PC] = 'unknown'
        PC += 4

    # Write to output .asm file
    with open(asm_file_path, 'w') as f:
        for pc, inst in instruction_result.items():
            f.write(f"{pc}:\t{inst}\n")

while (1):
    tc_id = input("Enter your testcase: ")
    if tc_id == 'e':
        break
    input_path_0 = f"D:/University/KLTN/hw_design/testcase/assembly/testcase_A_{tc_id}.bin"
    input_path_1 = f"D:/University/KLTN/hw_design/testcase/assembly/testcase_B_{tc_id}.bin"
    output_path_0 = f"D:/University/KLTN/hw_design/testcase/assembly/testcase_A_{tc_id}.asm"
    output_path_1 = f"D:/University/KLTN/hw_design/testcase/assembly/testcase_B_{tc_id}.asm"
    disassemble(input_path_0, output_path_0)
    disassemble(input_path_1, output_path_1)
