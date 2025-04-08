# **************************************************************************************
# subsystem's software model
# **************************************************************************************

# **************************************************************************************
"""
                                           ----------          ----------
                                           |  CPU A |          |  CPU A |
                                           ----------          ----------
                                                ^                  ^
                                                |                  |
                                                |                  |
                                                V                  V
                                          ------------        ------------
                                          |  CACHE A |        |  CACHE B |   (4-way, 16-set) 4MB
                                          ------------        ------------
                                                ^                  ^
                                                |                  |
                                                |                  |
                                                V                  V
                               -------------------------------------------------------
                                                  AXI + Coherence
                               -------------------------------------------------------
                                                         ^
                                                         |
                                                         |
                                                         V
                                               ---------------------
                                               |    Main Memory    |
                                               ---------------------
"""
# **************************************************************************************
from subsystem import *

if __name__ == "__main__":
    while (testbench_id := int(input("Which component do you want to run simulation?\n1. Cache\n2. AXI + Coherence\n3. Subsystem\nEnter your choice: "))) not in [1, 2, 3]:
        print("Your choice is unsupported!")
    if testbench_id == 1:
        run_cache()
    elif testbench_id == 2:
        run_axi_coherence()
    elif testbench_id == 3:
        run_subsystem()
    compare_actual_expected_results()
