//////////////////////////////////////////////////////////////////////////////////
// this is top module of one-core cache
//////////////////////////////////////////////////////////////////////////////////

module single_core_cache
#(
    parameter DATA_WIDTH = 32,
    parameter ADDR_WIDTH = 32
)
(
    // system signals
    input   ACLK,
    input   ARESETn,
    input   ENABLE,
    output  CACHE_HIT,
    output  CACHE_BUSY,
    
    // AXI5-Lite Interface (connect with CPU)
    // AW Channel
    input   m_AWVALID,
    output  m_AWREADY,
    input   [ADDR_WIDTH-1:0] m_AWADDR,
    
    // W Channel
    input   m_WVALID,
    output  m_WREADY,
    input   [DATA_WIDTH-1:0] m_WDATA,
    input   [3:0] m_WSTRB, // use default value: 0xF
    
    // B Channel
    output  m_BVALID,
    input   m_BREADY,
    output  [1:0] m_BRESP,
    
    // AR Channel
    input   m_ARVALID,
    output  m_ARREADY,
    input   [ADDR_WIDTH-1:0] m_ARADDR,
    
    // R Channel
    output  m_RVALID,
    input   m_RREADY,
    output  [DATA_WIDTH-1:0] m_RDATA,
    output  [1:0] m_RRESP,
    
    // AXI5 Interface (connect with Cache L2)
    // AW Channel
    output  s_AWID, // use default value: 0x0
    output  [ADDR_WIDTH-1:0] s_AWADDR,
    output  [3:0] s_AWLEN,
    output  [2:0] s_AWSIZE,  // use default value: Data bus width = 32-bit -> AWSIZE = 0x2
    output  [1:0] s_AWBURST, // use default value: 0x1, INCR   
    output  s_AWVALID,
    input   s_AWREADY,
    
    // W Channel
    output  s_WID,  // use default value: 0x0
    output  [DATA_WIDTH-1:0] s_WDATA,
    output  [3:0] s_WSTRB,  // use default value: 0xF
    output  s_WLAST,
    output  s_WVALID,
    input   s_WREADY,
    
    // B Channel
    input   s_BID,  // use default value: 0x0
    input   [1:0] s_BRESP,  
    input   s_BVALID,
    output  s_BREADY,
    
    // AR Channel
    output  s_ARID, // use default value: 0x0
    output  [ADDR_WIDTH-1:0] s_ARADDR,
    output  [3:0] s_ARLEN,
    output  [2:0] s_ARSIZE,  // use default value: Data bus width = 32-bit -> ARSIZE = 0x2
    output  [1:0] s_ARBURST, // use default value: 0x1, INCR  
    output  s_ARVALID,
    input   s_ARREADY,
    
    // R Channel
    input   s_RID,  // use default value: 0x0
    input   [DATA_WIDTH-1:0] s_RDATA,
    input   [1:0] s_RRESP,
    input   s_RLAST,
    input   s_RVALID,
    output  s_RREADY,
    
    // Custom Interface (connect with other Cache L1)
    // Snoop Request Channel
    // send request to other Cache L1
    output  m_ACVALID,
    input   m_ACREADY,
    output  [ADDR_WIDTH-1:0] m_ACADDR,
    output  [1:0] m_ACSNOOP,
    // receive response from other Cache L1
    input   m_CVALID,
    output  m_CREADY,
    input   [DATA_WIDTH-1:0] m_CDATA,
    input   m_CLAST,
    input   m_CHIT,
    
    // Snoop Response Channel
    // receive request from other Cache L1
    input   s_ACVALID,
    output  s_ACREADY,
    input   [ADDR_WIDTH-1:0] s_ACADDR,
    input   [1:0] s_ACSNOOP,
    // send response to other Cache L1
    output  s_CVALID,
    input   s_CREADY,
    output  [DATA_WIDTH-1:0] s_CDATA,
    output  s_CLAST,
    output  s_CHIT,
    
    // for demo to fix E-E bug
    // input is_E_E
    input is_R_R
    ///////////////////////////////////
);

    // internal register to store captured signals
    // signals CPU --> Cache L1
    reg [ADDR_WIDTH-1:0] m_AWADDR_reg;
    reg [DATA_WIDTH-1:0] m_WDATA_reg;
    reg [ADDR_WIDTH-1:0] m_ARADDR_reg;
    reg instr_type;
    
    // signals Cache L1 --> Cache L2
    reg [ADDR_WIDTH-1:0] s_AWADDR_reg;
    reg [ADDR_WIDTH-1:0] s_ARADDR_reg;
    
    // signals Cache L1 --> Other Cache L1
    reg [ADDR_WIDTH-1:0] m_ACADDR_reg;
    
    // signals Other Cache L1 --> Cache L1
    reg [ADDR_WIDTH-1:0] s_ACADDR_reg;
    reg [1:0] s_ACSNOOP_reg;
    
    // internal wires
    // for cache_controller
    wire data_w_en;
    wire plrut_w_en;
    
    // wire mem_wb;
    wire mem_bus_fetch;
    wire is_mem_fetch;
    wire is_bus_fetch;
    wire [1:0] w_data_sel;
    
    wire state_tag_w_en;
    wire cpu_m_aw_in_reg_en;
    wire cpu_m_w_in_reg_en;
    wire cpu_m_ar_in_reg_en;
    wire mem_s_aw_out_reg_en;
    wire mem_s_ar_out_reg_en;
    wire bus_m_ac_out_reg_en;
    
    // for snoop_controller
    wire state_tag_w_en_s;
    wire bus_in_reg_en;

    // for state_tag_ram
    wire w_en_w0, w_en_w1, w_en_w2, w_en_w3;
    wire [2:0]  r_state_w0, r_state_w1, r_state_w2, r_state_w3;
    wire [21:0] r_tag_w0, r_tag_w1, r_tag_w2, r_tag_w3;
    wire w_en_w0_s, w_en_w1_s, w_en_w2_s, w_en_w3_s;
    wire [2:0]  r_state_w0_s, r_state_w1_s, r_state_w2_s, r_state_w3_s;
    wire [21:0] r_tag_w0_s, r_tag_w1_s, r_tag_w2_s, r_tag_w3_s;
    
    // for checker_port1
    wire [21:0] tag;
    wire [3:0]  set;
    wire [1:0] hit_way;
    wire hit;
    wire full;
    wire [3:0] valid;
    wire [2:0] hit_way_state;

    // for checker_port2
    wire [21:0] tag_s;
    wire [3:0]  set_s;
    wire hit_s;
    wire [1:0] hit_way_s;
    wire [2:0] hit_way_state_s;
    
    // for PLRUt_controller
    wire [1:0] access_way;
    wire [2:0] r_PLRUt;
    wire [2:0] w_PLRUt;
    
    // for MOESI controller
    wire dirty;
    wire is_exclusive;
    wire [2:0] next_state;
    wire [2:0] next_state_s;
    
    // data_mem
    wire [DATA_WIDTH-1:0] w_data;
    wire [9:0] w_addr;
    wire [3:0] word_offset, w_word_offset, control_offset, control_offset_s;
    wire [9:0] r_addr;
    wire [9:0] r_addr_s;
    wire [DATA_WIDTH-1:0] r_data;
    wire [DATA_WIDTH-1:0] r_data_s;
    wire [21:0] wb_tag;
    wire [ADDR_WIDTH-1:0] wb_addr;
    
    assign {tag, set} = instr_type ? m_AWADDR_reg[31:6] : m_ARADDR_reg[31:6];
    assign {tag_s, set_s} = s_ACADDR_reg[31:6];
    
    assign word_offset = instr_type ? m_AWADDR_reg[5:2] : m_ARADDR_reg[5:2];
    assign w_word_offset = mem_bus_fetch ? control_offset : word_offset;
    
    assign w_data = (w_data_sel == 0) ? m_WDATA_reg : (w_data_sel == 1) ? m_CDATA : (w_data_sel == 2) ? s_RDATA : m_WDATA_reg;
    assign w_addr = {set, access_way, w_word_offset};
    assign r_addr = {set, access_way, w_word_offset};
    assign r_addr_s = {set_s, hit_way_s, control_offset_s};
    
    assign m_RDATA = r_data;
    assign s_WDATA = r_data;
    assign s_CDATA = r_data_s;
    
    assign wb_tag = (access_way == 2'b00) ? r_tag_w0 : (access_way == 2'b01) ? r_tag_w1 : (access_way == 2'b10) ? r_tag_w2 : (access_way == 2'b11) ? r_tag_w3 : r_tag_w0;
    assign wb_addr = {wb_tag, set, 6'b000000};
    
    // assign output
    assign s_ARADDR = s_ARADDR_reg;
    assign m_ACADDR = m_ACADDR_reg;
    assign s_AWADDR = s_AWADDR_reg;
    
    always @(posedge ACLK) begin
        if (!ARESETn) begin
            // registers CPU --> Cache L1
            m_AWADDR_reg <= 0;
            m_WDATA_reg <= 0;
            m_ARADDR_reg <= 0;
            instr_type <= 0;
            // registers Cache L1 --> Cache L2
            s_AWADDR_reg <= 0;
            s_ARADDR_reg <= 0;
            // register Cache L1 --> Other Cache L1
            m_ACADDR_reg <= 0;
            // registers Other Cache L1 --> Cache L1
            s_ACADDR_reg <= 0;
            s_ACSNOOP_reg <= 0;
        end
        else begin
            // registers CPU <--> Cache L1
            if (cpu_m_aw_in_reg_en) begin 
                m_AWADDR_reg <= m_AWADDR;
                instr_type <= 1;
            end
            if (cpu_m_w_in_reg_en)
                m_WDATA_reg <= m_WDATA;
            if (cpu_m_ar_in_reg_en) begin
                m_ARADDR_reg <= m_ARADDR; 
                instr_type <= 0;
            end  
            
            // registers Cache L1 --> Cache L2
            if (mem_s_aw_out_reg_en) begin
                s_AWADDR_reg <= wb_addr;
            end
            
            if (mem_s_ar_out_reg_en) begin
                s_ARADDR_reg <= instr_type ? {m_AWADDR_reg[31:6], 6'b000000} : {m_ARADDR_reg[31:6], 6'b000000};
            end
            
            // register Cache L1 --> Other Cache L1
            if (bus_m_ac_out_reg_en) begin
                m_ACADDR_reg <= instr_type ? {m_AWADDR_reg[31:6], 6'b000000} : {m_ARADDR_reg[31:6], 6'b000000};
            end
            
            // registers Other Cache L1 --> Cache L1
            if (bus_in_reg_en) begin
                s_ACADDR_reg <= s_ACADDR;
                s_ACSNOOP_reg <= s_ACSNOOP;
            end         
        end
    end

    // instance sub-modules
    // instance 4-Way: way0, way1, way2, way3
    state_tag_ram   way0
    (
        .clk(ACLK), .rst_n(ARESETn),       // input 
        .w_en1(w_en_w0),               // input
        .w_en2(w_en_w0_s),               // input
        .w_state_tag1({next_state, tag}),        // input
        .w_state_tag2({next_state_s, tag_s}),        // input
        .rw_addr1(set),            // input
        .rw_addr2(set_s),            // input
        .r_state_tag1({r_state_w0, r_tag_w0}),        // output
        .r_state_tag2({r_state_w0_s, r_tag_w0_s})         // output
    );
    
    state_tag_ram   way1
    (
        .clk(ACLK), .rst_n(ARESETn),       // input 
        .w_en1(w_en_w1),               // input
        .w_en2(w_en_w1_s),               // input
        .w_state_tag1({next_state, tag}),        // input
        .w_state_tag2({next_state_s, tag_s}),        // input
        .rw_addr1(set),            // input
        .rw_addr2(set_s),            // input
        .r_state_tag1({r_state_w1, r_tag_w1}),        // output
        .r_state_tag2({r_state_w1_s, r_tag_w1_s})         // output
    );
    
    state_tag_ram   way2
    (
        .clk(ACLK), .rst_n(ARESETn),       // input 
        .w_en1(w_en_w2),               // input
        .w_en2(w_en_w2_s),               // input
        .w_state_tag1({next_state, tag}),        // input
        .w_state_tag2({next_state_s, tag_s}),        // input
        .rw_addr1(set),            // input
        .rw_addr2(set_s),            // input
        .r_state_tag1({r_state_w2, r_tag_w2}),        // output
        .r_state_tag2({r_state_w2_s, r_tag_w2_s})         // output
    );
    
    state_tag_ram   way3
    (
        .clk(ACLK), .rst_n(ARESETn),       // input 
        .w_en1(w_en_w3),               // input
        .w_en2(w_en_w3_s),               // input
        .w_state_tag1({next_state, tag}),        // input
        .w_state_tag2({next_state_s, tag_s}),        // input
        .rw_addr1(set),            // input
        .rw_addr2(set_s),            // input
        .r_state_tag1({r_state_w3, r_tag_w3}),        // output
        .r_state_tag2({r_state_w3_s, r_tag_w3_s})         // output
    );
    
    // to check whether hit/miss when request coming from CPU
    checker_port1   checker_cpu_port
    (
        .tag_compare(tag),         // input
                                // input
        .tag_w0(r_tag_w0),              // input
        .tag_w1(r_tag_w1),              // input
        .tag_w2(r_tag_w2),              // input
        .tag_w3(r_tag_w3),              // input
                                // input
        .state_w0(r_state_w0),            // input
        .state_w1(r_state_w1),            // input
        .state_w2(r_state_w2),            // input
        .state_w3(r_state_w3),            // input
        
        .state_tag_w_en(state_tag_w_en),      // input
        .way(access_way),                 // input
        
        // write enable in state_tag_ram
        .w_en_w0(w_en_w0),             // output
        .w_en_w1(w_en_w1),             // output
        .w_en_w2(w_en_w2),             // output
        .w_en_w3(w_en_w3),             // output
                                
        .hit(hit),                 // output
        .hit_way(hit_way),             // output
        .full(full),                // output
        .valid(valid),               // output
        .hit_way_state(hit_way_state)        // output
    );
    
    // to check whether hit/mis when request coming from other Cache L1
    checker_port2   checker_other_cache_port
    (
        .tag_compare(tag_s),         // input
                                
        .tag_w0(r_tag_w0_s),              // input
        .tag_w1(r_tag_w1_s),              // input
        .tag_w2(r_tag_w2_s),              // input
        .tag_w3(r_tag_w3_s),              // input
                                
        .state_w0(r_state_w0_s),            // input
        .state_w1(r_state_w1_s),            // input
        .state_w2(r_state_w2_s),            // input
        .state_w3(r_state_w3_s),            // input
        
        .state_tag_w_en(state_tag_w_en_s),      // input
        
        .w_en_w0(w_en_w0_s),             // output
        .w_en_w1(w_en_w1_s),             // output
        .w_en_w2(w_en_w2_s),             // output
        .w_en_w3(w_en_w3_s),             // output
        
        .hit(hit_s),                 // output
        .hit_way(hit_way_s),             // output
        .hit_way_state(hit_way_state_s)        // output
    );
    
    // to store data in cache
    data_ram    cache_data_ram
    (
        .clk(ACLK), .rst_n(ARESETn),       // input
        .w_en(data_w_en),                // input
        .w_data(w_data),              // input
        .w_addr(w_addr),              // input    // address = {set, way, word offset}
        .r_addr1(r_addr),             // input
        .r_addr2(r_addr_s),             // input
        .r_data1(r_data),             // output
        .r_data2(r_data_s)              // output
    );
    
    // to store 3-bit PLRUt for 4-Way Set Associative Cache
    plrut_ram   plrut_ram
    (
        .clk(ACLK), .rst_n(ARESETn),       // input    
        .w_en(plrut_w_en),                // input    
        .w_plrut(w_PLRUt),             // input
        .w_addr(set),              // input    // using addr[9:6] to access
        .r_addr(set),              // input
        .r_plrut(r_PLRUt)              // output
    );
    
    // to deter which is the selected way to access, evict, ...
    plrut_controller    plrut_controller
    (
        .hit(hit),                 // input
        .full(full),                // input
        .valid(valid),               // input
        .hit_way(hit_way),             // input
        .current_PLRUt(r_PLRUt),       // input
        
        .next_PLRUt(w_PLRUt),          // output
        .access_way(access_way)           // output
    );
    
    // to determine the next state of MOESI protocol... for both CPU and other Cache L1 access
    moesi_controller    moesi_controller
    (
        .hit_way_state1(hit_way_state),      // input
        .hit_way_state2(hit_way_state_s),      // input
        .hit1(hit),                // input
        .hit2(hit_s),                // input
        .instr_type(instr_type),          // input    // read = 0(), write = 1
        .is_mem_fetch(is_mem_fetch),        // input
        .is_bus_fetch(is_bus_fetch),        // input
        .bus_snoop(s_ACSNOOP_reg),           // input
        .is_R_R(is_R_R),
        
        .dirty(dirty),               // output
        .is_exclusive(is_exclusive),
        .next_state1(next_state),         // output
        .next_state2(next_state_s)          // output
    );
    
    // snoop controller - used to control the access of other Cache L1
    snoop_controller    snoop_controller
    (
        // system signals
        .ACLK(ACLK),        // input
        .ARESETn(ARESETn),     // input
        
        // Snoop Response Channel
        // receive request from other Cache L1
        .s_ACVALID(s_ACVALID),   // input
        .s_ACREADY(s_ACREADY),   // output
        // input   [ADDR_WIDTH-1:0] s_ACADDR
        .s_ACSNOOP(s_ACSNOOP),   // input
        // send response to other Cache L1
        .s_CVALID(s_CVALID),    // output
        .s_CREADY(s_CREADY),    // input
        // output  [DATA_WIDTH-1:0] s_CDATA
        .s_CLAST(s_CLAST),     // output
        .s_CHIT(s_CHIT),      // output
        
        // signals to control datapath
        // input from checker_port2_REG
        .hit(hit_s),                             // input
        .state_tag_w_en(state_tag_w_en_s),                  // output
        .control_offset(control_offset_s),                  // output
        .bus_in_reg_en(bus_in_reg_en)                   // output
        // .checker_port2_out_reg_en(),        // output
        // .moesi_controller_out_reg()         // output
    );

    // cache controller - used to control the access of CPU
    cache_controller    cache_controller
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
        // input   [ADDR_WIDTH-1:0] m_AWADDR,
        
        // W Channel
        .m_WVALID(m_WVALID),
        .m_WREADY(m_WREADY),
        // input   [DATA_WIDTH-1:0] m_WDATA(),
        .m_WSTRB(m_WSTRB), // use default value: 0xF
        
        // B Channel
        .m_BVALID(m_BVALID),
        .m_BREADY(m_BREADY),
        .m_BRESP(m_BRESP),
        
        // AR Channel
        .m_ARVALID(m_ARVALID),
        .m_ARREADY(m_ARREADY),
        // input   [ADDR_WIDTH-1:0] m_ARADDR,
        
        // R Channel
        .m_RVALID(m_RVALID),
        .m_RREADY(m_RREADY),
        // output  [DATA_WIDTH-1:0] m_RDATA(),
        .m_RRESP(m_RRESP),
        
        // AXI5 Interface (connect with Cache L2)
        // AW Channel
        .s_AWID(s_AWID), // use default value: 0x0
        // output  [ADDR_WIDTH-1:0] s_AWADDR,
        .s_AWLEN(s_AWLEN),
        .s_AWSIZE(s_AWSIZE),  // use default value: Data bus width = 32-bit -> AWSIZE = 0x2
        .s_AWBURST(s_AWBURST), // use default value: 0x1(), INCR   
        .s_AWVALID(s_AWVALID),
        .s_AWREADY(s_AWREADY),
        
        // W Channel
        .s_WID(s_WID),  // use default value: 0x0
        // output  [DATA_WIDTH-1:0] s_WDATA(),
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
        // output  [ADDR_WIDTH-1:0] s_ARADDR(),
        .s_ARLEN(s_ARLEN),
        .s_ARSIZE(s_ARSIZE),  // use default value: Data bus width = 32-bit -> ARSIZE = 0x2
        .s_ARBURST(s_ARBURST), // use default value: 0x1(), INCR  
        .s_ARVALID(s_ARVALID),
        .s_ARREADY(s_ARREADY),
        
        // R Channel
        .s_RID(s_RID),  // use default value: 0x0
        // input   [DATA_WIDTH-1:0] s_RDATA(),
        .s_RRESP(s_RRESP),
        .s_RLAST(s_RLAST),
        .s_RVALID(s_RVALID),
        .s_RREADY(s_RREADY),
        
        // Snoop Request Channel
        // send request to other Cache L1
        .m_ACVALID(m_ACVALID),
        .m_ACREADY(m_ACREADY),
        // output  [ADDR_WIDTH-1:0] m_ACADDR(),
        .m_ACSNOOP(m_ACSNOOP),
        // receive response from other Cache L1
        .m_CVALID(m_CVALID),
        .m_CREADY(m_CREADY),
        // input   [DATA_WIDTH-1:0] m_CDATA(),
        .m_CLAST(m_CLAST),
        .m_CHIT(m_CHIT),
        
        // signals to control datapath
        .hit(hit),
        .dirty(dirty),
        .full(full),
        .instr_type(instr_type),   // read = 0, write = 1
        .is_exclusive(is_exclusive),
        
        // .mem_wb(mem_wb),
        .plrut_w_en(plrut_w_en),
        .state_tag_w_en(state_tag_w_en),
        .data_w_en(data_w_en),
        
        .mem_bus_fetch(mem_bus_fetch),
        .control_offset(control_offset),
        .w_data_sel(w_data_sel),
        .is_mem_fetch(is_mem_fetch),
        .is_bus_fetch(is_bus_fetch),
        
        .cpu_m_aw_in_reg_en(cpu_m_aw_in_reg_en),
        .cpu_m_w_in_reg_en(cpu_m_w_in_reg_en),
        .cpu_m_ar_in_reg_en(cpu_m_ar_in_reg_en),
        
        .mem_s_aw_out_reg_en(mem_s_aw_out_reg_en),
        .mem_s_ar_out_reg_en(mem_s_ar_out_reg_en),
        
        .bus_m_ac_out_reg_en(bus_m_ac_out_reg_en)
        
        // .checker_port1_out_reg_en(),
        // .plrut_moesi_controller_out_en()
    );
    
endmodule
