`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////


module dual_core_cache_tc_1();
    import axi_api_pkg::*;
    parameter DATA_WIDTH = 32;
    parameter ADDR_WIDTH = 32;
    parameter PATH_WAY0 = "D:/University/KLTN/hw_design/dual_core_cache/dual_core_cache.srcs/sources_1/new/way0.mem";
    parameter PATH_WAY1 = "D:/University/KLTN/hw_design/dual_core_cache/dual_core_cache.srcs/sources_1/new/way1.mem";
    parameter PATH_WAY2 = "D:/University/KLTN/hw_design/dual_core_cache/dual_core_cache.srcs/sources_1/new/way2.mem";
    parameter PATH_WAY3 = "D:/University/KLTN/hw_design/dual_core_cache/dual_core_cache.srcs/sources_1/new/way3.mem";
    parameter PATH_WAY0_result = "D:/University/KLTN/hw_design/dual_core_cache/dual_core_cache.srcs/sources_1/new/way0_result.mem";
    parameter PATH_WAY1_result = "D:/University/KLTN/hw_design/dual_core_cache/dual_core_cache.srcs/sources_1/new/way1_result.mem";
    parameter PATH_WAY2_result = "D:/University/KLTN/hw_design/dual_core_cache/dual_core_cache.srcs/sources_1/new/way2_result.mem";
    parameter PATH_WAY3_result = "D:/University/KLTN/hw_design/dual_core_cache/dual_core_cache.srcs/sources_1/new/way3_result.mem";
    parameter PATH_DATA = "D:/University/KLTN/hw_design/dual_core_cache/dual_core_cache.srcs/sources_1/new/data_ram.mem";
    parameter PATH_DATA_result = "D:/University/KLTN/hw_design/dual_core_cache/dual_core_cache.srcs/sources_1/new/data_ram_result.mem";
    parameter PATH_PLRUT = "D:/University/KLTN/hw_design/dual_core_cache/dual_core_cache.srcs/sources_1/new/plrut_ram.mem";
    parameter PATH_PLRUT_result = "D:/University/KLTN/hw_design/dual_core_cache/dual_core_cache.srcs/sources_1/new/plrut_ram_result.mem";
    parameter PATH_WB_DATA = "D:/University/KLTN/hw_design/dual_core_cache/dual_core_cache.srcs/sources_1/new/wb_data.mem";
    parameter PATH_BUS_SNOOP_DATA = "D:/University/KLTN/hw_design/dual_core_cache/dual_core_cache.srcs/sources_1/new/bus_snoop_data.mem";
    parameter PATH_CACHE_SNOOP_DATA = "D:/University/KLTN/hw_design/dual_core_cache/dual_core_cache.srcs/sources_1/new/cache_snoop_data.mem";
    parameter PATH_MEM_FETCH_DATA = "D:/University/KLTN/hw_design/dual_core_cache/dual_core_cache.srcs/sources_1/new/mem_fetch_data.mem";
    parameter PATH_CPU_READ_DATA = "D:/University/KLTN/hw_design/dual_core_cache/dual_core_cache.srcs/sources_1/new/cpu_read_data.mem";
    parameter PATH_CPU_WRITE_DATA = "D:/University/KLTN/hw_design/dual_core_cache/dual_core_cache.srcs/sources_1/new/cpu_write_data.mem";
    
    // system signals
    bit   ACLK;
    bit   ARESETn;
    
    // core0 signals
    bit   ENABLE_0;
    wire  CACHE_HIT_0;
    wire  CACHE_BUSY_0;
    
    // AXI5-Lite Interface (connect with CPU)
    // AW Channel
    bit   m_AWVALID_0;
    wire  m_AWREADY_0;
    bit   [ADDR_WIDTH-1:0] m_AWADDR_0;
    
    // W Channel
    bit   m_WVALID_0;
    wire  m_WREADY_0;
    bit   [DATA_WIDTH-1:0] m_WDATA_0;
    bit   [3:0] m_WSTRB_0; // use default value: 0xF
    
    // B Channel
    wire  m_BVALID_0;
    bit   m_BREADY_0;
    wire  [1:0] m_BRESP_0;
    
    // AR Channel
    bit   m_ARVALID_0;
    wire  m_ARREADY_0;
    bit   [ADDR_WIDTH-1:0] m_ARADDR_0;
    
    // R Channel
    wire  m_RVALID_0;
    bit   m_RREADY_0;
    wire  [DATA_WIDTH-1:0] m_RDATA_0;
    wire  [1:0] m_RRESP_0;
    
    // AXI5 Interface (connect with Cache L2)
    // AW Channel
    wire  s_AWID_0; // use default value: 0x0
    wire  [ADDR_WIDTH-1:0] s_AWADDR_0;
    wire  [3:0] s_AWLEN_0;
    wire  [2:0] s_AWSIZE_0;  // use default value: Data bus width = 32-bit -> AWSIZE = 0x2
    wire  [1:0] s_AWBURST_0; // use default value: 0x1_0; INCR   
    wire  s_AWVALID_0;
    bit   s_AWREADY_0;
    
    // W Channel
    wire  s_WID_0;  // use default value: 0x0
    wire  [DATA_WIDTH-1:0] s_WDATA_0;
    wire  [3:0] s_WSTRB_0;  // use default value: 0xF
    wire  s_WLAST_0;
    wire  s_WVALID_0;
    bit   s_WREADY_0;
    
    // B Channel
    bit   s_BID_0;  // use default value: 0x0
    bit   [1:0] s_BRESP_0;  
    bit   s_BVALID_0;
    wire  s_BREADY_0;
    
    // AR Channel
    wire  s_ARID_0; // use default value: 0x0
    wire  [ADDR_WIDTH-1:0] s_ARADDR_0;
    wire  [3:0] s_ARLEN_0;
    wire  [2:0] s_ARSIZE_0;  // use default value: Data bus width = 32-bit -> ARSIZE = 0x2
    wire  [1:0] s_ARBURST_0; // use default value: 0x1_0; INCR  
    wire  s_ARVALID_0;
    bit   s_ARREADY_0;
    
    // R Channel
    bit   s_RID_0;  // use default value: 0x0
    bit   [DATA_WIDTH-1:0] s_RDATA_0;
    bit   [1:0] s_RRESP_0;
    bit   s_RLAST_0;
    bit   s_RVALID_0;
    wire  s_RREADY_0;
    
    // Custom Interface (connect with other Cache L1)
    // Snoop Request Channel
    // send request to other Cache L1
    wire  m_ACVALID_0;
    wire   m_ACREADY_0;
    wire  [ADDR_WIDTH-1:0] m_ACADDR_0;
    wire  [1:0] m_ACSNOOP_0;
    // receive response from other Cache L1
    wire   m_CVALID_0;
    wire  m_CREADY_0;
    wire   [DATA_WIDTH-1:0] m_CDATA_0;
    wire   m_CLAST_0;
    wire   m_CHIT_0;
    
    // Snoop Response Channel
    // receive request from other Cache L1
    wire   s_ACVALID_0;
    wire  s_ACREADY_0;
    wire   [ADDR_WIDTH-1:0] s_ACADDR_0;
    wire   [1:0] s_ACSNOOP_0;
    // send response to other Cache L1
    wire  s_CVALID_0;
    wire   s_CREADY_0;
    wire  [DATA_WIDTH-1:0] s_CDATA_0;
    wire  s_CLAST_0;
    wire  s_CHIT_0;
    
    // core0 signals
    bit   ENABLE_1;
    wire  CACHE_HIT_1;
    wire  CACHE_BUSY_1;
    
    // AXI5-Lite Interface (connect with CPU)
    // AW Channel
    bit   m_AWVALID_1;
    wire  m_AWREADY_1;
    bit   [ADDR_WIDTH-1:0] m_AWADDR_1;
    
    // W Channel
    bit   m_WVALID_1;
    wire  m_WREADY_1;
    bit   [DATA_WIDTH-1:0] m_WDATA_1;
    bit   [3:0] m_WSTRB_1; // use default value: 0xF
    
    // B Channel
    wire  m_BVALID_1;
    bit   m_BREADY_1;
    wire  [1:0] m_BRESP_1;
    
    // AR Channel
    bit   m_ARVALID_1;
    wire  m_ARREADY_1;
    bit   [ADDR_WIDTH-1:0] m_ARADDR_1;
    
    // R Channel
    wire  m_RVALID_1;
    bit   m_RREADY_1;
    wire  [DATA_WIDTH-1:0] m_RDATA_1;
    wire  [1:0] m_RRESP_1;
    
    // AXI5 Interface (connect with Cache L2)
    // AW Channel
    wire  s_AWID_1; // use default value: 0x0
    wire  [ADDR_WIDTH-1:0] s_AWADDR_1;
    wire  [3:0] s_AWLEN_1;
    wire  [2:0] s_AWSIZE_1;  // use default value: Data bus width = 32-bit -> AWSIZE = 0x2
    wire  [1:0] s_AWBURST_1; // use default value: 0x1_1; INCR   
    wire  s_AWVALID_1;
    bit   s_AWREADY_1;
    
    // W Channel
    wire  s_WID_1;  // use default value: 0x0
    wire  [DATA_WIDTH-1:0] s_WDATA_1;
    wire  [3:0] s_WSTRB_1;  // use default value: 0xF
    wire  s_WLAST_1;
    wire  s_WVALID_1;
    bit   s_WREADY_1;
    
    // B Channel
    bit   s_BID_1;  // use default value: 0x0
    bit   [1:0] s_BRESP_1;  
    bit   s_BVALID_1;
    wire  s_BREADY_1;
    
    // AR Channel
    wire  s_ARID_1; // use default value: 0x0
    wire  [ADDR_WIDTH-1:0] s_ARADDR_1;
    wire  [3:0] s_ARLEN_1;
    wire  [2:0] s_ARSIZE_1;  // use default value: Data bus width = 32-bit -> ARSIZE = 0x2
    wire  [1:0] s_ARBURST_1; // use default value: 0x1_1; INCR  
    wire  s_ARVALID_1;
    bit   s_ARREADY_1;
    
    // R Channel
    bit   s_RID_1;  // use default value: 0x0
    bit   [DATA_WIDTH-1:0] s_RDATA_1;
    bit   [1:0] s_RRESP_1;
    bit   s_RLAST_1;
    bit   s_RVALID_1;
    wire  s_RREADY_1;
    
    // Custom Interface (connect with other Cache L1)
    // Snoop Request Channel
    // send request to other Cache L1
    wire  m_ACVALID_1;
    wire   m_ACREADY_1;
    wire  [ADDR_WIDTH-1:0] m_ACADDR_1;
    wire  [1:0] m_ACSNOOP_1;
    // receive response from other Cache L1
    wire   m_CVALID_1;
    wire  m_CREADY_1;
    wire   [DATA_WIDTH-1:0] m_CDATA_1;
    wire   m_CLAST_1;
    wire   m_CHIT_1;
    
    // Snoop Response Channel
    // receive request from other Cache L1
    wire   s_ACVALID_1;
    wire  s_ACREADY_1;
    wire   [ADDR_WIDTH-1:0] s_ACADDR_1;
    wire   [1:0] s_ACSNOOP_1;
    // send response to other Cache L1
    wire  s_CVALID_1;
    wire   s_CREADY_1;
    wire  [DATA_WIDTH-1:0] s_CDATA_1;
    wire  s_CLAST_1;
    wire  s_CHIT_1;
    
    // to initial senario of the test
    bit [DATA_WIDTH-1 : 0] cpu_read_data [0:31];
    bit [DATA_WIDTH * 16-1:0] wb_data [0:31];
    bit [DATA_WIDTH * 16-1:0] cache2bus_data [0:31];
    bit [DATA_WIDTH * 16-1:0] mem2cache_data [0:31];
    bit [DATA_WIDTH * 16-1:0] bus2cache_data [0:31];
    bit [DATA_WIDTH-1:0] cpu2cache_data [0:31];
    bit [24:0] state_tag_0 [0:15];
    bit [24:0] state_tag_1 [0:15];
    bit [24:0] state_tag_2 [0:15];
    bit [24:0] state_tag_3 [0:15];
    
    // for debug
    wire [4:0] current_state;
    wire [2:0] next_moesi_state;
    
    assign current_state = DUT.core_0_cache.cache_controller.state;
    assign next_moesi_state = DUT.core_0_cache.next_state;
    
    // core 0;
    // Snoop Request Channel
    // send request to other Cache L1
    assign  m_ACVALID_0 = DUT.m_ACVALID;
    assign  m_ACREADY_0 = DUT.m_ACREADY;
    assign  m_ACADDR_0  = DUT.m_ACADDR;
    assign  m_ACSNOOP_0 = DUT.m_ACSNOOP;
    // receive response from other Cache L1
    assign  m_CVALID_0 = DUT.m_CVALID;
    assign  m_CREADY_0 = DUT.m_CREADY;
    assign  m_CDATA_0  = DUT.m_CDATA;
    assign  m_CLAST_0  = DUT.m_CLAST;
    assign  m_CHIT_0   = DUT.m_CHIT;
    
    // Snoop Response Channel
    // receive request from other Cache L1
    assign  s_ACVALID_0 = DUT.s_ACVALID;
    assign  s_ACREADY_0 = DUT.s_ACREADY;
    assign  s_ACADDR_0  = DUT.s_ACADDR;
    assign  s_ACSNOOP_0 = DUT.s_ACSNOOP;
    // send response to other Cache L1
    assign  s_CVALID_0 = DUT.s_CVALID;
    assign  s_CREADY_0 = DUT.s_CREADY;
    assign  s_CDATA_0  = DUT.s_CDATA;
    assign  s_CLAST_0  = DUT.s_CLAST;
    assign  s_CHIT_0   = DUT.s_CHIT;
    
    // core1;
    // Snoop Request Channel
    // send request to other Cache L1
    assign  m_ACVALID_1 = DUT.s_ACVALID;
    assign  m_ACREADY_1 = DUT.s_ACREADY;
    assign  m_ACADDR_1  = DUT.s_ACADDR; 
    assign  m_ACSNOOP_1 = DUT.s_ACSNOOP;
    // receive response from other Cache L1
    assign  m_CVALID_1 = DUT.s_CVALID;
    assign  m_CREADY_1 = DUT.s_CREADY;
    assign  m_CDATA_1  = DUT.s_CDATA; 
    assign  m_CLAST_1  = DUT.s_CLAST; 
    assign  m_CHIT_1   = DUT.s_CHIT;  
    
    // Snoop Response Channel
    // receive request from other Cache L1
    assign  s_ACVALID_1 = DUT.m_ACVALID;
    assign  s_ACREADY_1 = DUT.m_ACREADY;
    assign  s_ACADDR_1  = DUT.m_ACADDR; 
    assign  s_ACSNOOP_1 = DUT.m_ACSNOOP;
    // send response to other Cache L1
    assign  s_CVALID_1 = DUT.m_CVALID;
    assign  s_CREADY_1 = DUT.m_CREADY;
    assign  s_CDATA_1  = DUT.m_CDATA; 
    assign  s_CLAST_1  = DUT.m_CLAST; 
    assign  s_CHIT_1   = DUT.m_CHIT;  
    
    initial begin
        $readmemb(PATH_WAY0, DUT.core_0_cache.way0.state_tag_ram);
        $readmemb(PATH_WAY1, DUT.core_0_cache.way1.state_tag_ram);
        $readmemb(PATH_WAY2, DUT.core_0_cache.way2.state_tag_ram);
        $readmemb(PATH_WAY3, DUT.core_0_cache.way3.state_tag_ram);
        $readmemh(PATH_DATA, DUT.core_0_cache.cache_data_ram.cache);
        $readmemb(PATH_PLRUT, DUT.core_0_cache.plrut_ram.plrut_ram);
        $readmemh(PATH_BUS_SNOOP_DATA, bus2cache_data);
        $readmemh(PATH_MEM_FETCH_DATA, mem2cache_data);
        $readmemh(PATH_CPU_WRITE_DATA, cpu2cache_data);
        
        for(int i = 0; i < 32; i = i+1) begin
            cpu_read_data[i] = 0;
            wb_data[i] = 0;
            cache2bus_data[i] = 0;
        end
    end
    
    initial begin
        ACLK = 0;
        ARESETn = 0;
        ENABLE_0 = 0;
        ENABLE_1 = 0;
        repeat (10) @(posedge ACLK);
        ARESETn = 1;
        ENABLE_0 = 1;
        ENABLE_1 = 1;
        
        // write with addr = 32'hfedc_ba98 --> miss
        repeat (5) @(posedge ACLK);
        m_AWVALID_1 <= 1;
        m_AWADDR_1 <= 32'hfedc_ba98;
        do begin
            @(posedge ACLK);
        end while (!m_AWREADY_1);
        m_AWVALID_1 <= 0;
        m_WVALID_1 <= 1;
        m_WDATA_1 <= cpu2cache_data[0];
        m_WSTRB_1 <= 4'hF;
        do begin
            @(posedge ACLK);
        end while (!m_WREADY_1);
        m_WVALID_1 <= 0;
        
        // fetch from Cache L2
        s_ARREADY_1 <= 1;
        do begin
            @(posedge ACLK);
        end while (!s_ARVALID_1);
        s_RID_1 <= 0;
        s_RRESP_1 <= 0;
        s_RVALID_1 <= 1;
        for (int j = 0; j < 16; j++) begin
            s_RDATA_1 <= mem2cache_data[0] >> (j * 32);
            s_RLAST_1 <= j == 15;
            @(posedge ACLK);
        end
        s_RLAST_1 <= 0;
        s_RVALID_1 <= 0;
        m_BREADY_1 <= 1;
        
        // read with add = 32'hfedc_ba98 --> miss
        repeat (5) @(posedge ACLK);
        m_ARVALID_0 <= 1;
        m_ARADDR_0 <= 32'hfedc_ba98;
        do begin
            @(posedge ACLK);
        end while (!m_ARREADY_0);
        m_ARVALID_0 <= 0;
        m_RREADY_0 <= 1;
        
        // write with addr = 32'hfedc_ba98 --> hit
        repeat (5) @(posedge ACLK);
        m_AWVALID_0 <= 1;
        m_AWADDR_0 <= 32'hfedc_ba9c;
        do begin
            @(posedge ACLK);
        end while (!m_AWREADY_0);
        m_AWVALID_0 <= 0;
        m_WVALID_0 <= 1;
        m_WDATA_0 <= cpu2cache_data[1];
        m_WSTRB_0 <= 4'hF;
        do begin
            @(posedge ACLK);
        end while (!m_WREADY_0);
        m_WVALID_0 <= 0;

//        do begin
//            @(posedge ACLK);
//        end while (!m_RVALID_0);
        
//        // write with addr = 32'hfedc_ba98 --> hit
//        repeat (5) @(posedge ACLK);
//        m_AWVALID_1 <= 1;
//        m_AWADDR_1 <= 32'hfedc_ba9c;
//        do begin
//            @(posedge ACLK);
//        end while (!m_AWREADY_1);
//        m_AWVALID_1 <= 0;
//        m_WVALID_1 <= 1;
//        m_WDATA_1 <= cpu2cache_data[1];
//        m_WSTRB_1 <= 4'hF;
//        do begin
//            @(posedge ACLK);
//        end while (!m_WREADY_1);
//        m_WVALID_1 <= 0;
        
    
        $display("[%0t] ************************* End Simulation *************************", $time);
        repeat(100) @(posedge ACLK);
        $writememb(PATH_WAY0_result, DUT.core_0_cache.way0.state_tag_ram);
        $writememb(PATH_WAY1_result, DUT.core_0_cache.way1.state_tag_ram);
        $writememb(PATH_WAY2_result, DUT.core_0_cache.way2.state_tag_ram);
        $writememb(PATH_WAY3_result, DUT.core_0_cache.way3.state_tag_ram);
        $writememh(PATH_DATA_result, DUT.core_0_cache.cache_data_ram.cache);
        $writememb(PATH_PLRUT_result, DUT.core_0_cache.plrut_ram.plrut_ram);
        $writememh(PATH_CPU_READ_DATA, cpu_read_data);
        $writememh(PATH_WB_DATA, wb_data);
        $writememh(PATH_CACHE_SNOOP_DATA, cache2bus_data);
        $display("[%0t] ********************* Finish Writing Result *********************", $time);
        $finish;
    end
    
//    typedef struct packed {
//        bit [31:0] addr;
//        bit [31:0] data;
//        bit instr_type;
//    } instruction_s;
    
//    function void load_instr_mem(input string path, output instruction_s instr_mem [0:31]);
//        int file;
//        string line;
//        int index = 0;
//        string op;
//        bit [31:0] addr, data;
//        int num_tokens = 0;
        
//        file = $fopen(path, "r");
//        if (file == 0) begin
//            $display("Error: Unable to open file %s", path);
//            return;
//        end
        
//        while (!$feof(file) && index < 32) begin
//            line = "";
//            void'($fgets(line, file));
            
//            if (line == "") continue;
            
//            op = "";
//            addr = 0;
//            data = 0;
            
//            num_tokens = $sscanf(line, "%s %h %h", op, addr, data);
            
//            if (num_tokens >= 2) begin
//                instr_mem[index].addr = addr;
                
//                if (op == "read") begin
//                    instr_mem[index].instr_type = 1'b0; // Read instruction
//                    instr_mem[index].data = 32'b0; // No data for read operations
//                end else if (op == "write" && num_tokens == 3) begin
//                    instr_mem[index].instr_type = 1'b1; // Write instruction
//                    instr_mem[index].data = data;
//                end else begin
//                    $display("Error: Invalid instruction format at line %d", index + 1);
//                    continue;
//                end
                
//                index++;
//            end
//        end
        
//        $fclose(file);
//    endfunction
    
    initial begin
        forever
            #5 ACLK = ~ACLK;
    end

    dual_core_cache DUT
    (
        // system signals
        .ACLK(ACLK),
        .ARESETn(ARESETn),
        
        // core_0 cache
        .ENABLE_0(ENABLE_0),
        .CACHE_HIT_0(CACHE_HIT_0),
        .CACHE_BUSY_0(CACHE_BUSY_0),
        
        // AXI5-Lite Interface (connect with CPU)
        // AW Channel
        .m_AWVALID_0(m_AWVALID_0),
        .m_AWREADY_0(m_AWREADY_0),
        .m_AWADDR_0(m_AWADDR_0),
        
        // W Channel
        .m_WVALID_0(m_WVALID_0),
        .m_WREADY_0(m_WREADY_0),
        .m_WDATA_0(m_WDATA_0),
        .m_WSTRB_0(m_WSTRB_0), // use default value: 0xF
        
        // B Channel
        .m_BVALID_0(m_BVALID_0),
        .m_BREADY_0(m_BREADY_0),
        .m_BRESP_0(m_BRESP_0),
        
        // AR Channel
        .m_ARVALID_0(m_ARVALID_0),
        .m_ARREADY_0(m_ARREADY_0),
        .m_ARADDR_0(m_ARADDR_0),
        
        // R Channel
        .m_RVALID_0(m_RVALID_0),
        .m_RREADY_0(m_RREADY_0),
        .m_RDATA_0(m_RDATA_0),
        .m_RRESP_0(m_RRESP_0),
        
        // AXI5 Interface (connect with Cache L2)
        // AW Channel
        .s_AWID_0(s_AWID_0), // use default value: 0x0
        .s_AWADDR_0(s_AWADDR_0),
        .s_AWLEN_0(s_AWLEN_0),
        .s_AWSIZE_0(s_AWSIZE_0),  // use default value: Data bus width = 32-bit -> AWSIZE = 0x2
        .s_AWBURST_0(s_AWBURST_0), // use default value: 0x1_0(), INCR   
        .s_AWVALID_0(s_AWVALID_0),
        .s_AWREADY_0(s_AWREADY_0),
        
        // W Channel
        .s_WID_0(s_WID_0),  // use default value: 0x0
        .s_WDATA_0(s_WDATA_0),
        .s_WSTRB_0(s_WSTRB_0),  // use default value: 0xF
        .s_WLAST_0(s_WLAST_0),
        .s_WVALID_0(s_WVALID_0),
        .s_WREADY_0(s_WREADY_0),
        
        // B Channel
        .s_BID_0(s_BID_0),  // use default value: 0x0
        .s_BRESP_0(s_BRESP_0),  
        .s_BVALID_0(s_BVALID_0),
        .s_BREADY_0(s_BREADY_0),
        
        // AR Channel
        .s_ARID_0(s_ARID_0), // use default value: 0x0
        .s_ARADDR_0(s_ARADDR_0),
        .s_ARLEN_0(s_ARLEN_0),
        .s_ARSIZE_0(s_ARSIZE_0),  // use default value: Data bus width = 32-bit -> ARSIZE = 0x2
        .s_ARBURST_0(s_ARBURST_0), // use default value: 0x1_0(), INCR  
        .s_ARVALID_0(s_ARVALID_0),
        .s_ARREADY_0(s_ARREADY_0),
        
        // R Channel
        .s_RID_0(s_RID_0),  // use default value: 0x0
        .s_RDATA_0(s_RDATA_0),
        .s_RRESP_0(s_RRESP_0),
        .s_RLAST_0(s_RLAST_0),
        .s_RVALID_0(s_RVALID_0),
        .s_RREADY_0(s_RREADY_0),
        
        // core_1 cache
        .ENABLE_1(ENABLE_1),
        .CACHE_HIT_1(CACHE_HIT_1),
        .CACHE_BUSY_1(CACHE_BUSY_1),
        
        // AXI5-Lite Interface (connect with CPU)
        // AW Channel
        .m_AWVALID_1(m_AWVALID_1),
        .m_AWREADY_1(m_AWREADY_1),
        .m_AWADDR_1(m_AWADDR_1),
        
        // W Channel
        .m_WVALID_1(m_WVALID_1),
        .m_WREADY_1(m_WREADY_1),
        .m_WDATA_1(m_WDATA_1),
        .m_WSTRB_1(m_WSTRB_1), // use default value: 0xF
        
        // B Channel
        .m_BVALID_1(m_BVALID_1),
        .m_BREADY_1(m_BREADY_1),
        .m_BRESP_1(m_BRESP_1),
        
        // AR Channel
        .m_ARVALID_1(m_ARVALID_1),
        .m_ARREADY_1(m_ARREADY_1),
        .m_ARADDR_1(m_ARADDR_1),
        
        // R Channel
        .m_RVALID_1(m_RVALID_1),
        .m_RREADY_1(m_RREADY_1),
        .m_RDATA_1(m_RDATA_1),
        .m_RRESP_1(m_RRESP_1),
        
        // AXI5 Interface (connect with Cache L2)
        // AW Channel
        .s_AWID_1(s_AWID_1), // use default value: 0x0
        .s_AWADDR_1(s_AWADDR_1),
        .s_AWLEN_1(s_AWLEN_1),
        .s_AWSIZE_1(s_AWSIZE_1),  // use default value: Data bus width = 32-bit -> AWSIZE = 0x2
        .s_AWBURST_1(s_AWBURST_1), // use default value: 0x1_1(), INCR   
        .s_AWVALID_1(s_AWVALID_1),
        .s_AWREADY_1(s_AWREADY_1),
        
        // W Channel
        .s_WID_1(s_WID_1),  // use default value: 0x0
        .s_WDATA_1(s_WDATA_1),
        .s_WSTRB_1(s_WSTRB_1),  // use default value: 0xF
        .s_WLAST_1(s_WLAST_1),
        .s_WVALID_1(s_WVALID_1),
        .s_WREADY_1(s_WREADY_1),
        
        // B Channel
        .s_BID_1(s_BID_1),  // use default value: 0x0
        .s_BRESP_1(s_BRESP_1),  
        .s_BVALID_1(s_BVALID_1),
        .s_BREADY_1(s_BREADY_1),
        
        // AR Channel
        .s_ARID_1(s_ARID_1), // use default value: 0x0
        .s_ARADDR_1(s_ARADDR_1),
        .s_ARLEN_1(s_ARLEN_1),
        .s_ARSIZE_1(s_ARSIZE_1),  // use default value: Data bus width = 32-bit -> ARSIZE = 0x2
        .s_ARBURST_1(s_ARBURST_1), // use default value: 0x1_1(), INCR  
        .s_ARVALID_1(s_ARVALID_1),
        .s_ARREADY_1(s_ARREADY_1),
        
        // R Channel
        .s_RID_1(s_RID_1),  // use default value: 0x0
        .s_RDATA_1(s_RDATA_1),
        .s_RRESP_1(s_RRESP_1),
        .s_RLAST_1(s_RLAST_1),
        .s_RVALID_1(s_RVALID_1),
        .s_RREADY_1(s_RREADY_1)
    );
    
//    string name = "AN NGUYEN!";
//    int file;
//    string line;
//    int index = 0;
//    instruction_s instr_mem [0:31];
    
//    initial begin
//        $display(name);
//        load_instr_mem("D:/University/KLTN/hw_design/dual_core_cache/dual_core_cache.srcs/sources_1/new/instruction_mem_0.mem", instr_mem);
//        foreach(instr_mem[i])
//            $display("%p", instr_mem[i]);
//    end

    typedef struct {
        bit [31:0] addr;
        bit [31:0] data [0:15];
    } cache_L2_s;
    cache_L2_s cache_L2_read [0:31];
    
    function void load_cache_L2(input string path, output cache_L2_s cache_L2_read [0:31]);
        int file;
        int index = 0;
        bit [7:0] line[256]; // Fixed-size array for line storage
        bit [31:0] addr;
        bit [31:0] data [0:15];
        int num_tokens = 0;
    
        file = $fopen(path, "r");
        if (file == 0) begin
            $display("Error: Unable to open file %s", path);
            return;
        end
    
        index = 0;
        while (!$feof(file) && index < 32) begin
            void'($fgets(line, file)); // Read a line from the file
    
            // Read address and multiple data values
            num_tokens = $sscanf(line, "%h %h %h %h %h %h %h %h %h %h %h %h %h %h %h %h %h", 
                                 addr,
                                 data[15], data[14], data[13], data[12],
                                 data[11], data[10], data[9], data[8],
                                 data[7], data[6], data[5], data[4],
                                 data[3], data[2], data[1], data[0]);
    
            if (num_tokens >= 2) begin
                cache_L2_read[index].addr = addr;
                cache_L2_read[index].data = data;
                index++;
            end
        end
    
        $fclose(file);
    endfunction
    
    function void save_cache_L2(input string path, input cache_L2_s cache_L2_read [0:31]);
        int file = 0;
        int index = 0;
        
        file = $fopen(path, "w");
        if (file == 0) begin
            $display("Error: Unable to open file %s for writing", path);
            return;
        end
        for (index = 0; index < 32; index++) begin
            // Write address followed by 16 data values in a single line
            $fwrite(file, "0x%h", cache_L2_read[index].addr);
            for (int i = 15; i >= 0; i--) begin
                $fwrite(file, " 0x%h", cache_L2_read[index].data[i]);
            end
            $fwrite(file, "\n"); // New line after each entry
        end
        $fclose(file);
    endfunction
    
    initial begin
        load_cache_L2("D:/University/KLTN/hw_design/dual_core_cache/dual_core_cache.srcs/sources_1/new/cache_L2_read.mem", cache_L2_read);
        
        foreach(cache_L2_read[i]) 
            $display("%p", cache_L2_read[i]);
            
        save_cache_L2("D:/University/KLTN/hw_design/dual_core_cache/dual_core_cache.srcs/sources_1/new/cache_L2_write.mem", cache_L2_read);
    end
    
endmodule
