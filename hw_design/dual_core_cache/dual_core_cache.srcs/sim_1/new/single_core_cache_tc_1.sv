`timescale 1ns / 1ps
//////////////////////////////////////////////////////////////////////////////////
// 
//////////////////////////////////////////////////////////////////////////////////


module single_core_cache_tc_1 ();
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
    bit   ENABLE;
    wire  CACHE_HIT;
    wire  CACHE_BUSY;
    
    // AXI5-Lite Interface (connect with CPU)
    // AW Channel
    bit   m_AWVALID;
    wire  m_AWREADY;
    bit   [ADDR_WIDTH-1:0] m_AWADDR;
    
    // W Channel
    bit   m_WVALID;
    wire  m_WREADY;
    bit   [DATA_WIDTH-1:0] m_WDATA;
    bit   [3:0] m_WSTRB; // use default value: 0xF
    
    // B Channel
    wire  m_BVALID;
    bit   m_BREADY;
    wire  [1:0] m_BRESP;
    
    // AR Channel
    bit   m_ARVALID;
    wire  m_ARREADY;
    bit   [ADDR_WIDTH-1:0] m_ARADDR;
    
    // R Channel
    wire  m_RVALID;
    bit   m_RREADY;
    wire  [DATA_WIDTH-1:0] m_RDATA;
    wire  [1:0] m_RRESP;
    
    // AXI5 Interface (connect with Cache L2)
    // AW Channel
    wire  s_AWID; // use default value: 0x0
    wire  [ADDR_WIDTH-1:0] s_AWADDR;
    wire  [3:0] s_AWLEN;
    wire  [2:0] s_AWSIZE;  // use default value: Data bus width = 32-bit -> AWSIZE = 0x2
    wire  [1:0] s_AWBURST; // use default value: 0x1; INCR   
    wire  s_AWVALID;
    bit   s_AWREADY;
    
    // W Channel
    wire  s_WID;  // use default value: 0x0
    wire  [DATA_WIDTH-1:0] s_WDATA;
    wire  [3:0] s_WSTRB;  // use default value: 0xF
    wire  s_WLAST;
    wire  s_WVALID;
    bit   s_WREADY;
    
    // B Channel
    bit   s_BID;  // use default value: 0x0
    bit   [1:0] s_BRESP;  
    bit   s_BVALID;
    wire  s_BREADY;
    
    // AR Channel
    wire  s_ARID; // use default value: 0x0
    wire  [ADDR_WIDTH-1:0] s_ARADDR;
    wire  [3:0] s_ARLEN;
    wire  [2:0] s_ARSIZE;  // use default value: Data bus width = 32-bit -> ARSIZE = 0x2
    wire  [1:0] s_ARBURST; // use default value: 0x1; INCR  
    wire  s_ARVALID;
    bit   s_ARREADY;
    
    // R Channel
    bit   s_RID;  // use default value: 0x0
    bit   [DATA_WIDTH-1:0] s_RDATA;
    bit   [1:0] s_RRESP;
    bit   s_RLAST;
    bit   s_RVALID;
    wire  s_RREADY;
    
    // Custom Interface (connect with other Cache L1)
    // Snoop Request Channel
    // send request to other Cache L1
    wire  m_ACVALID;
    bit   m_ACREADY;
    wire  [ADDR_WIDTH-1:0] m_ACADDR;
    wire  [1:0] m_ACSNOOP;
    // receive response from other Cache L1
    bit   m_CVALID;
    wire  m_CREADY;
    bit   [DATA_WIDTH-1:0] m_CDATA;
    bit   m_CLAST;
    bit   m_CHIT;
    
    // Snoop Response Channel
    // receive request from other Cache L1
    bit   s_ACVALID;
    wire  s_ACREADY;
    bit   [ADDR_WIDTH-1:0] s_ACADDR;
    bit   [1:0] s_ACSNOOP;
    // send response to other Cache L1
    wire  s_CVALID;
    bit   s_CREADY;
    wire  [DATA_WIDTH-1:0] s_CDATA;
    wire  s_CLAST;
    wire  s_CHIT;
    
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
    
    assign current_state = DUT.cache_controller.state;
    assign next_moesi_state = DUT.next_state;
    
    integer i;
    initial begin
        $readmemb(PATH_WAY0, DUT.way0.state_tag_ram);
        $readmemb(PATH_WAY1, DUT.way1.state_tag_ram);
        $readmemb(PATH_WAY2, DUT.way2.state_tag_ram);
        $readmemb(PATH_WAY3, DUT.way3.state_tag_ram);
        $readmemh(PATH_DATA, DUT.cache_data_ram.cache);
        $readmemb(PATH_PLRUT, DUT.plrut_ram.plrut_ram);
        $readmemh(PATH_BUS_SNOOP_DATA, bus2cache_data);
        $readmemh(PATH_MEM_FETCH_DATA, mem2cache_data);
        $readmemh(PATH_CPU_WRITE_DATA, cpu2cache_data);
        
        for(i = 0; i < 32; i = i+1) begin
            cpu_read_data[i] = 0;
            wb_data[i] = 0;
            cache2bus_data[i] = 0;
        end
    end
    
    integer j;
    initial begin
        ACLK = 0;
        ARESETn = 0;
        ENABLE = 0;
        repeat (10) @(posedge ACLK);
        ARESETn = 1;
        ENABLE = 1;
        
        // write with addr = 32'hfedc_ba98 --> miss
        repeat (5) @(posedge ACLK);
        m_AWVALID <= 1;
        m_AWADDR <= 32'hfedc_ba98;
        do begin
            @(posedge ACLK);
        end while (!m_AWREADY);
        m_AWVALID <= 0;
        m_WVALID <= 1;
        m_WDATA <= cpu2cache_data[0];
        m_WSTRB <= 4'hF;
        do begin
            @(posedge ACLK);
        end while (!m_WREADY);
        m_WVALID <= 0;
        m_ACREADY <= 1;
        repeat (5) @(posedge ACLK);
        m_CVALID <= 1;
        m_CDATA <= 32'hEEEE_EEEE;
        m_CLAST <= 1;
        m_CHIT <= 0;
        @(posedge ACLK);
        m_CVALID <= 0;
        
        // fetch from Cache L2
        s_ARREADY <= 1;
        repeat (5) @(posedge ACLK);
        s_RID <= 0;
        s_RRESP <= 0;
        s_RVALID <= 1;
        for (j = 0; j < 16; j++) begin
            s_RDATA <= mem2cache_data[0] >> (j * 32);
            s_RLAST <= j == 15;
            @(posedge ACLK);
        end
        s_RLAST <= 0;
        s_RVALID <= 0;
        m_BREADY <= 1;
        
        // write with addr = 32'hfedc_ba94 --> hit
        repeat (1) @(posedge ACLK);
        m_AWVALID <= 1;
        m_AWADDR <= 32'hfedc_ba94;
        do begin
            @(posedge ACLK);
        end while (!m_AWREADY);
        m_AWVALID <= 0;
        m_WVALID <= 1;
        m_WDATA <= cpu2cache_data[1];
        m_WSTRB <= 4'hF;
        do begin
            @(posedge ACLK);
        end while (!m_WREADY);
        m_WVALID <= 0;
        m_BREADY <= 1;
        m_ACREADY <= 1;
        @(posedge ACLK);
        m_CVALID <= 1;
        m_CDATA <= 32'hEEEE_EEEE;
        m_CLAST <= 1;
        m_CHIT <= 1;
        @(posedge ACLK);
        m_CVALID <= 0;
        
        // read with add = 32'hfedc_ba98 --> hit
        repeat (5) @(posedge ACLK);
        m_ARVALID <= 1;
        m_ARADDR <= 32'hfedc_ba98;
        do begin
            @(posedge ACLK);
        end while (!m_ARREADY);
        m_ARVALID <= 0;
        m_RREADY <= 1;
        
        // read with add = 32'habcd_5678 --> miss
        repeat (5) @(posedge ACLK);
        m_ARVALID <= 1;
        m_ARADDR <= 32'habcd_5678;
        do begin
            @(posedge ACLK);
        end while (!m_ARREADY);
        m_ARVALID <= 0;
        m_RREADY <= 1;
        m_ACREADY <= 1;
        @(posedge ACLK);
        m_CVALID <= 1;
        m_CDATA <= 32'hEEEE_EEEE;
        m_CLAST <= 1;
        m_CHIT <= 0;
        @(posedge ACLK);
        m_CVALID <= 0;
        
        // fetch from Cache L2
        s_ARREADY <= 1;
        repeat (5) @(posedge ACLK);
        s_RID <= 0;
        s_RRESP <= 0;
        s_RVALID <= 1;
        for (j = 0; j < 16; j++) begin
            s_RDATA <= mem2cache_data[1] >> (j * 32);
            s_RLAST <= j == 15;
            @(posedge ACLK);
        end
        s_RLAST <= 0;
        s_RVALID <= 0;
        
        // read with add = 32'h1234_a984 --> miss
        repeat (5) @(posedge ACLK);
        m_ARVALID <= 1;
        m_ARADDR <= 32'h1234_a984;
        do begin
            @(posedge ACLK);
        end while (!m_ARREADY);
        m_ARVALID <= 0;
        m_RREADY <= 1;
        
        // fetch from Other Cache L1
        m_ACREADY <= 1;
        @(posedge ACLK);
        m_CVALID <= 1;
        m_CHIT <= 1;
        for (j = 0; j < 16; j++) begin
            m_CDATA <= bus2cache_data[0] >> (j * 32);
            m_CLAST <= j == 15;
            // m_CHIT <= j == 10 ? 0 : 1;
            @(posedge ACLK);
        end
        m_CLAST <= 0;
        m_CVALID <= 0;
        
        // write with addr = 32'h1357_2468 --> miss
        repeat (5) @(posedge ACLK);
        m_AWVALID <= 1;
        m_AWADDR <= 32'h1357_2468;
        do begin
            @(posedge ACLK);
        end while (!m_AWREADY);
        m_AWVALID <= 0;
        m_WVALID <= 1;
        m_WDATA <= cpu2cache_data[2];
        m_WSTRB <= 4'hF;
        do begin
            @(posedge ACLK);
        end while (!m_WREADY);
        m_WVALID <= 0;
        
        // fetch from Other Cache L1
        m_ACREADY <= 1;
        @(posedge ACLK);
        m_CVALID <= 1;
        m_CHIT <= 1;
        for (j = 0; j < 16; j++) begin
            m_CDATA <= bus2cache_data[1] >> (j * 32);
            m_CLAST <= j == 15;
            //m_CHIT <= j == 15 ? 0 : 1;
            @(posedge ACLK);
        end
        m_CLAST <= 0;
        m_CVALID <= 0;
        
        // write with addr = 32'habcd_5678 --> hit
//        repeat (5) @(posedge ACLK);
//        m_AWVALID <= 1;
//        m_AWADDR <= 32'habcd_5678;
//        do begin
//            @(posedge ACLK);
//        end while (!m_AWREADY);
//        m_AWVALID <= 0;
//        m_WVALID <= 1;
//        m_WDATA <= cpu2cache_data[3];
//        m_WSTRB <= 4'hF;
//        do begin
//            @(posedge ACLK);
//        end while (!m_WREADY);
//        m_WVALID <= 0;

          m_WVALID <= to_int(1);
          @(posedge ACLK);
        
        $display("[%0t] ************************* End Simulation *************************", $time);
        repeat(100) @(posedge ACLK);
        $writememb(PATH_WAY0_result, DUT.way0.state_tag_ram);
        $writememb(PATH_WAY1_result, DUT.way1.state_tag_ram);
        $writememb(PATH_WAY2_result, DUT.way2.state_tag_ram);
        $writememb(PATH_WAY3_result, DUT.way3.state_tag_ram);
        $writememh(PATH_DATA_result, DUT.cache_data_ram.cache);
        $writememb(PATH_PLRUT_result, DUT.plrut_ram.plrut_ram);
        $writememh(PATH_CPU_READ_DATA, cpu_read_data);
        $writememh(PATH_WB_DATA, wb_data);
        $writememh(PATH_CACHE_SNOOP_DATA, cache2bus_data);
        $display("[%0t] ********************* Finish Writing Result *********************", $time);
        $finish;
    end
    
    
    initial begin
        forever
            #5 ACLK = ~ACLK;
    end
    
    single_core_cache DUT
    (
        // system signals
        .ACLK(ACLK),
        .ARESETn(ARESETn),
        .ENABLE(ENABLE),
        .CACHE_HIT(CACHE_HIT),
        .CACHE_BUSY(CACHE_BUSY),
        
        // AXI5-Lite Interface (connect with CPU)
        // AW Channel
        .m_AWVALID(m_AWVALID),
        .m_AWREADY(m_AWREADY),
        .m_AWADDR(m_AWADDR),
        
        // W Channel
        .m_WVALID(m_WVALID),
        .m_WREADY(m_WREADY),
        .m_WDATA(m_WDATA),
        .m_WSTRB(m_WSTRB), // use default value: 0xF
        
        // B Channel
        .m_BVALID(m_BVALID),
        .m_BREADY(m_BREADY),
        .m_BRESP(m_BRESP),
        
        // AR Channel
        .m_ARVALID(m_ARVALID),
        .m_ARREADY(m_ARREADY),
        .m_ARADDR(m_ARADDR),
        
        // R Channel
        .m_RVALID(m_RVALID),
        .m_RREADY(m_RREADY),
        .m_RDATA(m_RDATA),
        .m_RRESP(m_RRESP),
        
        // AXI5 Interface (connect with Cache L2)
        // AW Channel
        .s_AWID(s_AWID), // use default value: 0x0
        .s_AWADDR(s_AWADDR),
        .s_AWLEN(s_AWLEN),
        .s_AWSIZE(s_AWSIZE),  // use default value: Data bus width = 32-bit -> AWSIZE = 0x2
        .s_AWBURST(s_AWBURST), // use default value: 0x1(), INCR   
        .s_AWVALID(s_AWVALID),
        .s_AWREADY(s_AWREADY),
        
        // W Channel
        .s_WID(s_WID),  // use default value: 0x0
        .s_WDATA(s_WDATA),
        .s_WSTRB(s_WSTRB),  // use default value: 0xF
        .s_WLAST(s_WLAST),
        .s_WVALID(s_WVALID),
        .s_WREADY(s_WREADY),
        
        // B Channel
        .s_BID(s_BID),  // use default value: 0x0
        .s_BRESP(s_BRESP),  
        .s_BVALID(s_BVALID),
        .s_BREADY(s_BREADY),
        
        // AR Channel
        .s_ARID(s_ARID), // use default value: 0x0
        .s_ARADDR(s_ARADDR),
        .s_ARLEN(s_ARLEN),
        .s_ARSIZE(s_ARSIZE),  // use default value: Data bus width = 32-bit -> ARSIZE = 0x2
        .s_ARBURST(s_ARBURST), // use default value: 0x1(), INCR  
        .s_ARVALID(s_ARVALID),
        .s_ARREADY(s_ARREADY),
        
        // R Channel
        .s_RID(s_RID),  // use default value: 0x0
        .s_RDATA(s_RDATA),
        .s_RRESP(s_RRESP),
        .s_RLAST(s_RLAST),
        .s_RVALID(s_RVALID),
        .s_RREADY(s_RREADY),
        
        // Custom Interface (connect with other Cache L1)
        // Snoop Request Channel
        // send request to other Cache L1
        .m_ACVALID(m_ACVALID),
        .m_ACREADY(m_ACREADY),
        .m_ACADDR(m_ACADDR),
        .m_ACSNOOP(m_ACSNOOP),
        // receive response from other Cache L1
        .m_CVALID(m_CVALID),
        .m_CREADY(m_CREADY),
        .m_CDATA(m_CDATA),
        .m_CLAST(m_CLAST),
        .m_CHIT(m_CHIT),
        
        // Snoop Response Channel
        // receive request from other Cache L1
        .s_ACVALID(s_ACVALID),
        .s_ACREADY(s_ACREADY),
        .s_ACADDR(s_ACADDR),
        .s_ACSNOOP(s_ACSNOOP),
        // send response to other Cache L1
        .s_CVALID(s_CVALID),
        .s_CREADY(s_CREADY),
        .s_CDATA(s_CDATA),
        .s_CLAST(s_CLAST),
        .s_CHIT(s_CHIT)
    );
    

endmodule
