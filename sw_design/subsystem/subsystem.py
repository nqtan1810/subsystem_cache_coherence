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
import concurrent.futures
import os
import shutil
import subprocess
import concurrent.futures
import filecmp

from system_common import *
from processor import *
from cache_L1 import *
from Interconnect import *
from main_memory import *
from deadlock_handler import *

current_dir = os.path.dirname(os.path.abspath(__file__))
sw_design_dir_path = os.path.dirname(current_dir)
hw_design_dir_path = os.path.join(os.path.dirname(sw_design_dir_path), 'hw_design')

testcase_dir = os.path.join(hw_design_dir_path, 'testcase')
run_dir = os.path.join(testcase_dir, f'run')
subsystem_testcase_dir = os.path.join(testcase_dir, 'generate_instruction/subsystem_testcase')
# cache_testcase_dir = os.path.join(testcase_dir, 'generate_instruction/cache_testcase')
# axi_coherence_testcase_dir = os.path.join(testcase_dir, 'generate_instruction/axi_coherence_testcase')

subsystem_expected_result_dir = os.path.join(testcase_dir, 'run/subsystem_expected_result')
subsystem_actual_result_dir = os.path.join(testcase_dir, 'run/subsystem_actual_result')

# def list_files(directory):
#     #Trả về một dictionary các file với key là tên file và value là đường dẫn đầy đủ.
#     files_dict = {}
#     for root, dirs, files in os.walk(directory):
#         for file in files:
#             # Đảm bảo không ghi đè file có tên giống nhau ở các thư mục khác nhau
#             path = os.path.join(root, file)
#             if file not in files_dict:
#                 files_dict[file] = [path]
#             else:
#                 files_dict[file].append(path)
#     return files_dict
#
# def compare_actual_expected_results():
#     #So sánh các file có cùng tên trong hai thư mục.
#     files_in_folder1 = list_files(subsystem_expected_result_dir)
#     files_in_folder2 = list_files(subsystem_actual_result_dir)
#
#     # Thống kê kết quả
#     passed_num = number_of_testcase
#     result_list = {}
#     for i in range(1, number_of_testcase+1):
#             result_list[f"testcase_{i}"] = 'PASSED'
#     # print(result_list)
#
#     # So sánh các file có tên giống nhau trong hai folders
#     for filename in files_in_folder1:
#         if filename in files_in_folder2:
#             # Có thể có nhiều đường dẫn cho cùng một tên file
#             for file1_path in files_in_folder1[filename]:
#                 for file2_path in files_in_folder2[filename]:
#                     if filecmp.cmp(file1_path, file2_path, shallow=False):
#                         print(f"Actual result: {filename} is SAME with Expected result: {filename}.")
#                     else:
#                         print(f"Actual result: {filename} is NOT SAME with Expected result: {filename}.")
#                         temp_file_name = filename.replace("result", "testcase")
#                         result_list[temp_file_name] = "FAILED"
#                         passed_num = passed_num - 1
#         else:
#             print(f"File {filename} không tồn tại trong {subsystem_actual_result_dir}")
#
#     # Kiểm tra các file trong folder2 không có trong folder1
#     for filename in files_in_folder2:
#         if filename not in files_in_folder1:
#             print(f"File {filename} không tồn tại trong {subsystem_expected_result_dir}")
#
#     # write compare result on .log
#     log_file_path = os.path.join(testcase_dir, "result.log")
#     with open(log_file_path, 'w') as log_file:
#         for key in result_list:
#             log_file.write(key + ": " + result_list[key] + '\n')
#
#         log_file.write("\n\n\n******************** SUMMARY ********************\n" +
#                        "- Number of Testcases: ".ljust(30) + f"{number_of_testcase}".rjust(10) + '\n'
#                        "- Number of PASSED Testcases: ".ljust(30) + f"{passed_num}".rjust(10) + '\n'
#                        "- Number of FAILED Testcases: ".ljust(30) + f"{number_of_testcase-passed_num}".rjust(10) + '\n'
#                        "********************** END **********************\n")

def compare_actual_expected_results(actual_dir=subsystem_actual_result_dir, expected_dir=subsystem_expected_result_dir, log_dir=run_dir):
    with open(f"{log_dir}/result.log", "w", encoding="utf-8") as log:
        for dirpath, _, filenames in os.walk(expected_dir):
            for filename in filenames:
                rel_path = os.path.relpath(os.path.join(dirpath, filename), expected_dir)
                expected_file = os.path.join(expected_dir, rel_path)
                actual_file = os.path.join(actual_dir, rel_path)

                if not os.path.exists(actual_file):
                    log.write(f"[MISSING]    {rel_path}\n")
                elif not filecmp.cmp(expected_file, actual_file, shallow=False):
                    log.write(f"[DIFFERENT]  {rel_path}\n")
                else:
                    log.write(f"[MATCHED]    {rel_path}\n")

def run_cache():
    print("SW cache tb is still developing!")

def run_axi_coherence():
    print("SW run_axi_coherence tb is still developing!")

def delete_previous_expected_result(expected_result_dir, testcase_id):
    # print("Start delete previous actual_result!")
    result_path = os.path.join(current_dir, f"{expected_result_dir}/testcase_{testcase_id}")
    if os.path.exists(result_path):
        shutil.rmtree(result_path)
        print(f"Deleted {result_path}")

def create_expected_resutl_folder(base_path, testcase_id):
    folder_path = os.path.join(base_path, f"testcase_{testcase_id}")
    os.makedirs(folder_path, exist_ok=True)

def run_subsystem_testcase(testcase_id):
    create_expected_resutl_folder(subsystem_expected_result_dir, testcase_id)
    testcase_id_path = os.path.join(subsystem_testcase_dir, f'testcase_{testcase_id}')
    expected_result_path = os.path.join(subsystem_expected_result_dir, f'testcase_{testcase_id}')

    # clock generator
    sys_c = system_common()

    # create components
    cpuA = processor('cpuA', testcase_id_path, expected_result_path)
    cpuB = processor('cpuB', testcase_id_path, expected_result_path)

    cacheA = cache_L1('cacheA', expected_result_path)
    cacheB = cache_L1('cacheB', expected_result_path)
    deadlock_handler_ = deadlock_handler('Deadlock_Handler')

    AXI_Coherence = Interconnect('AXI_Coherence')

    Mem = main_memory('Mem', testcase_id_path, expected_result_path)

    # connection between cpu and cache
    cpuA.s_port.send_port = cacheA.m_port.send_port
    cpuA.s_port.recv_port = cacheA.m_port.recv_port

    cpuB.s_port.send_port = cacheB.m_port.send_port
    cpuB.s_port.recv_port = cacheB.m_port.recv_port

    # connection between 2 cache
    deadlock_handler_.cache_L1_0 = cacheA
    deadlock_handler_.cache_L1_1 = cacheB

    cacheA.other_cache = cacheB
    cacheB.other_cache = cacheA

    cacheA.resp_port.send_port = cacheB.req_port.send_port
    cacheA.resp_port.recv_port = cacheB.req_port.recv_port

    cacheB.resp_port.send_port = cacheA.req_port.send_port
    cacheB.resp_port.recv_port = cacheA.req_port.recv_port

    # connection between cache and bus
    cacheA.s_port.send_port = AXI_Coherence.m0_port.send_port
    cacheA.s_port.recv_port = AXI_Coherence.m0_port.recv_port

    cacheB.s_port.send_port = AXI_Coherence.m1_port.send_port
    cacheB.s_port.recv_port = AXI_Coherence.m1_port.recv_port

    # connection between bus and dram
    AXI_Coherence.s_port.send_port = Mem.m_port.send_port
    AXI_Coherence.s_port.recv_port = Mem.m_port.recv_port

    while sys_c.cycle <= SIMULATION_TIME:
        cpuA.run(sys_c)
        cpuB.run(sys_c)
        deadlock_handler_.run(sys_c)
        cacheA.run(sys_c)
        cacheB.run(sys_c)
        AXI_Coherence.run(sys_c)
        Mem.run(sys_c)

        # Components update
        cpuA.update()
        cpuB.update()
        cacheA.update()
        cacheB.update()
        AXI_Coherence.update()
        Mem.update()

        # this is rising edge
        sys_c.clk_posedge()

    cacheA.save_state_tag()
    cacheB.save_state_tag()

    cacheA.save_plrut()
    cacheB.save_plrut()

    cacheA.save_data()
    cacheB.save_data()

    cpuA.save_read_data()
    cpuB.save_read_data()

    Mem.save_mem()

def run_subsystem():
    testcase = int(input(f"Which testcase do you want to run? \n 0    : runall\n 1-{number_of_testcase}: testcase 1 - testcase {number_of_testcase} \n Your choice: "))

    if testcase == 0:
        for i in range(1, number_of_testcase + 1):
            delete_previous_expected_result(subsystem_expected_result_dir, i)

        # Generate test case IDs from 1 to 119 (as integers)
        testcase_ids = list(range(1, number_of_testcase + 1))  # Creates [1, 2, ..., 115]

        # Run test cases in parallel using 4 worker processes
        with concurrent.futures.ProcessPoolExecutor(max_workers=3) as executor:
            executor.map(run_subsystem_testcase, testcase_ids)

    elif testcase >= 1 and testcase <= number_of_testcase:
        delete_previous_expected_result(subsystem_expected_result_dir, testcase)
        run_subsystem_testcase(testcase)