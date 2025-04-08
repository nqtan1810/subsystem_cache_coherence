//////////////////////////////////////////////////////////////////////////////////
// this controller is used to control the access of requests coming from CPU
//////////////////////////////////////////////////////////////////////////////////


module cache_controller
(
    // system signals
    input   ACLK,
    input   ARESETn,
    input   ENABLE,
    output  reg CACHE_HIT,
    output  reg CACHE_BUSY,
    
    // AXI5-Lite Interface (connect with CPU)
    // AW Channel
    input   m_AWVALID,
    output  reg m_AWREADY,
    // input   [ADDR_WIDTH-1:0] m_AWADDR,
    
    // W Channel
    input   m_WVALID,
    output  reg m_WREADY,
    // input   [DATA_WIDTH-1:0] m_WDATA,
    input   [3:0] m_WSTRB, // use default value: 0xF
    
    // B Channel
    output  reg m_BVALID,
    input   m_BREADY,
    output  reg [1:0] m_BRESP,
    
    // AR Channel
    input   m_ARVALID,
    output  reg m_ARREADY,
    // input   [ADDR_WIDTH-1:0] m_ARADDR,
    
    // R Channel
    output  reg m_RVALID,
    input   m_RREADY,
    // output  [DATA_WIDTH-1:0] m_RDATA,
    output  reg [1:0] m_RRESP,
    
    // AXI5 Interface (connect with Cache L2)
    // AW Channel
    output  reg s_AWID, // use default value: 0x0
    // output  [ADDR_WIDTH-1:0] s_AWADDR,
    output  reg [3:0] s_AWLEN,
    output  reg [2:0] s_AWSIZE,  // use default value: Data bus width = 32-bit -> AWSIZE = 0x2
    output  reg [1:0] s_AWBURST, // use default value: 0x1, INCR   
    output  reg s_AWVALID,
    input   s_AWREADY,
    
    // W Channel
    output  reg s_WID,  // use default value: 0x0
    // output  [DATA_WIDTH-1:0] s_WDATA,
    output  reg [3:0] s_WSTRB,  // use default value: 0xF
    output  reg s_WLAST,
    output  reg s_WVALID,
    input   s_WREADY,
    
    // B Channel
    input   s_BID,  // use default value: 0x0
    input   [1:0] s_BRESP,  
    input   s_BVALID,
    output  reg s_BREADY,
    
    // AR Channel
    output  reg s_ARID, // use default value: 0x0
    // output  [ADDR_WIDTH-1:0] s_ARADDR,
    output  reg [3:0] s_ARLEN,
    output  reg [2:0] s_ARSIZE,  // use default value: Data bus width = 32-bit -> ARSIZE = 0x2
    output  reg [1:0] s_ARBURST, // use default value: 0x1, INCR  
    output  reg s_ARVALID,
    input   s_ARREADY,
    
    // R Channel
    input   s_RID,  // use default value: 0x0
    // input   [DATA_WIDTH-1:0] s_RDATA,
    input   [1:0] s_RRESP,
    input   s_RLAST,
    input   s_RVALID,
    output  reg s_RREADY,
    
    // Snoop Request Channel
    // send request to other Cache L1
    output  reg m_ACVALID,
    input   m_ACREADY,
    // output  [ADDR_WIDTH-1:0] m_ACADDR,
    output  reg [1:0] m_ACSNOOP,
    // receive response from other Cache L1
    input   m_CVALID,
    output  reg m_CREADY,
    // input   [DATA_WIDTH-1:0] m_CDATA,
    input   m_CLAST,
    input   m_CHIT,
    
    // signals to control datapath
    input hit,
    input dirty,
    input full,
    input instr_type,   // read = 0, write = 1
    input is_exclusive,
    
    // output reg mem_wb,
    output reg plrut_w_en,
    output reg state_tag_w_en,
    output reg data_w_en,
    
    output reg mem_bus_fetch,
    output reg [3:0] control_offset,
    output reg [1:0] w_data_sel,
    output reg is_mem_fetch,
    output reg is_bus_fetch,
    
    output reg cpu_m_aw_in_reg_en,
    output reg cpu_m_w_in_reg_en,
    output reg cpu_m_ar_in_reg_en,
    
    output reg mem_s_aw_out_reg_en,
    output reg mem_s_ar_out_reg_en,
    
    output reg bus_m_ac_out_reg_en
    
    // output  reg checker_port1_out_reg_en,
    // output  reg plrut_moesi_controller_out_en   // need to find way to reduce critical path
);

    // state definition
    localparam  IDLE      = 0;
    localparam  M_W_ADDR  = 1;
    localparam  M_W_DATA  = 2;
    localparam  M_W_RESP  = 3;
    localparam  M_R_ADDR  = 4;
    localparam  M_R_DATA  = 5;
    localparam  HIT_MISS  = 6;
    localparam  CPU_WRITE = 7;
    localparam  CPU_READ  = 8;
    localparam  REQ_BUS   = 9;
    localparam  WRITE_MEM = 10;
    localparam  S_W_ADDR  = 11;
    localparam  S_W_DATA  = 12;
    localparam  S_W_RESP  = 13;
    localparam  READ_MEM  = 14;
    localparam  S_R_ADDR  = 15;
    localparam  S_R_DATA  = 16;
    
    // variable to store state
    reg [4:0] state, next_state;
    
    // internal registers
    reg [3:0] word_cnt; // both sent_word_cnt and rcv_word_cnt
    reg handshake_done;
    reg fetch_done; // used to synchronize --> create a temp clk to check hit again when completing fetch from Cache L1/Other Cache L1
    // reg interrupt_req_bus; // used to indicate Cache L1 has been interrup REQ_BUS and change to READ_MEM to fix core0 snoop hit and core1 write-back
    
    always @(posedge ACLK) begin
        if (!ARESETn) begin
            state <= IDLE;
        end
        else 
        if (ENABLE) begin
            state <= next_state;
        end
    end
    
    always @(*) begin
        case (state)
            IDLE      : next_state = m_AWVALID ? M_W_ADDR : (m_ARVALID ? M_R_ADDR : IDLE);
            M_W_ADDR  : next_state = m_AWVALID ? M_W_DATA : M_W_ADDR;
            M_W_DATA  : next_state = m_WVALID ? HIT_MISS : M_W_DATA;
            M_W_RESP  : next_state = m_BREADY ? IDLE : M_W_RESP;
            M_R_ADDR  : next_state = m_ARVALID ? HIT_MISS : M_R_ADDR;
            M_R_DATA  : next_state = m_RREADY ? IDLE : M_R_DATA;
            HIT_MISS  : next_state = hit ? (instr_type ? (is_exclusive ? CPU_WRITE : REQ_BUS) : CPU_READ) : (full && dirty ? WRITE_MEM : REQ_BUS);
            CPU_WRITE : next_state = M_W_RESP;
            CPU_READ  : next_state = M_R_DATA;
            // REQ_BUS   : next_state = (m_CVALID && m_CLAST) ? (m_CHIT ? (instr_type ? CPU_WRITE : CPU_READ) : (hit ? CPU_WRITE : READ_MEM)) : REQ_BUS;
            // REQ_BUS   : next_state = m_CVALID ? (m_CHIT ? (m_CLAST ? (instr_type ? CPU_WRITE : CPU_READ) : REQ_BUS) : (hit ? CPU_WRITE : READ_MEM)) : REQ_BUS;
            REQ_BUS   : next_state = (m_CVALID && !m_CHIT) ? (hit ? CPU_WRITE : READ_MEM) : ((m_CVALID && hit) ? CPU_WRITE : (fetch_done ? (instr_type ? CPU_WRITE : CPU_READ) : REQ_BUS));
            // REQ_BUS   : next_state = m_CVALID ? (hit ? CPU_WRITE : (m_CHIT ? REQ_BUS : READ_MEM)) : (fetch_done ? (instr_type ? CPU_WRITE : CPU_READ) : REQ_BUS);
            WRITE_MEM : next_state = S_W_ADDR;
            S_W_ADDR  : next_state = s_AWREADY ? S_W_DATA : S_W_ADDR;
            S_W_DATA  : next_state = (word_cnt == 4'b1111 && s_WREADY) ? S_W_RESP : S_W_DATA;
            S_W_RESP  : next_state = s_BVALID ? REQ_BUS : S_W_RESP;
            READ_MEM  : next_state = S_R_ADDR;
            S_R_ADDR  : next_state = s_ARREADY ? S_R_DATA : S_R_ADDR;
            // S_R_DATA  : next_state = (s_RVALID && s_RLAST) ? (instr_type ? CPU_WRITE : CPU_READ) : S_R_DATA;
            S_R_DATA  : next_state = fetch_done ? (instr_type ? CPU_WRITE : CPU_READ) : S_R_DATA;
            default   : next_state = IDLE;
        endcase
    end
    
    always @(*) begin
        case (state)
            IDLE      : begin
                CACHE_HIT = 0;
                CACHE_BUSY = 0;
                m_AWREADY = 0;
                m_WREADY = 0;
                m_BVALID = 0;
                m_BRESP = 0;
                m_ARREADY = 0;
                m_RVALID = 0;
                m_RRESP = 0;
                s_AWID = 0;
                s_AWLEN = 4'h0;
                s_AWSIZE = 3'h0;
                s_AWBURST = 2'h1;
                s_AWVALID = 0;
                s_WID = 0;
                s_WSTRB = 4'hF;
                s_WLAST = 0;
                s_WVALID = 0;
                s_BREADY = 0;
                s_ARID = 0;
                s_ARLEN = 4'h0;
                s_ARSIZE = 3'h0;
                s_ARBURST = 2'h1;
                s_ARVALID = 0;
                s_RREADY = 0;
                m_ACVALID = 0;
                m_ACSNOOP = 2'h0;
                m_CREADY = 0;
                // internal signals
                // mem_wb = 0;
                plrut_w_en = 0;
                state_tag_w_en = 0;
                data_w_en = 0;
                mem_bus_fetch = 0;
                control_offset = 4'b0000;
                w_data_sel = 2'b00;
                is_mem_fetch = 0;
                is_bus_fetch = 0;
                cpu_m_aw_in_reg_en = 0;
                cpu_m_w_in_reg_en = 0;
                cpu_m_ar_in_reg_en = 0;
                mem_s_aw_out_reg_en = 0;
                mem_s_ar_out_reg_en = 0;
                bus_m_ac_out_reg_en = 0;
                // checker_port1_out_reg_en = 0;
                // plrut_moesi_controller_out_en = 0;
            end
            M_W_ADDR  : begin
                CACHE_HIT = 0;
                CACHE_BUSY = 1;
                m_AWREADY = 1;
                m_WREADY = 0;
                m_BVALID = 0;
                m_BRESP = 0;
                m_ARREADY = 0;
                m_RVALID = 0;
                m_RRESP = 0;
                s_AWID = 0;
                s_AWLEN = 4'h0;
                s_AWSIZE = 3'h0;
                s_AWBURST = 2'h1;
                s_AWVALID = 0;
                s_WID = 0;
                s_WSTRB = 4'hF;
                s_WLAST = 0;
                s_WVALID = 0;
                s_BREADY = 0;
                s_ARID = 0;
                s_ARLEN = 4'h0;
                s_ARSIZE = 3'h0;
                s_ARBURST = 2'h1;
                s_ARVALID = 0;
                s_RREADY = 0;
                m_ACVALID = 0;
                m_ACSNOOP = 2'h0;
                m_CREADY = 0;
                // internal signals
                // mem_wb = 0;
                plrut_w_en = 0;
                state_tag_w_en = 0;
                data_w_en = 0;
                mem_bus_fetch = 0;
                control_offset = 4'b0000;
                w_data_sel = 2'b00;
                is_mem_fetch = 0;
                is_bus_fetch = 0;
                cpu_m_aw_in_reg_en = 1;
                cpu_m_w_in_reg_en = 0;
                cpu_m_ar_in_reg_en = 0;
                mem_s_aw_out_reg_en = 0;
                mem_s_ar_out_reg_en = 0;
                bus_m_ac_out_reg_en = 0;
                // checker_port1_out_reg_en = 0;
                // plrut_moesi_controller_out_en = 0;
            end
            M_W_DATA  : begin
                CACHE_HIT = 0;
                CACHE_BUSY = 1;
                m_AWREADY = 0;
                m_WREADY = 1;
                m_BVALID = 0;
                m_BRESP = 0;
                m_ARREADY = 0;
                m_RVALID = 0;
                m_RRESP = 0;
                s_AWID = 0;
                s_AWLEN = 4'h0;
                s_AWSIZE = 3'h0;
                s_AWBURST = 2'h1;
                s_AWVALID = 0;
                s_WID = 0;
                s_WSTRB = 4'hF;
                s_WLAST = 0;
                s_WVALID = 0;
                s_BREADY = 0;
                s_ARID = 0;
                s_ARLEN = 4'h0;
                s_ARSIZE = 3'h0;
                s_ARBURST = 2'h1;
                s_ARVALID = 0;
                s_RREADY = 0;
                m_ACVALID = 0;
                m_ACSNOOP = 2'h0;
                m_CREADY = 0;
                // internal signals
                // mem_wb = 0;
                plrut_w_en = 0;
                state_tag_w_en = 0;
                data_w_en = 0;
                mem_bus_fetch = 0;
                control_offset = 4'b0000;
                w_data_sel = 2'b00;
                is_mem_fetch = 0;
                is_bus_fetch = 0;
                cpu_m_aw_in_reg_en = 0;
                cpu_m_w_in_reg_en = 1;
                cpu_m_ar_in_reg_en = 0;
                mem_s_aw_out_reg_en = 0;
                mem_s_ar_out_reg_en = 0;
                bus_m_ac_out_reg_en = 0;
                // checker_port1_out_reg_en = 0;
                // plrut_moesi_controller_out_en = 0;
            end
            M_W_RESP  : begin
                CACHE_HIT = 0;
                CACHE_BUSY = 1;
                m_AWREADY = 0;
                m_WREADY = 0;
                m_BVALID = 1;
                m_BRESP = 0;
                m_ARREADY = 0;
                m_RVALID = 0;
                m_RRESP = 0;
                s_AWID = 0;
                s_AWLEN = 4'h0;
                s_AWSIZE = 3'h0;
                s_AWBURST = 2'h1;
                s_AWVALID = 0;
                s_WID = 0;
                s_WSTRB = 4'hF;
                s_WLAST = 0;
                s_WVALID = 0;
                s_BREADY = 0;
                s_ARID = 0;
                s_ARLEN = 4'h0;
                s_ARSIZE = 3'h0;
                s_ARBURST = 2'h1;
                s_ARVALID = 0;
                s_RREADY = 0;
                m_ACVALID = 0;
                m_ACSNOOP = 2'h0;
                m_CREADY = 0;
                // internal signals
                // mem_wb = 0;
                plrut_w_en = 0;
                state_tag_w_en = 0;
                data_w_en = 0;
                mem_bus_fetch = 0;
                control_offset = 4'b0000;
                w_data_sel = 2'b00;
                is_mem_fetch = 0;
                is_bus_fetch = 0;
                cpu_m_aw_in_reg_en = 0;
                cpu_m_w_in_reg_en = 0;
                cpu_m_ar_in_reg_en = 0;
                mem_s_aw_out_reg_en = 0;
                mem_s_ar_out_reg_en = 0;
                bus_m_ac_out_reg_en = 0;
                // checker_port1_out_reg_en = 0;
                // plrut_moesi_controller_out_en = 0;
            end
            M_R_ADDR  : begin
                CACHE_HIT = 0;
                CACHE_BUSY = 1;
                m_AWREADY = 0;
                m_WREADY = 0;
                m_BVALID = 0;
                m_BRESP = 0;
                m_ARREADY = 1;
                m_RVALID = 0;
                m_RRESP = 0;
                s_AWID = 0;
                s_AWLEN = 4'h0;
                s_AWSIZE = 3'h0;
                s_AWBURST = 2'h1;
                s_AWVALID = 0;
                s_WID = 0;
                s_WSTRB = 4'hF;
                s_WLAST = 0;
                s_WVALID = 0;
                s_BREADY = 0;
                s_ARID = 0;
                s_ARLEN = 4'h0;
                s_ARSIZE = 3'h0;
                s_ARBURST = 2'h1;
                s_ARVALID = 0;
                s_RREADY = 0;
                m_ACVALID = 0;
                m_ACSNOOP = 2'h0;
                m_CREADY = 0;
                // internal signals
                // mem_wb = 0;
                plrut_w_en = 0;
                state_tag_w_en = 0;
                data_w_en = 0;
                mem_bus_fetch = 0;
                control_offset = 4'b0000;
                w_data_sel = 2'b00;
                is_mem_fetch = 0;
                is_bus_fetch = 0;
                cpu_m_aw_in_reg_en = 0;
                cpu_m_w_in_reg_en = 0;
                cpu_m_ar_in_reg_en = 1;
                mem_s_aw_out_reg_en = 0;
                mem_s_ar_out_reg_en = 0;
                bus_m_ac_out_reg_en = 0;
                // checker_port1_out_reg_en = 0;
                // plrut_moesi_controller_out_en = 0;
            end
            M_R_DATA  : begin
                CACHE_HIT = 0;
                CACHE_BUSY = 1;
                m_AWREADY = 0;
                m_WREADY = 0;
                m_BVALID = 0;
                m_BRESP = 0;
                m_ARREADY = 0;
                m_RVALID = 1;
                m_RRESP = 0;
                s_AWID = 0;
                s_AWLEN = 4'h0;
                s_AWSIZE = 3'h0;
                s_AWBURST = 2'h1;
                s_AWVALID = 0;
                s_WID = 0;
                s_WSTRB = 4'hF;
                s_WLAST = 0;
                s_WVALID = 0;
                s_BREADY = 0;
                s_ARID = 0;
                s_ARLEN = 4'h0;
                s_ARSIZE = 3'h0;
                s_ARBURST = 2'h1;
                s_ARVALID = 0;
                s_RREADY = 0;
                m_ACVALID = 0;
                m_ACSNOOP = 2'h0;
                m_CREADY = 0;
                // internal signals
                // mem_wb = 0;
                plrut_w_en = 0;
                state_tag_w_en = 0;
                data_w_en = 0;
                mem_bus_fetch = 0;
                control_offset = 4'b0000;
                w_data_sel = 2'b00;
                is_mem_fetch = 0;
                is_bus_fetch = 0;
                cpu_m_aw_in_reg_en = 0;
                cpu_m_w_in_reg_en = 0;
                cpu_m_ar_in_reg_en = 0;
                mem_s_aw_out_reg_en = 0;
                mem_s_ar_out_reg_en = 0;
                bus_m_ac_out_reg_en = 0;
                // checker_port1_out_reg_en = 0;
                // plrut_moesi_controller_out_en = 0;
            end
            HIT_MISS  : begin
                CACHE_HIT = hit;
                CACHE_BUSY = 1;
                m_AWREADY = 0;
                m_WREADY = 0;
                m_BVALID = 0;
                m_BRESP = 0;
                m_ARREADY = 0;
                m_RVALID = 0;
                m_RRESP = 0;
                s_AWID = 0;
                s_AWLEN = 4'h0;
                s_AWSIZE = 3'h0;
                s_AWBURST = 2'h1;
                s_AWVALID = 0;
                s_WID = 0;
                s_WSTRB = 4'hF;
                s_WLAST = 0;
                s_WVALID = 0;
                s_BREADY = 0;
                s_ARID = 0;
                s_ARLEN = 4'h0;
                s_ARSIZE = 3'h0;
                s_ARBURST = 2'h1;
                s_ARVALID = 0;
                s_RREADY = 0;
                m_ACVALID = 0;
                m_ACSNOOP = 2'h0;
                m_CREADY = 0;
                // internal signals
                // mem_wb = 0;
                plrut_w_en = 0;
                state_tag_w_en = 0;
                data_w_en = 0;
                mem_bus_fetch = 0;
                control_offset = 4'b0000;
                w_data_sel = 2'b00;
                is_mem_fetch = 0;
                is_bus_fetch = 0;
                cpu_m_aw_in_reg_en = 0;
                cpu_m_w_in_reg_en = 0;
                cpu_m_ar_in_reg_en = 0;
                mem_s_aw_out_reg_en = 0;
                mem_s_ar_out_reg_en = 0;
                bus_m_ac_out_reg_en = (hit && (!instr_type)) ? 0 : 1;
                // checker_port1_out_reg_en = 1;
                // plrut_moesi_controller_out_en = 1;
            end
            CPU_WRITE : begin
                CACHE_HIT = hit;
                CACHE_BUSY = 1;
                m_AWREADY = 0;
                m_WREADY = 0;
                m_BVALID = 0;
                m_BRESP = 0;
                m_ARREADY = 0;
                m_RVALID = 0;
                m_RRESP = 0;
                s_AWID = 0;
                s_AWLEN = 4'h0;
                s_AWSIZE = 3'h0;
                s_AWBURST = 2'h1;
                s_AWVALID = 0;
                s_WID = 0;
                s_WSTRB = 4'hF;
                s_WLAST = 0;
                s_WVALID = 0;
                s_BREADY = 0;
                s_ARID = 0;
                s_ARLEN = 4'h0;
                s_ARSIZE = 3'h0;
                s_ARBURST = 2'h1;
                s_ARVALID = 0;
                s_RREADY = 0;
                m_ACVALID = 0;
                m_ACSNOOP = 2'h0;
                m_CREADY = 0;
                // internal signals
                // mem_wb = 0;
                plrut_w_en = 1;
                state_tag_w_en = 1;
                data_w_en = 1;
                mem_bus_fetch = 0;
                control_offset = 4'b0000;
                w_data_sel = 2'b00;
                is_mem_fetch = 0;
                is_bus_fetch = 0;
                cpu_m_aw_in_reg_en = 0;
                cpu_m_w_in_reg_en = 0;
                cpu_m_ar_in_reg_en = 0;
                mem_s_aw_out_reg_en = 0;
                mem_s_ar_out_reg_en = 0;
                bus_m_ac_out_reg_en = 0;
                // checker_port1_out_reg_en = 0;
                // plrut_moesi_controller_out_en = 0;
            end
            CPU_READ  : begin
                CACHE_HIT = hit;
                CACHE_BUSY = 1;
                m_AWREADY = 0;
                m_WREADY = 0;
                m_BVALID = 0;
                m_BRESP = 0;
                m_ARREADY = 0;
                m_RVALID = 0;
                m_RRESP = 0;
                s_AWID = 0;
                s_AWLEN = 4'h0;
                s_AWSIZE = 3'h0;
                s_AWBURST = 2'h1;
                s_AWVALID = 0;
                s_WID = 0;
                s_WSTRB = 4'hF;
                s_WLAST = 0;
                s_WVALID = 0;
                s_BREADY = 0;
                s_ARID = 0;
                s_ARLEN = 4'h0;
                s_ARSIZE = 3'h0;
                s_ARBURST = 2'h1;
                s_ARVALID = 0;
                s_RREADY = 0;
                m_ACVALID = 0;
                m_ACSNOOP = 2'h0;
                m_CREADY = 0;
                // internal signals
                // mem_wb = 0;
                plrut_w_en = 1;
                state_tag_w_en = 0;
                data_w_en = 0;
                mem_bus_fetch = 0;
                control_offset = 4'b0000;
                w_data_sel = 2'b00;
                is_mem_fetch = 0;
                is_bus_fetch = 0;
                cpu_m_aw_in_reg_en = 0;
                cpu_m_w_in_reg_en = 0;
                cpu_m_ar_in_reg_en = 0;
                mem_s_aw_out_reg_en = 0;
                mem_s_ar_out_reg_en = 0;
                bus_m_ac_out_reg_en = 0;
                // checker_port1_out_reg_en = 0;
                // plrut_moesi_controller_out_en = 0;
            end
            REQ_BUS   : begin
                CACHE_HIT = 0;
                CACHE_BUSY = 1;
                m_AWREADY = 0;
                m_WREADY = 0;
                m_BVALID = 0;
                m_BRESP = 0;
                m_ARREADY = 0;
                m_RVALID = 0;
                m_RRESP = 0;
                s_AWID = 0;
                s_AWLEN = 4'h0;
                s_AWSIZE = 3'h0;
                s_AWBURST = 2'h1;
                s_AWVALID = 0;
                s_WID = 0;
                s_WSTRB = 4'hF;
                s_WLAST = 0;
                s_WVALID = 0;
                s_BREADY = 0;
                s_ARID = 0;
                s_ARLEN = 4'h0;
                s_ARSIZE = 3'h0;
                s_ARBURST = 2'h1;
                s_ARVALID = 0;
                s_RREADY = 0;
                m_ACVALID = ~handshake_done;
                m_ACSNOOP = instr_type ? (hit ? 2'h2 : 2'h1) : 2'h0;
                m_CREADY = 1;
                // internal signals
                // mem_wb = 0;
                plrut_w_en = 0/*(~hit & m_CVALID & m_CHIT & m_CLAST)*/;
                // state_tag_w_en = (~hit & m_CVALID & m_CHIT & m_CLAST);
                // state_tag_w_en = word_cnt == 4'b1110;
                state_tag_w_en = (word_cnt == 4'b1111) & m_CHIT;
                data_w_en = (~hit & m_CVALID & m_CHIT);
                mem_bus_fetch = 1;
                control_offset = word_cnt;
                w_data_sel = 2'b01;
                is_mem_fetch = 0;
                is_bus_fetch = 1;
                cpu_m_aw_in_reg_en = 0;
                cpu_m_w_in_reg_en = 0;
                cpu_m_ar_in_reg_en = 0;
                mem_s_aw_out_reg_en = 0;
                mem_s_ar_out_reg_en = 0;
                bus_m_ac_out_reg_en = 0;
                // checker_port1_out_reg_en = 0;
                // plrut_moesi_controller_out_en = 0;
            end
            WRITE_MEM : begin
                CACHE_HIT = 0;
                CACHE_BUSY = 1;
                m_AWREADY = 0;
                m_WREADY = 0;
                m_BVALID = 0;
                m_BRESP = 0;
                m_ARREADY = 0;
                m_RVALID = 0;
                m_RRESP = 0;
                s_AWID = 0;
                s_AWLEN = 4'h0;
                s_AWSIZE = 3'h0;
                s_AWBURST = 2'h1;
                s_AWVALID = 0;
                s_WID = 0;
                s_WSTRB = 4'hF;
                s_WLAST = 0;
                s_WVALID = 0;
                s_BREADY = 0;
                s_ARID = 0;
                s_ARLEN = 4'h0;
                s_ARSIZE = 3'h0;
                s_ARBURST = 2'h1;
                s_ARVALID = 0;
                s_RREADY = 0;
                m_ACVALID = 0;
                m_ACSNOOP = 2'h0;
                m_CREADY = 0;
                // internal signals
                // mem_wb = 1;
                plrut_w_en = 0;
                state_tag_w_en = 0;
                data_w_en = 0;
                mem_bus_fetch = 0;
                control_offset = 4'b0000;
                w_data_sel = 2'b00;
                is_mem_fetch = 0;
                is_bus_fetch = 0;
                cpu_m_aw_in_reg_en = 0;
                cpu_m_w_in_reg_en = 0;
                cpu_m_ar_in_reg_en = 0;
                mem_s_aw_out_reg_en = 1;
                mem_s_ar_out_reg_en = 0;
                bus_m_ac_out_reg_en = 0;
                // checker_port1_out_reg_en = 0;
                // plrut_moesi_controller_out_en = 0;
            end
            S_W_ADDR  : begin
                CACHE_HIT = 0;
                CACHE_BUSY = 1;
                m_AWREADY = 0;
                m_WREADY = 0;
                m_BVALID = 0;
                m_BRESP = 0;
                m_ARREADY = 0;
                m_RVALID = 0;
                m_RRESP = 0;
                s_AWID = 0;
                s_AWLEN = 4'hF;
                s_AWSIZE = 3'h2;
                s_AWBURST = 2'h1;
                s_AWVALID = 1;
                s_WID = 0;
                s_WSTRB = 4'hF;
                s_WLAST = 0;
                s_WVALID = 0;
                s_BREADY = 0;
                s_ARID = 0;
                s_ARLEN = 4'h0;
                s_ARSIZE = 3'h0;
                s_ARBURST = 2'h1;
                s_ARVALID = 0;
                s_RREADY = 0;
                m_ACVALID = 0;
                m_ACSNOOP = 2'h0;
                m_CREADY = 0;
                // internal signals
                // mem_wb = 1;
                plrut_w_en = 0;
                state_tag_w_en = 0;
                data_w_en = 0;
                mem_bus_fetch = 1;
                control_offset = 4'b0000;
                w_data_sel = 2'b00;
                is_mem_fetch = 0;
                is_bus_fetch = 0;
                cpu_m_aw_in_reg_en = 0;
                cpu_m_w_in_reg_en = 0;
                cpu_m_ar_in_reg_en = 0;
                mem_s_aw_out_reg_en = 0;
                mem_s_ar_out_reg_en = 0;
                bus_m_ac_out_reg_en = 0;
                // checker_port1_out_reg_en = 0;
                // plrut_moesi_controller_out_en = 0;
            end
            S_W_DATA  : begin
                CACHE_HIT = 0;
                CACHE_BUSY = 1;
                m_AWREADY = 0;
                m_WREADY = 0;
                m_BVALID = 0;
                m_BRESP = 0;
                m_ARREADY = 0;
                m_RVALID = 0;
                m_RRESP = 0;
                s_AWID = 0;
                s_AWLEN = 4'hF;
                s_AWSIZE = 3'h2;
                s_AWBURST = 2'h1;
                s_AWVALID = 0;
                s_WID = 0;
                s_WSTRB = 4'hF;
                s_WLAST = (word_cnt == 4'b1111) ? 1 : 0;
                s_WVALID = 1;
                s_BREADY = 0;
                s_ARID = 0;
                s_ARLEN = 4'h0;
                s_ARSIZE = 3'h0;
                s_ARBURST = 2'h1;
                s_ARVALID = 0;
                s_RREADY = 0;
                m_ACVALID = 0;
                m_ACSNOOP = 2'h0;
                m_CREADY = 0;
                // internal signals
                // mem_wb = 1;
                plrut_w_en = 0;
                state_tag_w_en = s_WLAST & s_WREADY;
                data_w_en = 0;
                mem_bus_fetch = 1;
                control_offset = word_cnt + 1;
                w_data_sel = 2'b00;
                is_mem_fetch = 0;
                is_bus_fetch = 0;
                cpu_m_aw_in_reg_en = 0;
                cpu_m_w_in_reg_en = 0;
                cpu_m_ar_in_reg_en = 0;
                mem_s_aw_out_reg_en = 0;
                mem_s_ar_out_reg_en = 0;
                bus_m_ac_out_reg_en = 0;
                // checker_port1_out_reg_en = 0;
                // plrut_moesi_controller_out_en = 0;
            end
            S_W_RESP  : begin
                CACHE_HIT = 0;
                CACHE_BUSY = 1;
                m_AWREADY = 0;
                m_WREADY = 0;
                m_BVALID = 0;
                m_BRESP = 0;
                m_ARREADY = 0;
                m_RVALID = 0;
                m_RRESP = 0;
                s_AWID = 0;
                s_AWLEN = 4'hF;
                s_AWSIZE = 3'h2;
                s_AWBURST = 2'h1;
                s_AWVALID = 0;
                s_WID = 0;
                s_WSTRB = 4'hF;
                s_WLAST = 0;
                s_WVALID = 0;
                s_BREADY = 1;
                s_ARID = 0;
                s_ARLEN = 4'h0;
                s_ARSIZE = 3'h0;
                s_ARBURST = 2'h1;
                s_ARVALID = 0;
                s_RREADY = 0;
                m_ACVALID = 0;
                m_ACSNOOP = 2'h0;
                m_CREADY = 0;
                // internal signals
                // mem_wb = 1;
                plrut_w_en = 0;
                state_tag_w_en = 0;
                data_w_en = 0;
                mem_bus_fetch = 0;
                control_offset = 4'b0000;
                w_data_sel = 2'b00;
                is_mem_fetch = 0;
                is_bus_fetch = 0;
                cpu_m_aw_in_reg_en = 0;
                cpu_m_w_in_reg_en = 0;
                cpu_m_ar_in_reg_en = 0;
                mem_s_aw_out_reg_en = 0;
                mem_s_ar_out_reg_en = 0;
                bus_m_ac_out_reg_en = 0;
                // checker_port1_out_reg_en = 0;
                // plrut_moesi_controller_out_en = 0;
            end
            READ_MEM  : begin
                CACHE_HIT = 0;
                CACHE_BUSY = 1;
                m_AWREADY = 0;
                m_WREADY = 0;
                m_BVALID = 0;
                m_BRESP = 0;
                m_ARREADY = 0;
                m_RVALID = 0;
                m_RRESP = 0;
                s_AWID = 0;
                s_AWLEN = 4'h0;
                s_AWSIZE = 3'h0;
                s_AWBURST = 2'h1;
                s_AWVALID = 0;
                s_WID = 0;
                s_WSTRB = 4'hF;
                s_WLAST = 0;
                s_WVALID = 0;
                s_BREADY = 0;
                s_ARID = 0;
                s_ARLEN = 4'h0;
                s_ARSIZE = 3'h0;
                s_ARBURST = 2'h1;
                s_ARVALID = 0;
                s_RREADY = 0;
                m_ACVALID = 0;
                m_ACSNOOP = 2'h0;
                m_CREADY = 1;
                // internal signals
                // mem_wb = 0;
                plrut_w_en = 0;
                state_tag_w_en = 0;
                data_w_en = 0;
                mem_bus_fetch = 0;
                control_offset = 4'b0000;
                w_data_sel = 2'b10;
                is_mem_fetch = 0;
                is_bus_fetch = 0;
                cpu_m_aw_in_reg_en = 0;
                cpu_m_w_in_reg_en = 0;
                cpu_m_ar_in_reg_en = 0;
                mem_s_aw_out_reg_en = 0;
                mem_s_ar_out_reg_en = 1;
                bus_m_ac_out_reg_en = 0;
                // checker_port1_out_reg_en = 0;
                // plrut_moesi_controller_out_en = 0;
            end
            S_R_ADDR  : begin
                CACHE_HIT = 0;
                CACHE_BUSY = 1;
                m_AWREADY = 0;
                m_WREADY = 0;
                m_BVALID = 0;
                m_BRESP = 0;
                m_ARREADY = 0;
                m_RVALID = 0;
                m_RRESP = 0;
                s_AWID = 0;
                s_AWLEN = 4'h0;
                s_AWSIZE = 3'h0;
                s_AWBURST = 2'h1;
                s_AWVALID = 0;
                s_WID = 0;
                s_WSTRB = 4'hF;
                s_WLAST = 0;
                s_WVALID = 0;
                s_BREADY = 0;
                s_ARID = 0;
                s_ARLEN = 4'hF;
                s_ARSIZE = 3'h2;
                s_ARBURST = 2'h1;
                s_ARVALID = 1;
                s_RREADY = 0;
                m_ACVALID = 0;
                m_ACSNOOP = 2'h0;
                m_CREADY = 1;
                // internal signals
                // mem_wb = 0;
                plrut_w_en = 0;
                state_tag_w_en = 0;
                data_w_en = 0;
                mem_bus_fetch = 1;
                control_offset = 4'b0000;
                w_data_sel = 2'b10;
                is_mem_fetch = 0;
                is_bus_fetch = 0;
                cpu_m_aw_in_reg_en = 0;
                cpu_m_w_in_reg_en = 0;
                cpu_m_ar_in_reg_en = 0;
                mem_s_aw_out_reg_en = 0;
                mem_s_ar_out_reg_en = 0;
                bus_m_ac_out_reg_en = 0;
                // checker_port1_out_reg_en = 0;
                // plrut_moesi_controller_out_en = 0;
            end
            S_R_DATA  : begin
                CACHE_HIT = 0;
                CACHE_BUSY = 1;
                m_AWREADY = 0;
                m_WREADY = 0;
                m_BVALID = 0;
                m_BRESP = 0;
                m_ARREADY = 0;
                m_RVALID = 0;
                m_RRESP = 0;
                s_AWID = 0;
                s_AWLEN = 4'h0;
                s_AWSIZE = 3'h0;
                s_AWBURST = 2'h1;
                s_AWVALID = 0;
                s_WID = 0;
                s_WSTRB = 4'hF;
                s_WLAST = 0;
                s_WVALID = 0;
                s_BREADY = 0;
                s_ARID = 0;
                s_ARLEN = 4'h0;
                s_ARSIZE = 3'h0;
                s_ARBURST = 2'h1;
                s_ARVALID = 0;
                s_RREADY = 1;
                m_ACVALID = 0;
                m_ACSNOOP = 2'h0;
                m_CREADY = 1;
                // internal signals
                // mem_wb = 0;
                plrut_w_en = 0/*s_RVALID & s_RLAST*/;
                state_tag_w_en = s_RVALID & s_RLAST;
                // state_tag_w_en = word_cnt == 4'b1110;
                data_w_en = s_RVALID;
                mem_bus_fetch = 1;
                control_offset = word_cnt;
                w_data_sel = 2'b10;
                is_mem_fetch = 1;
                is_bus_fetch = 0;
                cpu_m_aw_in_reg_en = 0;
                cpu_m_w_in_reg_en = 0;
                cpu_m_ar_in_reg_en = 0;
                mem_s_aw_out_reg_en = 0;
                mem_s_ar_out_reg_en = 0;
                bus_m_ac_out_reg_en = 0;
                // checker_port1_out_reg_en = 0;
                // plrut_moesi_controller_out_en = 0;
            end
            default   : begin
                CACHE_HIT = 0;
                CACHE_BUSY = 0;
                m_AWREADY = 0;
                m_WREADY = 0;
                m_BVALID = 0;
                m_BRESP = 0;
                m_ARREADY = 0;
                m_RVALID = 0;
                m_RRESP = 0;
                s_AWID = 0;
                s_AWLEN = 4'h0;
                s_AWSIZE = 3'h0;
                s_AWBURST = 2'h1;
                s_AWVALID = 0;
                s_WID = 0;
                s_WSTRB = 4'hF;
                s_WLAST = 0;
                s_WVALID = 0;
                s_BREADY = 0;
                s_ARID = 0;
                s_ARLEN = 4'h0;
                s_ARSIZE = 3'h0;
                s_ARBURST = 2'h1;
                s_ARVALID = 0;
                s_RREADY = 0;
                m_ACVALID = 0;
                m_ACSNOOP = 2'h0;
                m_CREADY = 0;
                // internal signals
                // mem_wb = 0;
                plrut_w_en = 0;
                state_tag_w_en = 0;
                data_w_en = 0;
                mem_bus_fetch = 0;
                control_offset = 4'b0000;
                w_data_sel = 2'b00;
                is_mem_fetch = 0;
                is_bus_fetch = 0;
                cpu_m_aw_in_reg_en = 0;
                cpu_m_w_in_reg_en = 0;
                cpu_m_ar_in_reg_en = 0;
                mem_s_aw_out_reg_en = 0;
                mem_s_ar_out_reg_en = 0;
                bus_m_ac_out_reg_en = 0;
                // checker_port1_out_reg_en = 0;
                // plrut_moesi_controller_out_en = 0;
            end
        endcase
    end
    
    always @(posedge ACLK) begin
        if (!ARESETn) begin
            handshake_done <= 0;
            word_cnt <= 4'b0000;
            fetch_done <= 0;
            // interrupt_req_bus <= 0;
        end
        else begin
            if (state != next_state) begin
                handshake_done <= 0;
                word_cnt <= 4'b0000;
                fetch_done <= 0;
                // interrupt_req_bus <= 0;
            end
            else begin
                if (m_ACVALID && m_ACREADY) begin
                    handshake_done <= 1;
                end
                if (s_WREADY || s_RVALID || m_CVALID) begin
                    word_cnt <= word_cnt + 4'b0001;
                end
                if (((state == REQ_BUS) && m_CVALID && m_CLAST && m_CHIT) || ((state == S_R_DATA) && s_RVALID && s_RLAST)) begin
                    fetch_done <= 1;
                end
                // if (m_CVALID && !m_CHIT && !hit && word_cnt) begin
                //     interrupt_req_bus <= 1;
                // end
            end
        end
    end

endmodule
