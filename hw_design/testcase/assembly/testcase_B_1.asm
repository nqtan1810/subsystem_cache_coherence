# This is testcase_B_1.asm
# Description: CORE_0/CORE_1 Read/Write hit/miss, access private region and shared region but no overlap address

.text
# assembly code is start here!
# === Set x13 = 0x0C00 ===
addi x13, x0, 0x0C
slli x13, x13, 8      # x13 = 0x0C00

# === x14 = index = 0 ===
addi x14, x0, 0

# === Store 5 values to memory at 0x0C00 ===
store_loop1:
    addi x15, x0, 5
    beq  x14, x15, load_loop1

    # Value = 0x22222222 + i
    addi x16, x0, 0x22
    slli x16, x16, 8
    ori  x16, x16, 0x22
    slli x16, x16, 8
    ori  x16, x16, 0x22
    slli x16, x16, 8
    ori  x16, x16, 0x22
    add  x16, x16, x14

    slli x17, x14, 2
    add  x18, x13, x17
    sw   x16, 0(x18)

    addi x14, x14, 1
    jal  x0, store_loop1

# === Load values from 0x0C00 ===
load_loop1:
    addi x14, x0, 0
    addi x19, x0, 0    # accumulator register

load1:
    addi x15, x0, 5
    beq  x14, x15, switch_base

    slli x17, x14, 2
    add  x18, x13, x17

    lw   x20, 0(x18)
    lh   x21, 0(x18)
    lhu  x22, 0(x18)
    lb   x23, 0(x18)
    lbu  x24, 0(x18)

    add  x19, x19, x20
    xor  x19, x19, x21
    or   x19, x19, x22
    and  x19, x19, x23
    add  x19, x19, x24

    addi x14, x14, 1
    jal  x0, load1

# === Switch base to 0x2000 ===
switch_base:
    addi x13, x0, 0x20
    slli x13, x13, 8      # x13 = 0x2000
    addi x14, x0, 0

# === Store to 0x2000 ===
store_loop2:
    addi x15, x0, 5
    beq  x14, x15, load_loop2

    # Value = 0xDEADBEEF + i
    addi x16, x0, 0xEF
    slli x16, x16, 8
    ori  x16, x16, 0xBE
    slli x16, x16, 8
    ori  x16, x16, 0xAD
    slli x16, x16, 8
    ori  x16, x16, 0xDE
    add  x16, x16, x14

    slli x17, x14, 2
    add  x18, x13, x17
    sw   x16, 0(x18)

    addi x14, x14, 1
    jal  x0, store_loop2

# === Load from 0x2000 ===
load_loop2:
    addi x14, x0, 0

load2:
    addi x15, x0, 5
    beq  x14, x15, end_program

    slli x17, x14, 2
    add  x18, x13, x17

    lw   x20, 0(x18)
    lh   x21, 0(x18)
    lhu  x22, 0(x18)
    lb   x23, 0(x18)
    lbu  x24, 0(x18)

    addi x14, x14, 1
    jal  x0, load2

# === End of program ===
end_program:
