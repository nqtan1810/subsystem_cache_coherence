import os

# Directory to save the files (optional)
output_dir = ""

# Create 20 .asm files
for k in range(1, 21):
    filename_0 = f"testcase_A_{k}.asm"
    filename_1 = f"testcase_B_{k}.asm"

    filepath = os.path.join(output_dir, filename_0)

    with open(filepath, "w") as f:
        f.write(f"# This is {filename_0}\n")
        f.write("# Description: \n\n")
        f.write(".text\n")
        f.write("# assembly code is start here!\n")
    f.close()

    filepath = os.path.join(output_dir, filename_1)

    with open(filepath, "w") as f:
        f.write(f"# This is {filename_1}\n")
        f.write("# Description: \n\n")
        f.write(".text\n")
        f.write("# assembly code is start here!\n")
    f.close()

print(f"20 .asm files created in '{output_dir}' folder.")


