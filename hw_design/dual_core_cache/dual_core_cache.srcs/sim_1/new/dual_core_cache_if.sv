`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// this is definition of dual_core_cache interface
//////////////////////////////////////////////////////////////////////////////////

interface dual_core_cache_if 
#(
    parameter DATA_WIDTH = 32,
    parameter ADDR_WIDTH = 32,
    // input files
    parameter INSTR_MEM_0 = "D:/University/KLTN/hw_design/dual_core_cache/dual_core_cache.srcs/sources_1/new/instruction_mem_0.mem",
    parameter INSTR_MEM_1 = "D:/University/KLTN/hw_design/dual_core_cache/dual_core_cache.srcs/sources_1/new/instruction_mem_1.mem",
    parameter CACHE_L2_READ = "D:/University/KLTN/hw_design/dual_core_cache/dual_core_cache.srcs/sources_1/new/cache_L2_read.mem",
    // output files
    parameter CACHE_L2_WRITE = "D:/University/KLTN/hw_design/dual_core_cache/dual_core_cache.srcs/sources_1/new/cache_L2_write.mem",
    parameter STATE_TAG_0 = "D:/University/KLTN/hw_design/dual_core_cache/dual_core_cache.srcs/sources_1/new/state_tag_0.mem",
    parameter STATE_TAG_1 = "D:/University/KLTN/hw_design/dual_core_cache/dual_core_cache.srcs/sources_1/new/state_tag_1.mem",
    parameter PLRUT_RAM_0 = "D:/University/KLTN/hw_design/dual_core_cache/dual_core_cache.srcs/sources_1/new/plrut_ram_0.mem",
    parameter PLRUT_RAM_1 = "D:/University/KLTN/hw_design/dual_core_cache/dual_core_cache.srcs/sources_1/new/plrut_ram_1.mem",
    parameter DATA_RAM_0 = "D:/University/KLTN/hw_design/dual_core_cache/dual_core_cache.srcs/sources_1/new/data_ram_0.mem",
    parameter DATA_RAM_1 = "D:/University/KLTN/hw_design/dual_core_cache/dual_core_cache.srcs/sources_1/new/data_ram_1.mem",
    parameter READ_DATA_0 = "D:/University/KLTN/hw_design/dual_core_cache/dual_core_cache.srcs/sources_1/new/read_data_0.mem",
    parameter READ_DATA_1 = "D:/University/KLTN/hw_design/dual_core_cache/dual_core_cache.srcs/sources_1/new/read_data_1.mem"
) (input bit ACLK);

    // System Signals
    logic   ARESETn;
    
    // Core 0 Cache
    logic   ENABLE_0;
    logic   CACHE_HIT_0;
    logic   CACHE_BUSY_0;
    
    // AXI5-Lite Interface (connect with CPU)
    // AW Channel
    logic   m_AWVALID_0;
    logic   m_AWREADY_0;
    logic   [ADDR_WIDTH-1:0] m_AWADDR_0;
    
    // W Channel
    logic   m_WVALID_0;
    logic   m_WREADY_0;
    logic   [DATA_WIDTH-1:0] m_WDATA_0;
    logic   [3:0] m_WSTRB_0;
    
    // B Channel
    logic   m_BVALID_0;
    logic   m_BREADY_0;
    logic   [1:0] m_BRESP_0;
    
    // AR Channel
    logic   m_ARVALID_0;
    logic   m_ARREADY_0;
    logic   [ADDR_WIDTH-1:0] m_ARADDR_0;
    
    // R Channel
    logic   m_RVALID_0;
    logic   m_RREADY_0;
    logic   [DATA_WIDTH-1:0] m_RDATA_0;
    logic   [1:0] m_RRESP_0;
    
    // AXI5 Interface (connect with Cache L2)
    // AW Channel
    logic   s_AWID_0;
    logic   [ADDR_WIDTH-1:0] s_AWADDR_0;
    logic   [3:0] s_AWLEN_0;
    logic   [2:0] s_AWSIZE_0;
    logic   [1:0] s_AWBURST_0;
    logic   s_AWVALID_0;
    logic   s_AWREADY_0;
    
    // W Channel
    logic   s_WID_0;
    logic   [DATA_WIDTH-1:0] s_WDATA_0;
    logic   [3:0] s_WSTRB_0;
    logic   s_WLAST_0;
    logic   s_WVALID_0;
    logic   s_WREADY_0;
    
    // B Channel
    logic   s_BID_0;
    logic   [1:0] s_BRESP_0;
    logic   s_BVALID_0;
    logic   s_BREADY_0;
    
    // AR Channel
    logic   s_ARID_0;
    logic   [ADDR_WIDTH-1:0] s_ARADDR_0;
    logic   [3:0] s_ARLEN_0;
    logic   [2:0] s_ARSIZE_0;
    logic   [1:0] s_ARBURST_0;
    logic   s_ARVALID_0;
    logic   s_ARREADY_0;
    
    // R Channel
    logic   s_RID_0;
    logic   [DATA_WIDTH-1:0] s_RDATA_0;
    logic   [1:0] s_RRESP_0;
    logic   s_RLAST_0;
    logic   s_RVALID_0;
    logic   s_RREADY_0;
    
    // Core 1 Cache
    logic   ENABLE_1;
    logic   CACHE_HIT_1;
    logic   CACHE_BUSY_1;
    
    // AXI5-Lite Interface (connect with CPU)
    // AW Channel
    logic   m_AWVALID_1;
    logic   m_AWREADY_1;
    logic   [ADDR_WIDTH-1:0] m_AWADDR_1;
    
    // W Channel
    logic   m_WVALID_1;
    logic   m_WREADY_1;
    logic   [DATA_WIDTH-1:0] m_WDATA_1;
    logic   [3:0] m_WSTRB_1;
    
    // B Channel
    logic   m_BVALID_1;
    logic   m_BREADY_1;
    logic   [1:0] m_BRESP_1;
    
    // AR Channel
    logic   m_ARVALID_1;
    logic   m_ARREADY_1;
    logic   [ADDR_WIDTH-1:0] m_ARADDR_1;
    
    // R Channel
    logic   m_RVALID_1;
    logic   m_RREADY_1;
    logic   [DATA_WIDTH-1:0] m_RDATA_1;
    logic   [1:0] m_RRESP_1;
    
    // AXI5 Interface (connect with Cache L2)
    // AW Channel
    logic   s_AWID_1;
    logic   [ADDR_WIDTH-1:0] s_AWADDR_1;
    logic   [3:0] s_AWLEN_1;
    logic   [2:0] s_AWSIZE_1;
    logic   [1:0] s_AWBURST_1;
    logic   s_AWVALID_1;
    logic   s_AWREADY_1;
    
    // W Channel
    logic   s_WID_1;
    logic   [DATA_WIDTH-1:0] s_WDATA_1;
    logic   [3:0] s_WSTRB_1;
    logic   s_WLAST_1;
    logic   s_WVALID_1;
    logic   s_WREADY_1;
    
    // B Channel
    logic   s_BID_1;
    logic   [1:0] s_BRESP_1;
    logic   s_BVALID_1;
    logic   s_BREADY_1;
    
    // AR Channel
    logic   s_ARID_1;
    logic   [ADDR_WIDTH-1:0] s_ARADDR_1;
    logic   [3:0] s_ARLEN_1;
    logic   [2:0] s_ARSIZE_1;
    logic   [1:0] s_ARBURST_1;
    logic   s_ARVALID_1;
    logic   s_ARREADY_1;
    
    // R Channel
    logic   s_RID_1;
    logic   [DATA_WIDTH-1:0] s_RDATA_1;
    logic   [1:0] s_RRESP_1;
    logic   s_RLAST_1;
    logic   s_RVALID_1;
    logic   s_RREADY_1;

    // for instruction mem
    typedef struct packed {
        bit [ADDR_WIDTH-1:0] addr;
        bit [DATA_WIDTH-1:0] data;
        bit instr_type;
    } instruction_s;
    
    // for read/write trans from/to Cache L2
    typedef struct {
        bit [ADDR_WIDTH-1:0] addr;
        bit [DATA_WIDTH-1:0] data [0:15];
    } cache_block_s;
    
    // for read trans from CPU
    typedef struct packed {
        bit [ADDR_WIDTH-1:0] addr;
        bit [DATA_WIDTH-1:0] data;
    } cache_word_s;
    
    instruction_s cpu0_instr_mem[$];
    instruction_s cpu1_instr_mem[$];
    
    cache_block_s cache_L2_read [$];
    cache_block_s cache_L2_write [$];
    
    cache_word_s read_data_0[$];
    cache_word_s read_data_1[$];
    
    // Clocking Block
    clocking drv_cb @(posedge ACLK);
        // system signals
        output ARESETn;
        
        // core_0 cache
        output ENABLE_0;
        
        // AXI5-Lite Interface (connect with CPU)
        // AW Channel
        output m_AWVALID_0;
        output m_AWADDR_0;
        
        // W Channel
        output m_WVALID_0;
        output m_WDATA_0;
        output m_WSTRB_0; // use default value: 0xF
        
        // B Channel
        output m_BREADY_0;
        
        // AR Channel
        output m_ARVALID_0;
        output m_ARADDR_0;
        
        // R Channel
        output m_RREADY_0;
        
        // AXI5 Interface (connect with Cache L2)
        // AW Channel
        output s_AWREADY_0;
        
        // W Channel
        output s_WREADY_0;
        
        // B Channel
        output s_BID_0;  // use default value: 0x0
        output s_BRESP_0;  
        output s_BVALID_0;
        
        // AR Channel
        output s_ARREADY_0;
        
        // R Channel
        output s_RID_0;  // use default value: 0x0
        output s_RDATA_0;
        output s_RRESP_0;
        output s_RLAST_0;
        output s_RVALID_0;
        
        // core_1 cache
        output ENABLE_1;
        
        // AXI5-Lite Interface (connect with CPU)
        // AW Channel
        output m_AWVALID_1;
        output m_AWADDR_1;
        
        // W Channel
        output m_WVALID_1;
        output m_WDATA_1;
        output m_WSTRB_1; // use default value: 0xF
        
        // B Channel
        output m_BREADY_1;
        
        // AR Channel
        output m_ARVALID_1;
        output m_ARADDR_1;
        
        // R Channel
        output m_RREADY_1;
        
        // AXI5 Interface (connect with Cache L2)
        // AW Channel
        output s_AWREADY_1;
        
        // W Channel
        output s_WREADY_1;
        
        // B Channel
        output s_BID_1;  // use default value: 0x0
        output s_BRESP_1;  
        output s_BVALID_1;
        
        // AR Channel
        output s_ARREADY_1;
        
        // R Channel
        output s_RID_1;  // use default value: 0x0
        output s_RDATA_1;
        output s_RRESP_1;
        output s_RLAST_1;
        output s_RVALID_1;
    endclocking
    
    clocking mon_cb @(posedge ACLK);
        // system signals
        input  ARESETn;
        
        // core_0 cache
        input  ENABLE_0;
        input  CACHE_HIT_0;
        input  CACHE_BUSY_0;
        
        // AXI5-Lite Interface (connect with CPU)
        // AW Channel
        input  m_AWVALID_0;
        input  m_AWREADY_0;
        input  m_AWADDR_0;
        
        // W Channel
        input  m_WVALID_0;
        input  m_WREADY_0;
        input  m_WDATA_0;
        input  m_WSTRB_0; // use default value: 0xF
        
        // B Channel
        input  m_BVALID_0;
        input  m_BREADY_0;
        input  m_BRESP_0;
        
        // AR Channel
        input  m_ARVALID_0;
        input  m_ARREADY_0;
        input  m_ARADDR_0;
        
        // R Channel
        input  m_RVALID_0;
        input  m_RREADY_0;
        input  m_RDATA_0;
        input  m_RRESP_0;
        
        // AXI5 Interface (connect with Cache L2)
        // AW Channel
        input  s_AWID_0; // use default value: 0x0
        input  s_AWADDR_0;
        input  s_AWLEN_0;
        input  s_AWSIZE_0;  // use default value: Data bus width = 32-bit -> AWSIZE = 0x2
        input  s_AWBURST_0; // use default value: 0x1_0; INCR   
        input  s_AWVALID_0;
        input  s_AWREADY_0;
        
        // W Channel
        input  s_WID_0;  // use default value: 0x0
        input  s_WDATA_0;
        input  s_WSTRB_0;  // use default value: 0xF
        input  s_WLAST_0;
        input  s_WVALID_0;
        input  s_WREADY_0;
        
        // B Channel
        input  s_BID_0;  // use default value: 0x0
        input  s_BRESP_0;  
        input  s_BVALID_0;
        input  s_BREADY_0;
        
        // AR Channel
        input  s_ARID_0; // use default value: 0x0
        input  s_ARADDR_0;
        input  s_ARLEN_0;
        input  s_ARSIZE_0;  // use default value: Data bus width = 32-bit -> ARSIZE = 0x2
        input  s_ARBURST_0; // use default value: 0x1_0; INCR  
        input  s_ARVALID_0;
        input  s_ARREADY_0;
        
        // R Channel
        input  s_RID_0;  // use default value: 0x0
        input  s_RDATA_0;
        input  s_RRESP_0;
        input  s_RLAST_0;
        input  s_RVALID_0;
        input  s_RREADY_0;
        
        // core_1 cache
        input  ENABLE_1;
        input  CACHE_HIT_1;
        input  CACHE_BUSY_1;
        
        // AXI5-Lite Interface (connect with CPU)
        // AW Channel
        input  m_AWVALID_1;
        input  m_AWREADY_1;
        input  m_AWADDR_1;
        
        // W Channel
        input  m_WVALID_1;
        input  m_WREADY_1;
        input  m_WDATA_1;
        input  m_WSTRB_1; // use default value: 0xF
        
        // B Channel
        input  m_BVALID_1;
        input  m_BREADY_1;
        input  m_BRESP_1;
        
        // AR Channel
        input  m_ARVALID_1;
        input  m_ARREADY_1;
        input  m_ARADDR_1;
        
        // R Channel
        input  m_RVALID_1;
        input  m_RREADY_1;
        input  m_RDATA_1;
        input  m_RRESP_1;
        
        // AXI5 Interface (connect with Cache L2)
        // AW Channel
        input  s_AWID_1; // use default value: 0x0
        input  s_AWADDR_1;
        input  s_AWLEN_1;
        input  s_AWSIZE_1;  // use default value: Data bus width = 32-bit -> AWSIZE = 0x2
        input  s_AWBURST_1; // use default value: 0x1_1; INCR   
        input  s_AWVALID_1;
        input  s_AWREADY_1;
        
        // W Channel
        input  s_WID_1;  // use default value: 0x0
        input  s_WDATA_1;
        input  s_WSTRB_1;  // use default value: 0xF
        input  s_WLAST_1;
        input  s_WVALID_1;
        input  s_WREADY_1;
        
        // B Channel
        input  s_BID_1;  // use default value: 0x0
        input  s_BRESP_1;  
        input  s_BVALID_1;
        input  s_BREADY_1;
        
        // AR Channel
        input  s_ARID_1; // use default value: 0x0
        input  s_ARADDR_1;
        input  s_ARLEN_1;
        input  s_ARSIZE_1;  // use default value: Data bus width = 32-bit -> ARSIZE = 0x2
        input  s_ARBURST_1; // use default value: 0x1_1; INCR  
        input  s_ARVALID_1;
        input  s_ARREADY_1;
        
        // R Channel
        input  s_RID_1;  // use default value: 0x0
        input  s_RDATA_1;
        input  s_RRESP_1;
        input  s_RLAST_1;
        input  s_RVALID_1;
        input  s_RREADY_1;
    endclocking
    
    task reset_n();
        $display("[%0t(ns)] Starting reset!", $time);
        // System signals
        drv_cb.ARESETn <= 0;
        
        // Core 0 cache signals
        drv_cb.ENABLE_0 <= 0;
        
        // AXI5-Lite Interface (Core 0)
        drv_cb.m_AWVALID_0 <= 0;
        drv_cb.m_AWADDR_0 <= 0;
        drv_cb.m_WVALID_0 <= 0;
        drv_cb.m_WDATA_0 <= 0;
        drv_cb.m_WSTRB_0 <= 0;
        drv_cb.m_BREADY_0 <= 0;
        drv_cb.m_ARVALID_0 <= 0;
        drv_cb.m_ARADDR_0 <= 0;
        drv_cb.m_RREADY_0 <= 0;
        
        // AXI5 Interface (Core 0 -> Cache L2)
        drv_cb.s_AWREADY_0 <= 0;
        drv_cb.s_WREADY_0 <= 0;
        drv_cb.s_BID_0 <= 0;
        drv_cb.s_BRESP_0 <= 0;
        drv_cb.s_BVALID_0 <= 0;
        drv_cb.s_ARREADY_0 <= 0;
        drv_cb.s_RID_0 <= 0;
        drv_cb.s_RDATA_0 <= 0;
        drv_cb.s_RRESP_0 <= 0;
        drv_cb.s_RLAST_0 <= 0;
        drv_cb.s_RVALID_0 <= 0;
        
        // Core 1 cache signals
        drv_cb.ENABLE_1 <= 0;
        
        // AXI5-Lite Interface (Core 1)
        drv_cb.m_AWVALID_1 <= 0;
        drv_cb.m_AWADDR_1 <= 0;
        drv_cb.m_WVALID_1 <= 0;
        drv_cb.m_WDATA_1 <= 0;
        drv_cb.m_WSTRB_1 <= 0;
        drv_cb.m_BREADY_1 <= 0;
        drv_cb.m_ARVALID_1 <= 0;
        drv_cb.m_ARADDR_1 <= 0;
        drv_cb.m_RREADY_1 <= 0;
        
        // AXI5 Interface (Core 1 -> Cache L2)
        drv_cb.s_AWREADY_1 <= 0;
        drv_cb.s_WREADY_1 <= 0;
        drv_cb.s_BID_1 <= 0;
        drv_cb.s_BRESP_1 <= 0;
        drv_cb.s_BVALID_1 <= 0;
        drv_cb.s_ARREADY_1 <= 0;
        drv_cb.s_RID_1 <= 0;
        drv_cb.s_RDATA_1 <= 0;
        drv_cb.s_RRESP_1 <= 0;
        drv_cb.s_RLAST_1 <= 0;
        drv_cb.s_RVALID_1 <= 0;
        
        // Hold reset for a few clock cycles
        repeat (5) @(posedge drv_cb);
        drv_cb.ARESETn <= 1;
        drv_cb.ENABLE_0 <= 1;
        drv_cb.ENABLE_1 <= 1;
        $display("[%0t(ns)] Finishing reset!", $time);
    endtask
    
    task run_all();
        fork
            // core_0 run
            begin
                $display("[%0t(ns)] CPU_0 start!", $time);
                foreach(cpu0_instr_mem[i]) begin
                    cache_word_s read_out_trans;
                    if (cpu0_instr_mem[i].instr_type) begin
                        cpu0_write(cpu0_instr_mem[i].addr, cpu0_instr_mem[i].data);
                    end
                    else begin
                        cpu0_read(cpu0_instr_mem[i].addr, cpu0_instr_mem[i].data);
                        read_out_trans.addr = cpu0_instr_mem[i].addr;
                        read_out_trans.data = cpu0_instr_mem[i].data;
                        read_data_0.push_back(read_out_trans);
                    end
                end
                $display("[%0t(ns)] CPU_0 finish!", $time);
            end
            // core_1 run
            begin
                $display("[%0t(ns)] CPU_1 start!", $time);
                foreach(cpu1_instr_mem[i]) begin
                    cache_word_s read_out_trans;
                    if (cpu1_instr_mem[i].instr_type) begin
                        cpu1_write(cpu1_instr_mem[i].addr, cpu1_instr_mem[i].data);
                    end
                    else begin
                        cpu1_read(cpu1_instr_mem[i].addr, cpu1_instr_mem[i].data);
                        read_out_trans.addr = cpu1_instr_mem[i].addr;
                        read_out_trans.data = cpu1_instr_mem[i].data;
                        read_data_1.push_back(read_out_trans);
                    end
                end
                $display("[%0t(ns)] CPU_1 finish!", $time);
            end
            // drive read response for read req to fecth Cache L2
            begin
                core0_read_cache_L2();
            end
            begin
                core1_read_cache_L2();
            end
            // capture read data response to CPU
            begin
            
            end
            // capture write-back trans to Cache L2
            begin
            
            end
        join
    endtask

    task cpu0_read(input bit [31:0] read_addr, output bit [31:0] read_data);
        $display("[%0t(ns)] CPU_0 start reading from Address = 0x%h", $time, read_addr);
        @(drv_cb);
        drv_cb.m_ARVALID_0 <= 1;
        drv_cb.m_ARADDR_0 <= read_addr;
        do begin
            @(drv_cb);
        end while (!mon_cb.m_ARREADY_0);
        drv_cb.m_ARVALID_0 <= 0;
        drv_cb.m_RREADY_0 <= 1;
        do begin
            @(drv_cb);
        end while (!mon_cb.m_RVALID_0);
        read_data = mon_cb.m_RDATA_0;
        drv_cb.m_RREADY_0 <= 0;
        @(drv_cb);
        $display("[%0t(ns)] CPU_0 finish reading from Address = 0x%h, Data = 0x%h", $time, read_addr, read_data);
    endtask
    
    task cpu0_write(input bit [31:0] write_addr, input bit [31:0] write_data);
        $display("[%0t(ns)] CPU_0 start writing from Address = 0x%h, Data = 0x%h", $time, write_addr, write_data);
        @(drv_cb);
        drv_cb.m_AWVALID_0 <= 1;
        drv_cb.m_AWADDR_0 <= write_addr;
        do begin
            @(drv_cb);
        end while (!mon_cb.m_AWREADY_0);
        drv_cb.m_AWVALID_0 <= 0;
        drv_cb.m_WVALID_0 <= 1;
        drv_cb.m_WDATA_0 <= write_data;
        drv_cb.m_WSTRB_0 <= 4'hF;
        do begin
            @(drv_cb);
        end while (!mon_cb.m_WREADY_1);
        drv_cb.m_WVALID_0 <= 0;
        drv_cb.m_BREADY_0 <= 1;
        do begin
            @(drv_cb);
        end while (!mon_cb.m_BVALID_0);
        drv_cb.m_BREADY_0 <= 0;
        @(drv_cb);
        $display("[%0t(ns)] CPU_0 finish writing from Address = 0x%h, Data = 0x%h", $time, write_addr, write_data);
    endtask
    
    task cpu1_read(input bit [31:0] read_addr, output bit [31:0] read_data);
        $display("[%0t(ns)] CPU_1 start reading from Address = 0x%h", $time, read_addr);
        @(drv_cb);
        drv_cb.m_ARVALID_1 <= 1;
        drv_cb.m_ARADDR_1 <= read_addr;
        do begin
            @(drv_cb);
        end while (!mon_cb.m_ARREADY_1);
        drv_cb.m_ARVALID_1 <= 0;
        drv_cb.m_RREADY_1 <= 1;
        do begin
            @(drv_cb);
        end while (!mon_cb.m_RVALID_1);
        read_data = mon_cb.m_RDATA_1;
        drv_cb.m_RREADY_1 <= 0;
        @(drv_cb);
        $display("[%0t(ns)] CPU_1 finish reading from Address = 0x%h, Data = 0x%h", $time, read_addr, read_data);
    endtask
    
    task cpu1_write(input bit [31:0] write_addr, input bit [31:0] write_data);
        $display("[%0t(ns)] CPU_1 start writing from Address = 0x%h, Data = 0x%h", $time, write_addr, write_data);
        @(drv_cb);
        drv_cb.m_AWVALID_1 <= 1;
        drv_cb.m_AWADDR_1 <= write_addr;
        do begin
            @(drv_cb);
        end while (!mon_cb.m_AWREADY_1);
        drv_cb.m_AWVALID_1 <= 0;
        drv_cb.m_WVALID_1 <= 1;
        drv_cb.m_WDATA_1 <= write_data;
        drv_cb.m_WSTRB_1 <= 4'hF;
        do begin
            @(drv_cb);
        end while (!mon_cb.m_WREADY_1);
        drv_cb.m_WVALID_1 <= 0;
        drv_cb.m_BREADY_1 <= 1;
        do begin
            @(drv_cb);
        end while (!mon_cb.m_BVALID_1);
        drv_cb.m_BREADY_1 <= 0;
        @(drv_cb);
        $display("[%0t(ns)] CPU_1 finish writing from Address = 0x%h, Data = 0x%h", $time, write_addr, write_data);
    endtask
    
    task core0_read_cache_L2 (/*output bit [31:0] cache_L2_read_addr, input bit [511:0] cache_L2_read_data*/);
        cache_block_s hit_block;
        int hit_index = 0;
        bit [31:0] read_addr;
        int cnt = 0;
        @(drv_cb);
        drv_cb.s_ARREADY_0 <= 1;
        do begin
            @(drv_cb);
        end while (!mon_cb.s_ARVALID_0);
        $display("[%0t(ns)] Core_0 start reading from Cache L2", $time);
        read_addr = mon_cb.s_ARADDR_0;
        s_RID_0 <= 0;
        s_RRESP_0 <= 0;
        // s_RVALID_0 <= 1;
        // hit_block = cache_L2_read.find_first with (item.addr == read_addr);
        foreach(cache_L2_read[i]) begin
            if (cache_L2_read[i].addr == read_addr) begin
                hit_index = i;
                break;
            end
        end
        hit_block = cache_L2_read[hit_index];
        do begin
            if (mon_cb.s_RREADY_0) begin
                drv_cb.s_RDATA_0 <= hit_block.data[cnt];
                drv_cb.s_RLAST_0 <= cnt == 15;
                s_RVALID_0 <= 1;
                cnt++;
            end
            @(drv_cb);
        end while (cnt < 16);
        drv_cb.s_RLAST_0 <= 0;
        drv_cb.s_RVALID_0 <= 0;
        @(drv_cb);
        $display("[%0t(ns)] Core_0 finish reading from Cache L2", $time);
    endtask
    
    task core1_read_cache_L2 (/*output bit [31:0] cache_L2_read_addr, input bit [511:0] cache_L2_read_data*/);
        cache_block_s hit_block;
        int hit_index = 0;
        bit [31:0] read_addr;
        int cnt = 0;
        @(drv_cb);
        drv_cb.s_ARREADY_1 <= 1;
        do begin
            @(drv_cb);
        end while (!mon_cb.s_ARVALID_1);
        $display("[%0t(ns)] Core_1 start reading from Cache L2", $time);
        read_addr = mon_cb.s_ARADDR_1;
        s_RID_1 <= 0;
        s_RRESP_1 <= 0;
        // s_RVALID_1 <= 1;
        // hit_block = cache_L2_read.find_first with (item.addr == read_addr);
        foreach(cache_L2_read[i]) begin
            if (cache_L2_read[i].addr == read_addr) begin
                hit_index = i;
                break;
            end
        end
        hit_block = cache_L2_read[hit_index];
        do begin
            if (mon_cb.s_RREADY_1) begin
                drv_cb.s_RDATA_1 <= hit_block.data[cnt];
                drv_cb.s_RLAST_1 <= cnt == 15;
                s_RVALID_1 <= 1;
                cnt++;
            end
            @(drv_cb);
        end while (cnt < 16);
        drv_cb.s_RLAST_1 <= 0;
        drv_cb.s_RVALID_1 <= 0;
        @(drv_cb);
        $display("[%0t(ns)] Core_1 finish reading from Cache L2", $time);
    endtask
    
//    task core0_write_cache_L2 (output bit [31:0] cache_L2_write_addr, output bit [511:0] cache_L2_write_data);
    
//    endtask

    function void init_all();
        // load instruction from file
        load_instr_mem(INSTR_MEM_0, cpu0_instr_mem);
        load_instr_mem(INSTR_MEM_1, cpu1_instr_mem);
        // load date fetch from cache L2 from file
        load_cache_L2(CACHE_L2_READ, cache_L2_read);
    endfunction
    
    function void load_instr_mem(input string path, output instruction_s instr_mem[$]);
        int file;
        string line;
        string op;
        bit [31:0] addr, data;
        int num_tokens = 0;
        
        // Clear the queue before loading new data
        instr_mem.delete(); // Reset the queue
        file = $fopen(path, "r");
        if (file == 0) begin
            $display("Error: Unable to open file %s", path);
            return;
        end
        while (!$feof(file)) begin
            line = "";
            void'($fgets(line, file));
            if (line == "") continue;
            op = "";
            addr = 0;
            data = 0;
            num_tokens = $sscanf(line, "%s %h %h", op, addr, data);
            if (num_tokens >= 2) begin
                instruction_s instr_entry;
                instr_entry.addr = addr;
                if (op == "read") begin
                    instr_entry.instr_type = 1'b0; // Read instruction
                    instr_entry.data = 32'b0; // No data for read operations
                end else if (op == "write" && num_tokens == 3) begin
                    instr_entry.instr_type = 1'b1; // Write instruction
                    instr_entry.data = data;
                end else begin
                    $display("Error: Invalid instruction format");
                    continue;
                end
                instr_mem.push_back(instr_entry); // Add to the queue
            end
        end
        $fclose(file);
    endfunction

    
    function void load_cache_L2(input string path, output cache_block_s cache_L2_read[$]);
        int file;
        bit [7:0] line[256]; // Fixed-size array for line storage
        bit [31:0] addr;
        bit [31:0] data [0:15];
        int num_tokens = 0;
        
        // Clear the queue before loading new data
        cache_L2_read.delete(); // Reset the queue
        file = $fopen(path, "r");
        if (file == 0) begin
            $display("Error: Unable to open file %s", path);
            return;
        end
        while (!$feof(file)) begin
            void'($fgets(line, file)); // Read a line from the file
            // Read address and multiple data values
            num_tokens = $sscanf(line, "0x%h 0x%h 0x%h 0x%h 0x%h 0x%h 0x%h 0x%h 0x%h 0x%h 0x%h 0x%h 0x%h 0x%h 0x%h 0x%h 0x%h", 
                                 addr,
                                 data[15], data[14], data[13], data[12],
                                 data[11], data[10], data[9], data[8],
                                 data[7], data[6], data[5], data[4],
                                 data[3], data[2], data[1], data[0]);
            if (num_tokens >= 2) begin
                cache_block_s cache_entry;
                cache_entry.addr = addr;
                cache_entry.data = data;
                cache_L2_read.push_back(cache_entry); // Add to the queue
            end
        end
        $fclose(file);
    endfunction

    
    function void save_cache_L2(input string path, input cache_block_s cache_L2_write [$]);
        int file = 0;
        int index = 0;
        
        file = $fopen(path, "w");
        if (file == 0) begin
            $display("Error: Unable to open file %s for writing", path);
            return;
        end
        foreach (cache_L2_write[index]) begin
            // Write address followed by 16 data values in a single line
            $fwrite(file, "0x%h", cache_L2_write[index].addr);
            for (int i = 15; i >= 0; i--) begin
                $fwrite(file, " 0x%h", cache_L2_write[index].data[i]);
            end
            $fwrite(file, "\n"); // New line after each entry
        end
        $fclose(file);
    endfunction
    
    task save_state_tag_ram(
        input string path,
        input bit [24:0] state_tag_ram0 [0:15],
        input bit [24:0] state_tag_ram1 [0:15],
        input bit [24:0] state_tag_ram2 [0:15],
        input bit [24:0] state_tag_ram3 [0:15]
    );
        integer file;
        integer i;
    
        // Open the file for writing
        file = $fopen(path, "w");
        if (file == 0) begin
            $display("Error: Unable to open file %s", path);
            return;
        end
        // Write data
        for (i = 0; i < 16; i = i + 1) begin
            $fdisplay(file, "%25b %25b %25b %25b", state_tag_ram0[i], state_tag_ram1[i], state_tag_ram2[i], state_tag_ram3[i]);
        end
        // Close the file
        $fclose(file);
    endtask

    
    task save_plrut_ram(input string path, input [2:0] plrut_ram [0:15]);
        integer file;
        integer i;
    
        // Open the file for writing
        file = $fopen(path, "w");
        if (file == 0) begin
            $display("Error: Unable to open file %s", path);
            return;
        end
        // Write data
        for (i = 0; i < 16; i = i + 1) begin
            $fdisplay(file, "%3b", plrut_ram[i]);
        end
        // Close the file
        $fclose(file);
    endtask
    
    task save_data_ram(input string path, input [31:0] cache [0:1023]);
        integer file;
        integer i, j;
    
        // Open the file for writing
        file = $fopen(path, "w");
        if (file == 0) begin
            $display("Error: Unable to open file %s", path);
            return;
        end
        // Write data
        for (i = 0; i < 64; i = i + 1) begin
            for (j = 15; j >= 0; j--) begin
                $fwrite(file, " 0x%h", cache[i*16+j]);
            end
            $fwrite(file, "\n"); // New line after each entry
        end
        // Close the file
        $fclose(file);
    endtask
    
    task save_read_data(input string path, input cache_word_s read_data[$]);
        integer file;
        integer i, j;
    
        // Open the file for writing
        file = $fopen(path, "w");
        if (file == 0) begin
            $display("Error: Unable to open file %s", path);
            return;
        end
        // Write data
        foreach(read_data[i]) begin
            $fdisplay(file, "0x%h 0x%h", read_data[i].addr, read_data[i].data);
        end
        // Close the file
        $fclose(file);
    endtask
    
    task save_all(
                    input [24:0] state_tag_ram_0_0 [0:15],
                    input [24:0] state_tag_ram_1_0 [0:15],
                    input [24:0] state_tag_ram_2_0 [0:15],
                    input [24:0] state_tag_ram_3_0 [0:15],
                    input [24:0] state_tag_ram_0_1 [0:15],
                    input [24:0] state_tag_ram_1_1 [0:15],
                    input [24:0] state_tag_ram_2_1 [0:15],
                    input [24:0] state_tag_ram_3_1 [0:15], 
                    
                    input [2:0] plrut_ram_0 [0:15],
                    input [2:0] plrut_ram_1 [0:15],
                    
                    input [31:0] cache_data_0 [0:1023],
                    input [31:0] cache_data_1 [0:1023]
                  );
        $display("[%0t(ns)] Start saving simulation result!", $time);
        save_state_tag_ram(STATE_TAG_0, state_tag_ram_0_0, state_tag_ram_1_0, state_tag_ram_2_0, state_tag_ram_3_0);
        save_state_tag_ram(STATE_TAG_1, state_tag_ram_0_1, state_tag_ram_1_1, state_tag_ram_2_1, state_tag_ram_3_1);
        
        save_plrut_ram(PLRUT_RAM_0, plrut_ram_0);
        save_plrut_ram(PLRUT_RAM_1, plrut_ram_1);
        
        save_data_ram(DATA_RAM_0, cache_data_0);
        save_data_ram(DATA_RAM_1, cache_data_1);
        
        save_read_data(READ_DATA_0, read_data_0);
        save_read_data(READ_DATA_1, read_data_1);
        
        save_cache_L2(CACHE_L2_WRITE, cache_L2_write);
        $display("[%0t(ns)] Finish saving simulation result!", $time);
    endtask

endinterface
