# Add "0x" prefix to each hex value
hex_values_prefixed = ['0x00000000'] * (2**16)

# Join them into a single-column formatted string
single_column_output_prefixed = '\n'.join(hex_values_prefixed)

# Save to a file
file_path = "D:/University/KLTN/hw_design/coherence_cache/coherence_cache.srcs/sources_1/new/mem_init.mem"
with open(file_path, "w") as f:
        f.write(single_column_output_prefixed)

