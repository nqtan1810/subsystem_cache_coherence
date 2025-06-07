# This is testcase_A_2.asm
# Description: CORE_0/CORE_1 Read miss - Fetch từ  MEM - Set not full - No Write back,
#		truy cập vào vùng dữ liệu dùng chung nhưng không cùng địa chỉ

.text
# assembly code is start here!
# === Set x1 = 0x1000 ===
addi x1, x0, 0x10
slli x1, x1, 8        # x1 = 0x1000

# === x2 = index = 0 ===
addi x2, x0, 0

# === Store 5 values to memory ===
store_loop1:
    addi x3, x0, 5
    beq  x2, x3, load_loop1

    # Value = 0x11111111 + i
    addi x4, x0, 0x11
    slli x4, x4, 8
    ori  x4, x4, 0x11
    slli x4, x4, 8
    ori  x4, x4, 0x11
    slli x4, x4, 8
    ori  x4, x4, 0x11
    add  x4, x4, x2

    slli x5, x2, 2
    add  x6, x1, x5
    sw   x4, 0(x6)

    addi x2, x2, 1
    jal  x0, store_loop1

# === Load values from 0x1000 ===
load_loop1:
    addi x2, x0, 0
    addi x7, x0, 0

load1:
    addi x3, x0, 5
    beq  x2, x3, switch_base2

    slli x5, x2, 2
    add  x6, x1, x5

    lw   x8, 0(x6)
    lh   x9, 0(x6)
    lhu  x10, 0(x6)
    lb   x11, 0(x6)
    lbu  x12, 0(x6)

    add  x7, x7, x8
    xor  x7, x7, x9
    or   x7, x7, x10
    and  x7, x7, x11
    add  x7, x7, x12

    addi x2, x2, 1
    jal  x0, load1

# === Switch to base 0x1400 ===
switch_base2:
    addi x1, x0, 0x14
    slli x1, x1, 8       # x1 = 0x1400
    addi x2, x0, 0

# === Store to 0x1400 ===
store_loop2:
    addi x3, x0, 5
    beq  x2, x3, load_loop2

    # Value = 0x22222222 + i
    addi x4, x0, 0x22
    slli x4, x4, 8
    ori  x4, x4, 0x22
    slli x4, x4, 8
    ori  x4, x4, 0x22
    slli x4, x4, 8
    ori  x4, x4, 0x22
    add  x4, x4, x2

    slli x5, x2, 2
    add  x6, x1, x5
    sw   x4, 0(x6)

    addi x2, x2, 1
    jal  x0, store_loop2

# === Load from 0x1400 ===
load_loop2:
    addi x2, x0, 0

load2:
    addi x3, x0, 5
    beq  x2, x3, switch_base3

    slli x5, x2, 2
    add  x6, x1, x5

    lw   x8, 0(x6)
    lh   x9, 0(x6)
    lhu  x10, 0(x6)
    lb   x11, 0(x6)
    lbu  x12, 0(x6)

    addi x2, x2, 1
    jal  x0, load2
# === Switch to base 0x1800 ===
switch_base3:
    addi x1, x0, 0x18
    slli x1, x1, 8       # x1 = 0x1800
    addi x2, x0, 0

# === Store to 0x1800 ===
store_loop3:
    addi x3, x0, 5
    beq  x2, x3, load_loop3

    # Value = 0x33333333 + i
    addi x4, x0, 0x33
    slli x4, x4, 8
    ori  x4, x4, 0x33
    slli x4, x4, 8
    ori  x4, x4, 0x33
    slli x4, x4, 8
    ori  x4, x4, 0x33
    add  x4, x4, x2

    slli x5, x2, 2
    add  x6, x1, x5
    sw   x4, 0(x6)

    addi x2, x2, 1
    jal  x0, store_loop3

# === Load from 0x1800 ===
load_loop3:
    addi x2, x0, 0

load3:
    addi x3, x0, 5
    beq  x2, x3, switch_base4

    slli x5, x2, 2
    add  x6, x1, x5

    lw   x8, 0(x6)
    lh   x9, 0(x6)
    lhu  x10, 0(x6)
    lb   x11, 0(x6)
    lbu  x12, 0(x6)

    addi x2, x2, 1
    jal  x0, load3
# === Switch to base 0x1c00 ===
switch_base4:
    addi x1, x0, 0x1c
    slli x1, x1, 8       # x1 = 0x1c00
    addi x2, x0, 0

# === Store to 0x1c00 ===
store_loop4:
    addi x3, x0, 5
    beq  x2, x3, load_loop4

    # Value = 0x44444444 + i
    addi x4, x0, 0x44
    slli x4, x4, 8
    ori  x4, x4, 0x44
    slli x4, x4, 8
    ori  x4, x4, 0x44
    slli x4, x4, 8
    ori  x4, x4, 0x44
    add  x4, x4, x2

    slli x5, x2, 2
    add  x6, x1, x5
    sw   x4, 0(x6)

    addi x2, x2, 1
    jal  x0, store_loop4

# === Load from 0x1c00 ===
load_loop4:
    addi x2, x0, 0

load4:
    addi x3, x0, 5
    beq  x2, x3, switch_base5

    slli x5, x2, 2
    add  x6, x1, x5

    lw   x8, 0(x6)
    lh   x9, 0(x6)
    lhu  x10, 0(x6)
    lb   x11, 0(x6)
    lbu  x12, 0(x6)

    addi x2, x2, 1
    jal  x0, load4
# === Switch to base 0x2000 ===
switch_base5:
    addi x1, x0, 0x20
    slli x1, x1, 8       # x1 = 0x2000
    addi x2, x0, 0

# === Store to 0x2000 ===
store_loop5:
    addi x3, x0, 5
    beq  x2, x3, load_loop5

    # Value = 0x55555555 + i
    addi x4, x0, 0x55
    slli x4, x4, 8
    ori  x4, x4, 0x55
    slli x4, x4, 8
    ori  x4, x4, 0x55
    slli x4, x4, 8
    ori  x4, x4, 0x55
    add  x4, x4, x2

    slli x5, x2, 2
    add  x6, x1, x5
    sw   x4, 0(x6)

    addi x2, x2, 1
    jal  x0, store_loop5

# === Load from 0x2000 ===
load_loop5:
    addi x2, x0, 0

load5:
    addi x3, x0, 5
    beq  x2, x3, end_program

    slli x5, x2, 2
    add  x6, x1, x5

    lw   x8, 0(x6)
    lh   x9, 0(x6)
    lhu  x10, 0(x6)
    lb   x11, 0(x6)
    lbu  x12, 0(x6)

    addi x2, x2, 1
    jal  x0, load5
    
end_program:
