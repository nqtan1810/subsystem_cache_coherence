0:	addi   x1  , x0  , 32
4:	slli   x1  , x1  , 8
8:	addi   x2  , x0  , 0
12:	addi   x3  , x0  , 5
16:	beq    x2  , x3  , 56
20:	addi   x4  , x0  , 85
24:	slli   x4  , x4  , 8
28:	ori    x4  , x4  , 85
32:	slli   x4  , x4  , 8
36:	ori    x4  , x4  , 85
40:	slli   x4  , x4  , 8
44:	ori    x4  , x4  , 85
48:	add    x4  , x4  , x2
52:	slli   x5  , x2  , 2
56:	add    x6  , x1  , x5
60:	sw     x4  , 0(x6)
64:	addi   x2  , x2  , 1
68:	jal    x0  , -56
