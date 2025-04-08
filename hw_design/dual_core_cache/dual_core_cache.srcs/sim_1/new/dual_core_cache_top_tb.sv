`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// this is top-testbench of dual core cache
//////////////////////////////////////////////////////////////////////////////////


module dual_core_cache_top_tb();
    parameter DATA_WIDTH = 32;
    parameter ADDR_WIDTH = 32;
    // input files
    parameter INSTR_MEM_0 = "D:/University/KLTN/hw_design/dual_core_cache/dual_core_cache.srcs/sources_1/new/instruction_mem_0.mem";
    parameter INSTR_MEM_1 = "D:/University/KLTN/hw_design/dual_core_cache/dual_core_cache.srcs/sources_1/new/instruction_mem_1.mem";
    parameter CACHE_L2_READ = "D:/University/KLTN/hw_design/dual_core_cache/dual_core_cache.srcs/sources_1/new/cache_L2_read.mem";
    // output files
    parameter CACHE_L2_WRITE = "D:/University/KLTN/hw_design/dual_core_cache/dual_core_cache.srcs/sources_1/new/cache_L2_write.mem";
    parameter STATE_TAG_0 = "D:/University/KLTN/hw_design/dual_core_cache/dual_core_cache.srcs/sources_1/new/state_tag_0.mem";
    parameter STATE_TAG_1 = "D:/University/KLTN/hw_design/dual_core_cache/dual_core_cache.srcs/sources_1/new/state_tag_1.mem";
    parameter PLRUT_RAM_0 = "D:/University/KLTN/hw_design/dual_core_cache/dual_core_cache.srcs/sources_1/new/plrut_ram_0.mem";
    parameter PLRUT_RAM_1 = "D:/University/KLTN/hw_design/dual_core_cache/dual_core_cache.srcs/sources_1/new/plrut_ram_1.mem";
    parameter DATA_RAM_0 = "D:/University/KLTN/hw_design/dual_core_cache/dual_core_cache.srcs/sources_1/new/data_ram_0.mem";
    parameter DATA_RAM_1 = "D:/University/KLTN/hw_design/dual_core_cache/dual_core_cache.srcs/sources_1/new/data_ram_1.mem";
    parameter READ_DATA_0 = "D:/University/KLTN/hw_design/dual_core_cache/dual_core_cache.srcs/sources_1/new/read_data_0.mem";
    parameter READ_DATA_1 = "D:/University/KLTN/hw_design/dual_core_cache/dual_core_cache.srcs/sources_1/new/read_data_1.mem";

    bit SystemClock; 
    
    // Instantiate the interface with custom parameters
    dual_core_cache_if #(
        .DATA_WIDTH(DATA_WIDTH),
        .ADDR_WIDTH(ADDR_WIDTH),
        .INSTR_MEM_0(INSTR_MEM_0),
        .INSTR_MEM_1(INSTR_MEM_1),
        .CACHE_L2_READ(CACHE_L2_READ),
        .CACHE_L2_WRITE(CACHE_L2_WRITE),
        .STATE_TAG_0(STATE_TAG_0),
        .STATE_TAG_1(STATE_TAG_1),
        .PLRUT_RAM_0(PLRUT_RAM_0),
        .PLRUT_RAM_1(PLRUT_RAM_1),
        .DATA_RAM_0(DATA_RAM_0),
        .DATA_RAM_1(DATA_RAM_1),
        .READ_DATA_0(READ_DATA_0),
        .READ_DATA_1(READ_DATA_1)
    ) m_if (.ACLK(SystemClock)); // Connect clock signal
    
    initial begin
        forever
            #5 SystemClock = ~SystemClock;
    end
    
    initial begin
        $display("[%0t(ns)] Start simulation!", $time);
        m_if.init_all();
        m_if.reset_n();
        m_if.run_all();
        m_if.save_all(
            DUT.core_0_cache.way0.state_tag_ram,
            DUT.core_0_cache.way1.state_tag_ram,
            DUT.core_0_cache.way2.state_tag_ram,
            DUT.core_0_cache.way3.state_tag_ram,
            DUT.core_1_cache.way0.state_tag_ram,
            DUT.core_1_cache.way1.state_tag_ram,
            DUT.core_1_cache.way2.state_tag_ram,
            DUT.core_1_cache.way3.state_tag_ram,
            
            DUT.core_0_cache.plrut_ram.plrut_ram,
            DUT.core_1_cache.plrut_ram.plrut_ram,
            
            DUT.core_0_cache.cache_data_ram.cache,
            DUT.core_1_cache.cache_data_ram.cache
            );
        $display("[%0t(ns)] Finish simulation!", $time);
    end
    
    dual_core_cache DUT
    (
        // system signals
        .ACLK(m_if.ACLK),
        .ARESETn(m_if.ARESETn),
        
        // core_0 cache
        .ENABLE_0(m_if.ENABLE_0),
        .CACHE_HIT_0(m_if.CACHE_HIT_0),
        .CACHE_BUSY_0(m_if.CACHE_BUSY_0),
        
        // AXI5-Lite Interface (connect with CPU)
        // AW Channel
        .m_AWVALID_0(m_if.m_AWVALID_0),
        .m_AWREADY_0(m_if.m_AWREADY_0),
        .m_AWADDR_0(m_if.m_AWADDR_0),
        
        // W Channel
        .m_WVALID_0(m_if.m_WVALID_0),
        .m_WREADY_0(m_if.m_WREADY_0),
        .m_WDATA_0(m_if.m_WDATA_0),
        .m_WSTRB_0(m_if.m_WSTRB_0), // use default value: 0xF
        
        // B Channel
        .m_BVALID_0(m_if.m_BVALID_0),
        .m_BREADY_0(m_if.m_BREADY_0),
        .m_BRESP_0(m_if.m_BRESP_0),
        
        // AR Channel
        .m_ARVALID_0(m_if.m_ARVALID_0),
        .m_ARREADY_0(m_if.m_ARREADY_0),
        .m_ARADDR_0(m_if.m_ARADDR_0),
        
        // R Channel
        .m_RVALID_0(m_if.m_RVALID_0),
        .m_RREADY_0(m_if.m_RREADY_0),
        .m_RDATA_0(m_if.m_RDATA_0),
        .m_RRESP_0(m_if.m_RRESP_0),
        
        // AXI5 Interface (connect with Cache L2)
        // AW Channel
        .s_AWID_0(m_if.s_AWID_0), // use default value: 0x0
        .s_AWADDR_0(m_if.s_AWADDR_0),
        .s_AWLEN_0(m_if.s_AWLEN_0),
        .s_AWSIZE_0(m_if.s_AWSIZE_0),  // use default value: Data bus width = 32-bit -> AWSIZE = 0x2
        .s_AWBURST_0(m_if.s_AWBURST_0), // use default value: 0x1_0(), INCR   
        .s_AWVALID_0(m_if.s_AWVALID_0),
        .s_AWREADY_0(m_if.s_AWREADY_0),
        
        // W Channel
        .s_WID_0(m_if.s_WID_0),  // use default value: 0x0
        .s_WDATA_0(m_if.s_WDATA_0),
        .s_WSTRB_0(m_if.s_WSTRB_0),  // use default value: 0xF
        .s_WLAST_0(m_if.s_WLAST_0),
        .s_WVALID_0(m_if.s_WVALID_0),
        .s_WREADY_0(m_if.s_WREADY_0),
        
        // B Channel
        .s_BID_0(m_if.s_BID_0),  // use default value: 0x0
        .s_BRESP_0(m_if.s_BRESP_0),  
        .s_BVALID_0(m_if.s_BVALID_0),
        .s_BREADY_0(m_if.s_BREADY_0),
        
        // AR Channel
        .s_ARID_0(m_if.s_ARID_0), // use default value: 0x0
        .s_ARADDR_0(m_if.s_ARADDR_0),
        .s_ARLEN_0(m_if.s_ARLEN_0),
        .s_ARSIZE_0(m_if.s_ARSIZE_0),  // use default value: Data bus width = 32-bit -> ARSIZE = 0x2
        .s_ARBURST_0(m_if.s_ARBURST_0), // use default value: 0x1_0(), INCR  
        .s_ARVALID_0(m_if.s_ARVALID_0),
        .s_ARREADY_0(m_if.s_ARREADY_0),
        
        // R Channel
        .s_RID_0(m_if.s_RID_0),  // use default value: 0x0
        .s_RDATA_0(m_if.s_RDATA_0),
        .s_RRESP_0(m_if.s_RRESP_0),
        .s_RLAST_0(m_if.s_RLAST_0),
        .s_RVALID_0(m_if.s_RVALID_0),
        .s_RREADY_0(m_if.s_RREADY_0),
        
        // core_1 cache
        .ENABLE_1(m_if.ENABLE_1),
        .CACHE_HIT_1(m_if.CACHE_HIT_1),
        .CACHE_BUSY_1(m_if.CACHE_BUSY_1),
        
        // AXI5-Lite Interface (connect with CPU)
        // AW Channel
        .m_AWVALID_1(m_if.m_AWVALID_1),
        .m_AWREADY_1(m_if.m_AWREADY_1),
        .m_AWADDR_1(m_if.m_AWADDR_1),
        
        // W Channel
        .m_WVALID_1(m_if.m_WVALID_1),
        .m_WREADY_1(m_if.m_WREADY_1),
        .m_WDATA_1(m_if.m_WDATA_1),
        .m_WSTRB_1(m_if.m_WSTRB_1), // use default value: 0xF
        
        // B Channel
        .m_BVALID_1(m_if.m_BVALID_1),
        .m_BREADY_1(m_if.m_BREADY_1),
        .m_BRESP_1(m_if.m_BRESP_1),
        
        // AR Channel
        .m_ARVALID_1(m_if.m_ARVALID_1),
        .m_ARREADY_1(m_if.m_ARREADY_1),
        .m_ARADDR_1(m_if.m_ARADDR_1),
        
        // R Channel
        .m_RVALID_1(m_if.m_RVALID_1),
        .m_RREADY_1(m_if.m_RREADY_1),
        .m_RDATA_1(m_if.m_RDATA_1),
        .m_RRESP_1(m_if.m_RRESP_1),
        
        // AXI5 Interface (connect with Cache L2)
        // AW Channel
        .s_AWID_1(m_if.s_AWID_1), // use default value: 0x0
        .s_AWADDR_1(m_if.s_AWADDR_1),
        .s_AWLEN_1(m_if.s_AWLEN_1),
        .s_AWSIZE_1(m_if.s_AWSIZE_1),  // use default value: Data bus width = 32-bit -> AWSIZE = 0x2
        .s_AWBURST_1(m_if.s_AWBURST_1), // use default value: 0x1_1(), INCR   
        .s_AWVALID_1(m_if.s_AWVALID_1),
        .s_AWREADY_1(m_if.s_AWREADY_1),
        
        // W Channel
        .s_WID_1(m_if.s_WID_1),  // use default value: 0x0
        .s_WDATA_1(m_if.s_WDATA_1),
        .s_WSTRB_1(m_if.s_WSTRB_1),  // use default value: 0xF
        .s_WLAST_1(m_if.s_WLAST_1),
        .s_WVALID_1(m_if.s_WVALID_1),
        .s_WREADY_1(m_if.s_WREADY_1),
        
        // B Channel
        .s_BID_1(m_if.s_BID_1),  // use default value: 0x0
        .s_BRESP_1(m_if.s_BRESP_1),  
        .s_BVALID_1(m_if.s_BVALID_1),
        .s_BREADY_1(m_if.s_BREADY_1),
        
        // AR Channel
        .s_ARID_1(m_if.s_ARID_1), // use default value: 0x0
        .s_ARADDR_1(m_if.s_ARADDR_1),
        .s_ARLEN_1(m_if.s_ARLEN_1),
        .s_ARSIZE_1(m_if.s_ARSIZE_1),  // use default value: Data bus width = 32-bit -> ARSIZE = 0x2
        .s_ARBURST_1(m_if.s_ARBURST_1), // use default value: 0x1_1(), INCR  
        .s_ARVALID_1(m_if.s_ARVALID_1),
        .s_ARREADY_1(m_if.s_ARREADY_1),
        
        // R Channel
        .s_RID_1(m_if.s_RID_1),  // use default value: 0x0
        .s_RDATA_1(m_if.s_RDATA_1),
        .s_RRESP_1(m_if.s_RRESP_1),
        .s_RLAST_1(m_if.s_RLAST_1),
        .s_RVALID_1(m_if.s_RVALID_1),
        .s_RREADY_1(m_if.s_RREADY_1)
    );
    
endmodule
