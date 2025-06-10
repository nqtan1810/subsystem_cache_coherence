0:	addi   x1  , x0  , 16
4:	slli   x1  , x1  , 8
8:	addi   x2  , x0  , 0
12:	addi   x3  , x0  , 16
16:	beq    x2  , x3  , 48
20:	addi   x4  , x4  , 291
24:	slli   x5  , x4  , 13
28:	srli   x7  , x4  , 9
32:	xor    x4  , x4  , x5
36:	xor    x4  , x4  , x7
40:	addi   x4  , x4  , 291
44:	slli   x5  , x2  , 2
48:	add    x6  , x1  , x5
52:	sw     x4  , 0(x6)
56:	addi   x2  , x2  , 1
60:	jal    x0  , -48
64:	lw     x8  , 0(x1)
68:	lh     x9  , 4(x1)
72:	lhu    x10 , 8(x1)
76:	lb     x11 , 12(x1)
80:	lbu    x12 , 16(x1)
84:	lw     x13 , 20(x1)
88:	lh     x14 , 24(x1)
92:	lhu    x15 , 28(x1)
96:	lb     x16 , 32(x1)
100:	lbu    x17 , 36(x1)
104:	lw     x18 , 40(x1)
108:	lw     x19 , 44(x1)
112:	addi   x1  , x0  , 32
116:	slli   x1  , x1  , 8
120:	lw     x20 , 0(x1)
124:	lh     x21 , 4(x1)
128:	lhu    x22 , 8(x1)
132:	lb     x23 , 12(x1)
136:	lbu    x24 , 16(x1)
140:	lw     x25 , 20(x1)
144:	lh     x26 , 24(x1)
148:	lhu    x27 , 28(x1)
152:	lb     x28 , 32(x1)
156:	lbu    x29 , 36(x1)
160:	lw     x30 , 40(x1)
164:	lw     x31 , 44(x1)
