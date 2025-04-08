def analyze_address(a):
    n_set = 4  # Số set trong cache
    a_bin = f"{a:032b}"
    set_a = (a >> 6) & ((1 << 4) - 1)
    word_a = (a >> 2) & ((1 << 4) - 1)
    tag_a = a >> (4 + n_set + 2)
    print(f"Address: {a_bin} (Hex: 0x{a:08x}) | Set Index: {set_a} | Tag: {tag_a} | Word Offset: {word_a}")


analyze_address(0x000008a4)
analyze_address(0x0000729c)
analyze_address(0x00002684)
analyze_address(0x000020ac)
analyze_address(0x000016b0)
