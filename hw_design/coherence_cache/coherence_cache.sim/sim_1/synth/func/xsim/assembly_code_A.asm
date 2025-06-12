.text

addi x1, x0, 48			# pc = 0
addi x2, x0, 64			# pc = 4
addi x3, x0, 84			# pc = 8
addi x4, x0, 108		# pc = 12
addi x2, x0, 0x78       # x2 = 0x78 (positive byte)
addi x3, x0, -1         # x3 = 0xFFFFFFFF = -1 (signed byte)
addi x4, x0, 0x123      # x4 = 0x123 (positive halfword)
addi x5, x0, 0x123      # x5 = 0x123 (positive halfword for testing, limited to 12-bit range)
addi x6, x0, 0x78       # x6 = 0x78 (positive word)
addi x7, x0, 0x567      # x7 = 0x567 (positive word, within 12-bit range)
addi x1, x0, 48			# pc = 0
addi x2, x0, 64			# pc = 4
addi x3, x0, 84			# pc = 8
addi x4, x0, 108		# pc = 12
addi x2, x0, 0x78       # x2 = 0x78 (positive byte)
addi x3, x0, -1         # x3 = 0xFFFFFFFF = -1 (signed byte)
addi x4, x0, 0x123      # x4 = 0x123 (positive halfword)
addi x5, x0, 0x123      # x5 = 0x123 (positive halfword for testing, limited to 12-bit range)
addi x6, x0, 0x78       # x6 = 0x78 (positive word)
addi x7, x0, 0x567      # x7 = 0x567 (positive word, within 12-bit range)

lui x1, 0x1             # x1 = 0x1000 (base address for memory tests)
lb x8, 0(x1)           # Load byte at MEM[0x1000] -> x8 = 0x78