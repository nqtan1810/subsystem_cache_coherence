0:	addi   x1  , x0  , 32
4:	slli   x1  , x1  , 8
8:	addi   x2  , x0  , 0
12:	addi   x3  , x0  , 16
16:	beq    x2  , x3  , 48
20:	addi   x4  , x4  , 801
24:	slli   x5  , x4  , 13
28:	srli   x7  , x4  , 9
32:	xor    x4  , x4  , x5
36:	xor    x4  , x4  , x7
40:	addi   x4  , x4  , 801
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
112:	addi   x1  , x0  , 16
116:	slli   x1  , x1  , 8
120:	addi   x20 , x0  , 291
124:	addi   x21 , x0  , 1110
128:	addi   x22 , x0  , 120
132:	sw     x20 , 0(x1)
136:	sh     x21 , 0(x1)
140:	sb     x22 , 0(x1)
144:	lw     x20 , 0(x1)
148:	lh     x21 , 4(x1)
152:	lhu    x22 , 8(x1)
156:	lb     x23 , 12(x1)
160:	lbu    x24 , 16(x1)
164:	lw     x25 , 20(x1)
168:	lh     x26 , 24(x1)
172:	lhu    x27 , 28(x1)
176:	lb     x28 , 32(x1)
180:	lbu    x29 , 36(x1)
184:	lw     x30 , 40(x1)
188:	lw     x31 , 44(x1)
